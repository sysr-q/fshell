#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, abort, request, g
from flask import redirect, url_for, flash, make_response, jsonify, send_file

import pysqlw

import time

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

        "agent": ua.string if not ua.string == None else "",
        "agent_platform": ua.platform if not ua.platform == None else "",
        "agent_browser": ua.browser if not ua.browser == None else "",
        "agent_version": ua.version if not ua.version == None else "",
        "agent_language": ua.language if not ua.language == None else ""
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
    with open('schema.sql', 'rb') as f:
        pysql()._wrap.cursor.executescript(f.read())

if __name__ == "__main__":
    main()
