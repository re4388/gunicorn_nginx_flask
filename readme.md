## Note
1. 如何使用Nginx, Gunicorn與Supervisor 部署一個Flask App
https://peterli.website/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8nginx-gunicorn%E8%88%87supervisor-%E9%83%A8%E7%BD%B2%E4%B8%80%E5%80%8Bflask-app/


### run
Instead of flask default WSGI, we run use Gunicron as WSGI server for Python flask
`gunicorn --bind=127.0.0.1:5001 wsgi:app`


### on Nginx
1. edit this file in your linux or vps or cloud vm..etc -> /etc/nginx/sites-available/default
2. change here:
   
    ```
    location / {
            proxy_pass http://127.0.0.1:5001;
            
            }
    ```


### Reference
1. https://www.cyberciti.biz/faq/nginx-linux-restart/
2. https://www.cyberciti.biz/faq/nginx-restart-ubuntu-linux-command/
3. https://www.cnblogs.com/ray-liang/p/4837850.html
4. https://nginx.org/
5. https://gunicorn.org/#quickstart
6. https://peterli.website/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8nginx-gunicorn%E8%88%87supervisor-%E9%83%A8%E7%BD%B2%E4%B8%80%E5%80%8Bflask-app/
7. https://dotblogs.com.tw/grayyin/2017/05/18/183117