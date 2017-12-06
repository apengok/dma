# -*- coding: utf-8 -*-

from flask import Blueprint,render_template,Response,url_for,redirect,session,request,flash,jsonify,stream_with_context,json
from apps import app,db

from apps.models import WBalance
from apps.models import scada
from apps.models.scada import *
from sqlalchemy import func
from . import main



@main.route('/')
@main.route('/wbalance/')
def wbalance():
    balance = WBalance.query.order_by(WBalance.name).all()
    month_group = [ba.name for ba in balance ]
    return render_template('main/wbalance.html',balance=balance[0],month_group=month_group,current_mon=month_group[0])
    
@main.route('/wbalance/<mon>')
def wbalance_mon(mon):
    balance = WBalance.query.order_by(WBalance.name).all()
    month_group = [ba.name for ba in balance ]
    balance1 = WBalance.query.filter_by(name=mon).first()
    return render_template('main/wbalance.html',balance=balance1,month_group=month_group,current_mon=mon)

    
@main.route('/wstasitc/')
def wstasitc():
    balance = WBalance.query.order_by(WBalance.name).all()
    month_group = [ba.name for ba in balance ]
    return render_template('main/wstasitc.html',balance=balance[0],month_group=month_group,current_mon=month_group[0])
    
@main.route('/economize/')
def economize():

    return render_template('main/economize.html')
    
@main.route('/dma/')
def dma():

    return render_template('main/dma.html')

@main.route('/dma_summary/')
def dma_summary():
       
    summary_content = ['年供水总量（万 m3）','年注册用户用水量（万 m3）','明漏水量（万 m3）','暗漏水量（万 m3）','背景漏失水量（万 m3）','水箱、水池的渗漏和溢流水量 （万 m3）','居民用户总分表差损失水量（万 m3）','非居民用户表具误差损失水量（万m3）','抄表到户居民用户用水量（万 m3）','年平均出厂压力（ MPa）','最大冻土深度（ m）','管网长度（ km）','管网分区计量级别数','一级分区数量（个）','一级分区覆盖水量（万 m3）','一级分区覆盖管网长度（ km）' ,'二级分区数量（个）','二级分区覆盖水量（万 m3）','二级分区覆盖管网长度（ km）' ,'N 级分区数量（个）','N 级分区覆盖水量（万 m3）','N 级分区覆盖管网长度（ km）','管网压力合格率','管网水质合格率','用户服务综合满意率','管网漏损率','水表抄见率（ %）','抄表准确率（ %）','在线压力点数量（个）','在线流量计数量（个）','在线水质监测点数量（个）','收费用远传水表数量（只）','收费用远传水表水量占销售水量比（ %）','探出漏点总数（个）','漏失水量(万 m3)','漏损率（ %）','压力合格率（ %）','水质合格率（ %）','压力（ MPa）','经济投入','经济效益','社会效益']
    
        
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render_template('/main/dma_summary.html',summary_content=enumerate(summary_content))