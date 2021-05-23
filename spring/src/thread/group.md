## group

+ 线程可以设置优先级 作为建议 `getPriority()` 
+ 线程优先级不会大于线程组的优先级
+ Copies into the specified array every active thread in this thread group and its subgroups.
  	An invocation of this method behaves in exactly the same way as the invocation
  		`group.enumerate(threads);`



+ 线程组异常处理 

  ```java
  		ThreadGroup gThreadGroup=new ThreadGroup("group1") {
  			public void uncaughtException(Thread t, Throwable e) {
  				System.out.println(t.getName()+":"+e.getMessage());
  			};
  		};
  ```

  