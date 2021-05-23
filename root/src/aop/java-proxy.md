# java-proxy


<div style="display:none">java-tag-amF2YS10YWc=</div>

+ JDK-Proxy
> 必须先定义接口
```java
 @CallerSensitive
    public static Object newProxyInstance(ClassLoader loader, //目标类的loader
                                          Class<?>[] interfaces,                      //接口类数组
                                          InvocationHandler h){                       //执行代理方法
                                          //more
                                          }
    //在 InvocationHandler 里 可以在自定义切面方法
    // like  :before  after 

```


+  Cglib-Proxy
> 无需接口，通过asm直接加载字节码生成子类
```java
	    Enhancer enhancer = new Enhancer();
		enhancer.setSuperclass(target.getClass());
		enhancer.setCallback(
		                //  impl MethodInterceptor
		                        );
	    enhancer.create();
```

> 上面的cglib实现用到了`import net.sf.cglib.proxy.MethodInterceptor;import net.sf.cglib.proxy.MethodProxy;`
> 如果在spring环境下也可以 用 `import org.springframework.cglib.proxy.MethodInterceptor;import org.springframework.cglib.proxy.MethodProxy;`