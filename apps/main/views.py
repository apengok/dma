from flask import Blueprint,render_template,Response,url_for,redirect,session,request,flash,jsonify,stream_with_context,json
from apps import app,db

from apps.models import WBalance
from apps.models.scada import *
from . import main


def return_feature_collection(cur):
    """
    Execute a JSON-returning SQL and return HTTP response
    :type sql: SQL statement that returns a a GeoJSON Feature
    """
    

    def generate():
        yield '{ "result": { "type": "FeatureCollection", "features": ['
        for idx, row in enumerate(cur):
            if idx > 0:
                yield ','
            yield json.dumps(row[0])
        yield ']}}'
        
    return Response(stream_with_context(generate()), mimetype='application/json')

@main.route('/')
def index():
    
    return render_template('index_xyz.html')
    
@main.route('/openlayer/')
def openlayer():
    
    return render_template('index_test.html')
    
@main.route('/dlzxc/')
def dlzxc():
    dlzxc = db.session.query(GCloudlayerMetaDlzxc.bounds_geom.ST_AsGeoJSON()).all()
    return jsonify(result=dlzxc[0][0])
    #return return_feature_collection(dlzxc)
    
    
@main.route('/load_dlzxc/')
def load_dlzxc():
    
    return render_template('index_gjson.html')
    
@main.route('/wbalance')
def wbalance():
    return render_template('main/wbalance.html')

@main.route('/wstasitc')
def wstasitc():
    return 'adsfds'

@main.route('/wdma')
def wdma():
    balance = WBalance.query.order_by(WBalance.name).all()
    month_group = [ba.name for ba in balance ]
    return render_template('main/dma.html',balance=balance[0],month_group=month_group,current_mon=month_group[0])
    
@main.route('/wdma/<mon>')
def wdma_mon(mon):
    balance = WBalance.query.order_by(WBalance.name).all()
    month_group = [ba.name for ba in balance ]
    balance1 = WBalance.query.filter_by(name=mon).first()
    return render_template('main/dma.html',balance=balance1,month_group=month_group,current_mon=mon)
