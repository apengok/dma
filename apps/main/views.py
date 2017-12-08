# -*- coding: utf-8 -*-

from flask import Blueprint,render_template,Response,url_for,redirect,session,request,flash,jsonify,stream_with_context,json
from apps import app,db

from apps.models import WBalance
from apps.models import scada
from apps.models.scada import *
from sqlalchemy import func
from . import main
from dma import dma_tree,dma_file,summary_file,static_monthly


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
    
    
    return render_template('main/wstasitc.html',balance=balance[0],month_group=month_group,current_mon=month_group[0],static_monthly=static_monthly)
    
@main.route('/economize/')
def economize():

    return render_template('main/economize.html')
    
    
@main.route('/dma/')
def dma():
    
    
    dma_file['name']['value'] = dma_tree[0]['text'].decode('utf-8')
    return render_template('main/dma.html',json_data=dma_tree,dma_content=dma_file)
    
#@main.route('/sub_dma/<dma_name>')
#@main.route('/sub_dma/<dma_name>/<sub_name>')
@main.route('/<path:fullurl>')
def sub_dma(fullurl):
    try:
        namelist = fullurl.split('/')
        if len(namelist) == 2:
            dma_name = namelist[1]
            dma_file.get('name')['value']=dma_name
        if len(namelist) == 3:
            dma_name = namelist[1]
            sub_name = namelist[2]
            dma_file.get('name')['value']=sub_name
        else:
            dma_file.get('name')['value']=namelist[-1]
        flash("you selected:%s"%(fullurl,))
    except :
        namelist = fullurl.split('/')
        flash("you selected:%s-%s"%(fullurl,' '.join(namelist)))
        flash("invalid dma name")
    #dma_file['name']['value'] = dma_name
    return render_template('main/dma.html',json_data=dma_tree,dma_content=dma_file)

@main.route('/dma_summary/')
def dma_summary():
       
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render_template('/main/dma_summary.html',json_data=dma_tree,summary_content=summary_file)