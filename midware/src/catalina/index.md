# catalina

> [apache/catalina](http://tomcat.apache.org/tomcat-7.0-doc/api/org/apache/catalina/startup/Catalina.html)

```text
Startup/Shutdown shell program for Catalina. The following command line options are recognized:

    -config {pathname} - Set the pathname of the configuration file to be processed. If a relative path is specified, it will be interpreted as relative to the directory pathname specified by the "catalina.base" system property. [conf/server.xml]
    -help - Display usage information.
    -nonaming - Disable naming support.
    configtest - Try to test the config
    start - Start an instance of Catalina.
    stop - Stop the currently running instance of Catalina.

Should do the same thing as Embedded, but using a server.xml file.
```

![startup](https://cdn.jsdelivr.net/gh/ChenPufeng/picgo@master/img/tomcat-index.png)