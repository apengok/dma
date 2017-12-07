# -*- coding: utf-8 -*-

from flask import Blueprint,render_template,Response,url_for,redirect,session,request,flash,jsonify,stream_with_context,json
from apps import app,db

from apps.models import WBalance
from apps.models import scada
from apps.models.scada import *
from sqlalchemy import func
from . import main
from dma import dma_tree,dma_file,summary_file


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
    
def dma_tojson():
    
    def genereate():
        yield '['
        
        yield ']'
    
@main.route('/dma/')
def dma():
    
    

    return render_template('main/dma.html',json_data=dma_tree,dma_content=dma_file)

@main.route('/dma_summary/')
def dma_summary():
       
    #summary_content = [suma.decode('utf-8') for suma in tmp]
    return render_template('/main/dma_summary.html',json_data=dma_tree,summary_content=summary_file)