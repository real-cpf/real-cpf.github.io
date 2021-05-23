# mybatis


```java

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.springframework.stereotype.Component;


@Component
@Mapper
public interface DemoTableMapper {
	@Insert("insert into demotable(col1,col2,col3) values(#{col1},#{col2},#{col3})")
	int add(DemoTable student);
	
	@Update("update demotable set col1=#{col1},col2=#{col2} where col3=#{col3}")
    int update(DemoTable student);
	
	@Delete("delete from demotable where col3=#{col3}")
    int deleteBycol3(String sno);
	
	@Select("select * from demotable where col3=#{col3}")   // #{col3} means  select * from demotable where col3=?;
	@Results(id = "demotable",value= {                          // if use '${name}' means select * from demotable where col3 = 'name'
		 @Result(property = "col3", column = "col3", javaType = String.class),
         @Result(property = "col2", column = "col2", javaType = String.class),
         @Result(property = "col1", column = "col1", javaType = String.class)
	})
    Student queryDemoTableBycol3(String col3); // @Param("col3") String col3

	@Select("select * from demotable ")                          //  <resultMap id="allDemoTable" type="xxx.xxx.entity.DemoTable" >
	@Results(value= {                                            // <id column="id" property="id" jdbcType="BIGINT" />    
		 @Result(property = "col3", column = "col3", javaType = String.class),//        <result column="col3" property="col3" jdbcType="VARCHAR" />
         @Result(property = "col2", column = "col2", javaType = String.class),     //   <result column="col2" property="col2" jdbcType="VARCHAR" />
         @Result(property = "col1", column = "col1", javaType = String.class)    //    <result column="col1" property="col1" javaType="com.neo.enums.UserSexEnum"/>
	})                                                                            //  </resultMap>
	List<DemoTable> allDemoTable();
}

```

maven

```xml
		<dependency>
		    <groupId>org.mybatis.spring.boot</groupId>
		    <artifactId>mybatis-spring-boot-starter</artifactId>
		    <version>1.3.1</version>
		</dependency>
```