#!/bin/bash -e

ps -ef |grep gunicorn |awk '{print $2}'|xargs kill -9
sleep 1

exec venv/bin/gunicorn -c cmd/gunicorn.conf "app:create_app()" --access-logformat '%(t)s %(h)s %(l)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s' -t 60
