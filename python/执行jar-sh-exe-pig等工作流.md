workflow.py
```
# coding=utf-8
import commands
import re
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

__author__ = 'min'

pattern_exp = re.compile(r'\$\{+[0-9A-Za-z]+\}')
pattern_map_class = re.compile(r'\$+[0-9A-Za-z]')


def exec_work_flow(work_flow, jar, main_class, start_action, end_action, params_dict_input):
    print 'exec the workflow '+work_flow
    params_dict = {}
    tree = ET.ElementTree(file=work_flow)
    root = tree.getroot()

    # step one , find the params
    params = root.find("params")
    for param in params:
        key = param.attrib.get('key')
        value = param.text
        if pattern_exp.match(value):
            value = params_dict_input.get(value)
        params_dict[key] = value
    print 'params:'+str(params_dict)

    # step two find the start
    start = start_action
    if start_action is None:
        start = root.find("start").attrib.get("to")

    # step 3,find all the actions
    actions = root.findall("action")
    action_dict = {}
    for action in actions:
        action_dict[action.attrib.get("name")] = action
    print 'actions:'+str(action_dict.keys())

    # finally , from 'start' to exec the actions
    iter_action_name = start
    iter_action = action_dict.get(iter_action_name)
    while iter_action_name != 'end' and iter_action != end_action and iter_action_name != 'fail':
        try:
            print 'cur action is :'+str(iter_action_name)
            iter_action = action_dict.get(iter_action_name)
            iter_action_name = exec_action(iter_action, jar, main_class, params_dict)
        except Exception, e:
            print 'except @ '+iter_action.attrib.get("name")
            error = action.find("error").attrib.get("to")
            if error.strip() == 'fail':
                raise RuntimeError("workflow fail: "+str(iter_action.attrib.get("name")))
            iter_action_name = error

    print 'the workflow end !'


# exec the action type of mapreduce
def exec_mr(action, jar, main_class, params_dict):
    print '--------------------------------------------------------------------------------------'
    print 'mr action '
    print '--------------------------------------------------------------------------------------'
    mr = action.find("map-reduce")
    prepare = mr.find("prepare")
    if prepare is not None:
        for prepare_del in prepare:
            delete_path = prepare_del.attrib.get("path")
            res = pattern_exp.findall(delete_path)
            for r in res:
                delete_path = delete_path.replace(r, params_dict.get(r.strip('${').strip('}')))
            print "delete path:"+delete_path
            commond_str = 'hadoop dfs -rm -r ' + str(delete_path)
            print 'exe command:'+commond_str
            r = commands.getstatusoutput(commond_str)
            print r
            print 'delete success '

    mr_commond_str = 'hadoop jar ' + jar + ' ' + main_class + ' '
    configuration = mr.find("configuration")
    no_job_name = True
    for property in configuration:
        name = property.find("name").text
        if 'mapred.job.name' in name:
            no_job_name = False
        value = property.find("value").text
        res = pattern_exp.findall(value)
        for re in res:
            value = value.replace(re, params_dict.get(re.strip('${').strip('}')))
        # shell command think the $M is a value , we should shift it
        res = pattern_map_class.findall(value)
        for re in res:
            print 'map class: '+str(re)
            value = value.replace(re, '$\\'+re.strip('$'))
        mr_commond_str += ' -D '+str(name).strip()+'='+str(value).strip()
    if no_job_name:
        mr_commond_str += ' -D '+str('mapred.job.name')+'='+str(action.attrib.get("name"))
    print 'exe command:'+str(mr_commond_str)
    r = commands.getstatusoutput(mr_commond_str)
    print r
    if r[0] == 0:
        print '--------------------------------------------------------------------------------------'
        print 'the mr action exec success :'+str(action.attrib.get("name"))
        print '--------------------------------------------------------------------------------------'
    else:
        print '--------------------------------------------------------------------------------------'
        print 'the mr action exec fail :'+str(action.attrib.get("name"))
        print '--------------------------------------------------------------------------------------'
        raise Exception('action exe fail '+str(action.attrib.get("name")))
    print 'the action '+str(action.attrib.get("name"))+' is end!'
    if r[0] == 0:
         print action.attrib.get("name")+'exec success!'
    else:
        print action.attrib.get("name")+'exec failed!'
        error = action.find("error").get("to")
        return error
    ok = action.find("ok").attrib.get("to")
    return ok


def exec_sh(action, params_dict):
    print '--------------------------------------------------------------------------------------'
    print 'shell action '
    print '--------------------------------------------------------------------------------------'
    arg_list = action.find("arg-list")
    for arg in arg_list:
        shell_str = arg.text
        res = pattern_exp.findall(shell_str)
        for r in res:
            shell_str = shell_str.replace(r, params_dict.get(r.strip('${').strip('}')))
        print 'shell commond str : '+str(shell_str)
        r = commands.getstatusoutput(shell_str)
        print r
        if r[0] == 0:
            print '--------------------------------------------------------------------------------------'
            print 'sh success :'+str(shell_str)
            print '--------------------------------------------------------------------------------------'
        elif r[0] == 256:  # something like deleted file or dictory not exist
            print '--------------------------------------------------------------------------------------'
            print 'sh fail :'+str(shell_str)
            print '--------------------------------------------------------------------------------------'
        else:
            print '--------------------------------------------------------------------------------------'
            print 'sh fail :'+str(shell_str)
            print '--------------------------------------------------------------------------------------'
            raise Exception('shell exe faild')
    print 'exec all the shell end!'
    ok = action.find("ok").attrib.get("to")
    iter_action_name = ok
    return iter_action_name


# exec the action type of pig
def exec_pig(action, params_dict):
    print '--------------------------------------------------------------------------------------'
    print 'pig action '
    print '--------------------------------------------------------------------------------------'
    node_pig = action.find("java")
    pig_file = open(action.attrib.get("name")+'.pig','w')
    prepare = node_pig.find("prepare")
    if prepare is not None:
        for prepare_del in prepare:
            delete_path = prepare_del.attrib.get("path")
            res = pattern_exp.findall(delete_path)
            print params_dict
            for r in res:
                delete_path = delete_path.replace(r, params_dict.get(r.strip('${').strip('}')))
            print "delete path:"+delete_path
            commond_str = 'hadoop dfs -rm -r ' + str(delete_path)
            print commond_str
            r = commands.getstatusoutput(commond_str)
            print r
            print 'delete success '
    print node_pig

    arg_list = node_pig.find("arg-list")
    print node_pig.find("arg-list")
    for arg in arg_list:
        pig_str = arg.text
        print 'pig pattern exp :'+pig_str
        res = pattern_exp.findall(pig_str)
        for r in res:
            print 'the pattern exp :'+str(r)
            pig_str = pig_str.replace(r, params_dict.get(r.strip('${').strip('}')))
            print 'after the pattern exp:'+pig_str
        pig_file.write(pig_str+'\n')
    pig_file.close()
    print pig_file.name
    pig_commond_str = 'pig '+pig_file.name
    r = commands.getstatusoutput(pig_commond_str)
    print r
    if r[0] == 0:
        print '--------------------------------------------------------------------------------------'
        print 'the pig action exec success :'+str(action.attrib.get("name"))
        print '--------------------------------------------------------------------------------------'
    else:
        print '--------------------------------------------------------------------------------------'
        print 'the pig action exec fail :'+str(action.attrib.get("name"))
        print '--------------------------------------------------------------------------------------'
        raise Exception('action exe fail '+str(action.attrib.get("name")))
    ok = action.find("ok").attrib.get("to")
    return ok


# choose action operator to exe action
def exec_action(action, jar, main_class, params_dict):
    action_type = action.attrib.get("type")
    if action_type == "mr":
        print 'specific the exec operator : mapreduce.'
        return exec_mr(action, jar, main_class, params_dict)
    elif action_type == "pig":
        print 'specific the exec operator : pig.'
        return exec_pig(action, params_dict)
    elif action_type == "shell":
        print 'specific the exec operator : shell.'
        return exec_sh(action, params_dict)
    else:
        print 'Not specific any exec operator. now begin to recognize...'
        defal_exec_action(action, jar, main_class, params_dict)
    ok = action.find("ok").attrib.get("to")
    return ok


# 选择合适合适的operator执行器执行
def defal_exec_action(action, jar, main_class, params_dict):
    mr = action.find("map-reduce")
    if mr is not None:
        print 'recognize the action type as mapreduce action :'+str(action.attrib.get("name"))
        return exec_mr(action, jar, main_class, params_dict)
    if 'PigOperator' in str(action.find("java").find("class").text):
        print 'recognize the action type as pig action :'+str(action.attrib.get("name"))
        return exec_pig(action, params_dict)


# to parse and find the start action or end action, only care start and end.
def parse_start_end(argv):
    start_action = None
    end_action = None
    if argv is not None:
        for arg in argv:
            items = arg.strip().split("=")
            if items[0].strip() == 'start':
                start_action = items[1].strip()
            if items[0].strip() == 'end':
                end_action = items[1].strip()
    return start_action, end_action

```
mapred_rdc_metrics.xml
```
<workflow-app name="mapred_rdc_metrics">
	<params>
		<param key="metricsHistoryDay">${today}</param>
		<param key="metricsForecastDay">${metricsDay}</param>
		<param key="metricsScope">90</param>
		<param key="rootDir">/user/cmo_ipc/forecast</param>
		<param key="jarDir">autopo-job-1.0.jar</param>
	</params>
	<start to="Metrics" />

	<action name="Metrics">
		<map-reduce><prepare><delete path="${rootDir}/result/Metrics90/${metricsForecastDay}" /></prepare>
			<configuration>
				<property>
					<name>mapred.jar</name>
					<value>${jarDir}</value>
				</property>
				<property>
					<name>mapred.reduce.tasks</name>
					<value>300</value>
				</property>
				<property>
					<name>calcType</name>
					<value>0</value>
				</property>
				<property>
					<name>mapred.output.compress</name>
					<value>false</value>
				</property>
                <property>
                    <name>mapreduce.map.speculative</name>
                    <value>true</value>
                </property>
                <property>
                        <name>mapreduce.am.max-attempts</name>
                        <value>5</value>
                </property>
				<property>
					<name>metricsDays</name>
					<value>${metricsScope}</value>
				</property>
				<property>
					<name>mapreduce.map.class</name>
					<value>com.jd.ipc.forecasting.autopo.job.metrics.Metrics$M</value>
				</property>
				<property>
					<name>mapreduce.reduce.class</name>
					<value>com.jd.ipc.forecasting.autopo.job.metrics.Metrics$R</value>
				</property>
				<property>
					<name>mapred.input.dir</name>
					<value>${rootDir}/history/SKU/${metricsHistoryDay},/user/cmo_ipc/app.db/app_sfs_rdc_forecast_result/dt=${metricsForecastDay}</value>
				</property>
				<property>
					<name>mapred.output.dir</name>
					<value>${rootDir}/result/Metrics90/${metricsForecastDay}</value>
				</property>
			</configuration>
		</map-reduce>
		<ok to="renameForecastResult" />
		<error to="fail" />
	</action>

    <action name="renameForecastResult" type="shell">
        <arg-list>
            <arg>hadoop fs -mv ${rootDir}/result/Forecast/${metricsForecastDay} ${rootDir}/result/ForecastHistory/${metricsForecastDay}</arg>
        </arg-list>
        <ok to="end" />
        <error to="fail" />
    </action>

	<kill name="fail"></kill>
	<end name="end" />
</workflow-app>
```
main.py
```
#!/usr/bin/python
# coding=utf-8

__author__ = 'min'

import datetime
import workflow
import sys


if __name__ == '__main__':
    start_action = None
    end_action = None
    (start_action, end_action) = workflow.parse_start_end(sys.argv)
    params_dict_input = {}
    params_dict_input['${metricsDay}'] = str(datetime.date.today() + datetime.timedelta(-90))
    params_dict_input['${today}'] = str(datetime.date.today())
    jar = 'autopo-job-1.0.jar'
    main_class = 'com.jd.ipc.forecasting.autopo.job.AutoPoHadoopMain'
    workflow.exec_work_flow('mapred_rdc_metrics.xml', jar, main_class, start_action, end_action, params_dict_input)
```