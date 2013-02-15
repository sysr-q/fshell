#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from flask import Flask, render_template, request
import pysqlw

import settings

app = Flask(__name__)

app.debug = True

@app.route(settings.url, methods=["GET", "POST"])
def shell():
    ua = request.user_agent
    data = {
        "method": request.method,
        "ip": request.remote_addr,
        "time": int(time.time()),

        "agent": "" if not ua.string else ua.string,
        "agent_platform": "" if not ua.platform else ua.platform,
        "agent_browser": "" if not ua.browser else ua.browser,
        "agent_version": "" if not ua.version else ua.version,
        "agent_language": "" if not ua.language else ua.language
    }
    if not pysql().insert('fshell', data):
        print 'Unable to insert data to fshell database.'
    title = settings.template if settings.show_title else ""
    return render_template("{0}.html".format(settings.template), title=title, **settings.template_vars)

def main():
    check_sql()
    app.run(host=settings.host, port=settings.port)

def pysql():
    return pysqlw.pysqlw(db_type="sqlite", db_path=settings.database)

def check_sql():
    import os
    if os.path.isfile(settings.database):
        return
    with pysql() as p:
        p.wrapper \
        .cursor \
        .executescript(settings.schema)

if __name__ == "__main__":
    main()
