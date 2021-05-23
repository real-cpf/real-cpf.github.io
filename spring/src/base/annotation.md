## Annotation

```java
public @interface TestOneAnnotion{
    
}
// then ,we can use on my objs
@TestOneAnnotion
public class App{
    @TestOneAnnotion
    public static void main(String[] args){
        
    }
}
```



+ 元注解
  + @Retention  `means retention on compile 、class loading、jvm runtime`  ```enum RetentionPolicy```
  + @Target `scope` ```ElementType```
  + @Documented `java doc`
  + @Inherited `如果被Inherited 修饰的父类的子类没有被其他注解修饰，则继承本注解`
  + @Repeatable `can repeat`
+ 注解的属性
  + 类型 ： 基本数据类型、string、class、enum 、 注解、前面的一维数组
  + 注解属性获取 `getAnnotation`