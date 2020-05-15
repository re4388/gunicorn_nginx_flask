### note
1. 如何使用Nginx, Gunicorn與Supervisor 部署一個Flask App
https://peterli.website/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8nginx-gunicorn%E8%88%87supervisor-%E9%83%A8%E7%BD%B2%E4%B8%80%E5%80%8Bflask-app/


## run
Instead of flask default WSGI, we run use Gunicron as WSGI server for Python flask
`gunicorn --bind=127.0.0.1:5001 wsgi:app`
