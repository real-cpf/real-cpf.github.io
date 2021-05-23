# config



```java


import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

/*
src/main/resources/test.properties 


test.name=KangKang
test.age=25
test.vvv=vvv

then 
@EnableConfigurationProperties(TestConfigBean.class)
with start Application
@Autowired
with the config bean like  `TestConfigBean`

*/


@Configuration
@ConfigurationProperties(prefix="test")
@PropertySource("classpath:test.properties") // ->  src/main/resources/test.properties 
@Component
public class TestConfigBean {
	@Value("${test.vvv}")
   private String vvv;


	private String name;

	private String name;
	private int age;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	
}

```