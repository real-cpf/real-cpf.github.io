## run & start

+ extend Thread & implements Runable

  ```java
  public class TDemo1 {
  	public static class MyThread extends Thread {
  		@Override
  		public void run() {
  			System.out.println("mythread");
  			System.out.println(Thread.currentThread().getId());
  			
  		}
  		
  	}
  	
  	public static class MyThread1 implements Runnable{
  		@Override
  		public void run() {
  			System.out.println("mythread1111");
  			System.out.println(Thread.currentThread().getId());
  			
  		}
  	}
  	 public static void main(String[] args) {
  		new MyThread().start();
  		new Thread(new MyThread1()).start();
  		new Thread(()->{
  			System.out.println("inline");
  			System.out.println(Thread.currentThread().getId());
  		}).start();
  	}
  
  }
  
  ```

  ```java
  /**
       * Initializes a Thread.
       *
       * @param g the Thread group
       * @param target the object whose run() method gets called
       * @param name the name of the new Thread
       * @param stackSize the desired stack size for the new thread, or
       *        zero to indicate that this parameter is to be ignored.
       * @param acc the AccessControlContext to inherit, or
       *            AccessController.getContext() if null
       * @param inheritThreadLocals if {@code true}, inherit initial values for
       *            inheritable thread-locals from the constructing thread
       */
      private Thread(ThreadGroup g, Runnable target, String name,
                     long stackSize, AccessControlContext acc,
                     boolean inheritThreadLocals) {
          if (name == null) {
              throw new NullPointerException("name cannot be null");
          }
  
          this.name = name;
  
          Thread parent = currentThread();
          SecurityManager security = System.getSecurityManager();
          if (g == null) {
              /* Determine if it's an applet or not */
  
              /* If there is a security manager, ask the security manager
                 what to do. */
              if (security != null) {
                  g = security.getThreadGroup();
              }
  
              /* If the security manager doesn't have a strong opinion
                 on the matter, use the parent thread group. */
              if (g == null) {
                  g = parent.getThreadGroup();
              }
          }
  
          /* checkAccess regardless of whether or not threadgroup is
             explicitly passed in. */
          g.checkAccess();
  
          /*
           * Do we have the required permissions?
           */
          if (security != null) {
              if (isCCLOverridden(getClass())) {
                  security.checkPermission(
                          SecurityConstants.SUBCLASS_IMPLEMENTATION_PERMISSION);
              }
          }
  
          g.addUnstarted();
  
          this.group = g;
          this.daemon = parent.isDaemon();
          this.priority = parent.getPriority();
          if (security == null || isCCLOverridden(parent.getClass()))
              this.contextClassLoader = parent.getContextClassLoader();
          else
              this.contextClassLoader = parent.contextClassLoader;
          this.inheritedAccessControlContext =
                  acc != null ? acc : AccessController.getContext();
          this.target = target;
          setPriority(priority);
          if (inheritThreadLocals && parent.inheritableThreadLocals != null)
              this.inheritableThreadLocals =
                  ThreadLocal.createInheritedMap(parent.inheritableThreadLocals);
          /* Stash the specified stack size in case the VM cares */
          this.stackSize = stackSize;
  
          /* Set thread ID */
          this.tid = nextThreadID();
      }
  ```

  + thead 的常用方法

  ```java
  
  
      currentThread() //静态方法，返回对当前正在执行的线程对象的引用；
      start()//开始执行线程的方法，java虚拟机会调用线程内的run()方法；
      yield()//yield在英语里有放弃的意思，同样，这里的yield()指的是当前线程愿意让出对当前处理器的占用。这里需要注意的是，就算当前线程调用了yield()方法，程序在调度的时候，也还有可能继续运行这个线程的；
      sleep()//静态方法，使当前线程睡眠一段时间；
      join()//使当前线程等待另一个线程执行完毕之后再继续执行，内部调用的是Object类的wait方法实现的；
  
  ```

  

+ Callable & Future

  ```java
  import java.util.concurrent.Callable;
  import java.util.concurrent.ExecutionException;
  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.concurrent.Future;
  
  
  public class Task1 implements Callable<Integer>{ 
  	@Override
  	public Integer call() throws Exception {
  		Thread.sleep(1000);
  		return 2;
  	}
  	public static void main(String[] args) throws InterruptedException, ExecutionException {
  		ExecutorService executorService=Executors.newCachedThreadPool();
  		Task1 task1=new Task1();
  		Future<Integer> result = executorService.submit(task1);
  		System.out.println(result.get());
  	}
  }
  
  ```

+ FutureTask

  ```java
  import java.util.concurrent.Callable;
  import java.util.concurrent.ExecutionException;
  import java.util.concurrent.ExecutorService;
  import java.util.concurrent.Executors;
  import java.util.concurrent.FutureTask;
  
  public class Task2 implements Callable<Integer> {
  	@Override
  	public Integer call() throws Exception {
  		Thread.sleep(1000);
  		return 2;
  	}
  	
  	public static void main(String[] args) throws InterruptedException, ExecutionException {
  		ExecutorService executorService=Executors.newCachedThreadPool();
  		FutureTask<Integer> futureTask=new FutureTask<Integer>(new Task2());
  		executorService.submit(futureTask);
  		System.out.println(futureTask.get());
  	}
  }
  
  ```

  