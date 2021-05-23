# mongodb

> mongodb



```groovy
	// https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-data-mongodb
	compile group: 'org.springframework.boot', name: 'spring-boot-starter-data-mongodb', version: '2.4.0'
```





```java
public interface CustomerRepository  extends MongoRepository<Customer,String>{}
```

