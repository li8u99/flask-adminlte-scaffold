from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from . import main
from app import models



def query():
        db = models.db
        cursor = db.cursor()
        sql = "SELECT * FROM ip_mac"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data[0][1])
        db.close()
        return data


# 办公设备资产管理
@main.route('/itarea', methods=['GET'])
@login_required
def itarea():
    data = query()
    return render_template('itarea.html', data=data)