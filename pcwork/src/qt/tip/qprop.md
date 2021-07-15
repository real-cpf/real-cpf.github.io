## Qprop


```tex
 READ fun：定义了读取属性的接口fun，fun必须返回属性的类型或者属性同类型引用；fun不能带参数。
 WRITE fun：定义了设置属相的接口fun，fun没有返回值，必须带有一个参数，传值或者传引用，参数类型与属相类型相同。
 MEMBER var：MEMBER指明了成员变量var即可读也可写的，相当于同时使用了READ和WRITE关键字。不定义READ，那么必须定义MEMBER；定义了MEMBER，仍可以使用READ或者WRITE控制访问接口。
```

​	

