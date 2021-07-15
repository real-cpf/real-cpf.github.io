## 安全策略



#### 隐藏版本号

`server_tokens off;`

#### SSL证书

```nginx
server {
    listen       443 ssl; # 1.5之前的版本要单独加  ssl on;  
    server_name  domain;
	ssl_certificate     cert/xxx.pem;   
	ssl_certificate_key  cert/xxx.key;    
    ssl_session_cache    shared:SSL:1m;
    ssl_session_timeout  5m;        # session
    # 指定算法
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
   # I mentioned how you negotiate which cipher you choose; you can prefer the client’s choice or the server’s choice. it’s always better to prefer the server’s choice. So there’s a directive here:  – always turn this on. ssl_prefer_server_ciphers
    ssl_prefer_server_ciphers  on;
    
}
```

#### 禁止不安全的请求

```nginx
if($request_method !~ ^(GET|POST)$){
    return 405;
}
```



#### 访问白名单

```nginx
location / {
    allow 127.0.0.1;
    deny all;
}
```

