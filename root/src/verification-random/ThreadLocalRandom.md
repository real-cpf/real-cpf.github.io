# ThreadLocalRandom


> 所以，current根据当前线程获得random实例
 ``` java
      /**
     * Returns the current thread's {@code ThreadLocalRandom}.
     *
     * @return the current thread's {@code ThreadLocalRandom}
     */
    public static ThreadLocalRandom current() {        
        if (U.getInt(Thread.currentThread(), PROBE) == 0)
            localInit();
        return instance;
    }
  ```

> 在初始化时 ，seed与唯一线程一一对应
> 即每一线程有自己的seed
> 如果取不到自己的seed，就会造成不同线程使用同一seed

```java
    /**
     * Initialize Thread fields for the current thread.  Called only
     * when Thread.threadLocalRandomProbe is zero, indicating that a
     * thread local seed value needs to be generated. Note that even
     * though the initialization is purely thread-local, we need to
     * rely on (static) atomic generators to initialize the values.
     */
    static final void localInit() {            
        int p = probeGenerator.addAndGet(PROBE_INCREMENT);
        int probe = (p == 0) ? 1 : p; // skip 0
        long seed = mix64(seeder.getAndAdd(SEEDER_INCREMENT));
        Thread t = Thread.currentThread();
        U.putLong(t, SEED, seed);
        U.putInt(t, PROBE, probe);
    }
```

`最后 ，不同线程使用统同一算法、同一seed便会出现相同的随机数 `