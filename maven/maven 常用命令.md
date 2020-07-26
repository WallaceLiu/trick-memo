# 常用命令
- 创建Maven的普通java项目： 
```
mvn archetype:create 
   -DgroupId=packageName 
   -DartifactId=projectName  
```
- 创建Maven的Web项目：   
```
mvn archetype:create 
    -DgroupId=packageName    
    -DartifactId=webappName 
    -DarchetypeArtifactId=maven-archetype-webapp    
```
- 编译源代码
```
mvn compile 
```
- 编译测试代码
```
mvn test-compile    
```
- 运行测试
```
mvn test   
```
- 产生site
```
mvn site
```
- 打包
```
mvn package
```
- 在本地Repository中安装jar
```
mvn install 
```
- 清除产生的项目
```
mvn clean
```
- 生成eclipse项目
```
mvn eclipse:eclipse  
```
- 生成idea项目
```
mvn idea:idea  
```
- 组合使用goal命令，如只打包不测试
```
mvn -Dtest package   
```
- 编译测试的内容
```
mvn test-compile  
```
- 只打jar包
```
mvn jar:jar  
```
- 只测试而不编译，也不测试编译
```
mvn test -skipping compile -skipping test-compile 
```
skipping 的灵活运用，当然也可以用于其他组合命令)。 
- 清除eclipse的一些系统设置
```
mvn eclipse:clean
```
- 查看实际pom信息
```
mvn help:effective-pom
```
- 分析项目的依赖信息
```
mvn dependency:analyze 或 mvn dependency:tree
```
- 查看冲突
```
mvn project-info-reports:dependencies
```