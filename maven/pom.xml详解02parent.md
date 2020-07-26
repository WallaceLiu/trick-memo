```
<!--父项目的坐标。如果项目中没有规定某个元素的值，那么父项目中的对应值即为项目的默认值。 坐标包括group ID，artifact ID和 version。-->
<parent> 
  <!--被继承的父项目的构件标识符-->  
  <artifactId/>  
  <!--被继承的父项目的全球唯一标识符-->  
  <groupId/>  
  <!--被继承的父项目的版本-->  
  <version/>  
  <!-- 父项目的pom.xml文件的相对路径。相对路径允许你选择一个不同的路径。默认值是../pom.xml。Maven首先在构建当前项目的地方寻找父项 目的pom，其次在文件系统的这个位置（relativePath位置），然后在本地仓库，最后在远程仓库寻找父项目的pom。-->  
  <relativePath/> 
</parent>
```