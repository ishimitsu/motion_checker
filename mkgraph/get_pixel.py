#!/usr/bin/python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import MySQLdb
import datetime

def pixel_chart(environ, start_response):
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tpl = env.get_template('template.html')

    #テンプレートへ挿入するデータの作成
    title = u"Pixel Chart"

    pixel_list = []

    connector = MySQLdb.connect(host="localhost", db="motion_db", user="www_data", passwd="hogehoge", charset="utf8")    
    cursor = connector.cursor()
    sql = "select changed_pixels,time_stamp from sleep_check"

    cursor.execute(sql)
    records = cursor.fetchall()
    for record in records:
        pixel_list.append({'date':record[1].strftime("%Y-%m-%d %H:%M:%S"), 'pixel':record[0]})
        
    cursor.close()
    connector.close()

    #テンプレートへ挿入するデータの作成
    title = u"Pixel Chart"
        
    #テンプレートへの挿入
    html = tpl.render({'title':title, 'pixel_list':pixel_list})

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf-8')]
    
if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(pixel_chart).run()
