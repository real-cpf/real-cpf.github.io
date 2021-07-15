# java-security


[java-standard-加密算法](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html)

```java
     Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
	 cipher.init(Cipher.ENCRYPT_MODE, secretKey, params);
	 cipher.doFinal(base64content)
```


### SM2
```java
SM2Engine engine = new SM2Engine(digest, mode);
                    engine.processBlock(data, 0, length); 

```