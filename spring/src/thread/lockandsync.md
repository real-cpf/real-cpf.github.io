## lock & sync

+ 简单加锁 synchronized `对象锁`

+ wait(),notify(),notifyAll()通信

+ volatile 信号量

+ PipedWriter`、 `PipedReader`、 `PipedOutputStream`、 `PipedInputStream

  ```java
  
  import java.io.IOException;
  import java.io.PipedReader;
  import java.io.PipedWriter;
  
  public class PipeDemo {
  	static class ReadThread implements Runnable{
  		private PipedReader reader;
  		public ReadThread(PipedReader reader ) {
  			this.reader=reader;
  		}
  		@Override
  		public void run() {
  			// TODO Auto-generated method stub
  			System.out.println("this is reader");
  			int receive=0;
  			try {
  				while ((receive=reader.read())!=-1) {
  					System.out.println((char)receive);
  				}
  			} catch (IOException e) {
  				// TODO: handle exception
  				e.printStackTrace();
  			}
  		}
  	}
  	
  	static class WriterThread implements Runnable{
  		private PipedWriter writer;
  		public WriterThread(PipedWriter writer) {
  			// TODO Auto-generated constructor stub
  			this.writer=writer;
  		}
  		@Override
  		public void run() {
  			// TODO Auto-generated method stub
  			System.out.println("this is writer");
  			int send=0;
  			
  			try {
  				writer.write("test");
  			} catch (IOException e) {
  				// TODO: handle exception
  				e.printStackTrace();
  			}finally {
  				try {
  					writer.close();
  				} catch (IOException e2) {
  					// TODO: handle exception
  					e2.printStackTrace();
  				}
  			}
  		}
  	}
  	
  	public static void main(String[] args) throws IOException, InterruptedException {
  		PipedWriter writer=new PipedWriter();
  		PipedReader reader=new PipedReader();
  		writer.connect(reader);
  		new Thread(new ReadThread(reader)).start();
  		Thread.sleep(1000);
  		new Thread(new WriterThread(writer)).start();
  		
  		
  	}
  }
  ```

  

+ join() `可以使得主线程获得子线程后的某个数据`

+ sleep() 

  > - wait可以指定时间，也可以不指定；而sleep必须指定时间。
  > - wait释放cpu资源，同时释放锁；sleep释放cpu资源，但是不释放锁，所以易死锁。
  > - wait必须放在同步块或同步方法中，而sleep可以再任意位置

+ ThreadLocal 本地线程副本

  > 如果开发者希望将类的某个静态变量（user ID或者transaction ID）与线程状态关联，则可以考虑使用ThreadLocal。
  >
  > 最常见的ThreadLocal使用场景为用来解决数据库连接、Session管理等。数据库连接和Session管理涉及多个复杂对象的初始化和关闭。如果在每个线程中声明一些私有变量来进行操作，那这个线程就变得不那么“轻量”了，需要频繁的创建和关闭连接。