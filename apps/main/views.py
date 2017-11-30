from flask import Blueprint,render_template,Response,url_for,redirect,session,request,flash,jsonify,stream_with_context,json
from apps import app,db

from apps.models import WBalance
from apps.models import scada
from apps.models.scada import *
from sqlalchemy import func
from . import main

scada_classes_all = dict([(name, cls) for name, cls in scada.__dict__.items() if isinstance(cls, type)])

def return_feature_collection2(cur):
    """
    Execute a JSON-returning SQL and return HTTP response
    :type sql: SQL statement that returns a a GeoJSON Feature
    """
    

    def generate():
        yield '{ "result": { "type": "FeatureCollection", "features": ['
        for idx, row in enumerate(cur):
            if idx > 0:
                yield ','
            yield row[0] #json.dumps(row[0])
        yield ']}}'
        
    return Response(stream_with_context(generate()), mimetype='application/json')

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
            yield '{ "type":"Feature","geometry":'
            yield row[0] #json.dumps(row[0])
            yield '}'
        yield ']}}'
        
    return Response(stream_with_context(generate()), mimetype='application/json')

def get_table_by_name(tablename):
    cls = None
    rets = "no such gist table %s "% tablename
    for k,v in scada_classes_all.items():
        try:
            if v.__tablename__ == tablename:
                cls = v
        except:
            continue
    
    return cls
    
@main.route('/')
def index():
    
    return render_template('index.html')
    
@main.route('/openlayer/')
def openlayer():
    
    return render_template('index_test.html')
    
@main.route('/dlzxc/')
def dlzxc():
    dlzxc = db.session.query(GCloudlayerMetaDlzxc.geomjson).all()
    #return dlzxc[0]
    #return jsonify(dlzxc)
    return return_feature_collection(dlzxc)
    
    

@main.route('/geom/<tablename>/')
def get_geomjson_by_tblname(tablename):
    
    
    cls = None
    rets = "no such gist table %s "% tablename
    for k,v in scada_classes_all.items():
        try:
            if v.__tablename__ == tablename:
                cls = v
        except:
            continue
    if cls is None:
        return rets
    _geojson = db.session.query(cls.geomjson).all()
    #return dlzxc[0]
    #return jsonify(dlzxc)
    return return_feature_collection(_geojson)
    
@main.route('/bounds/<tablename>/')
def get_bounds_geom_by_tblname(tablename):
    
    cls = None
    rets = "no such gist table %s "% tablename
    for k,v in scada_classes_all.items():
        try:
            if v.__tablename__ == tablename:
                cls = v
        except:
            continue
    if cls is None:
        return rets
    _boundsjson = db.session.query(func.ST_AsGeoJSON(cls.bounds_geom)).all()
    #return dlzxc[0]
    #return jsonify(dlzxc)
    return return_feature_collection(_boundsjson)
    
@main.route('/load_dlzxc/')
def load_dlzxc():
    
    return render_template('index_gjson.html')
    
@main.route('/getGeom',methods=['GET','POST'])
def getGeom():
    left = request.args.get('left')
    top = request.args.get('top')
    right = request.args.get('right')
    bottom = request.args.get('bottom')
    layerName = request.args.get('layerName') or ''
    
    tablename = 'g_cloudlayer_meta_'+layerName
    cls = get_table_by_name(tablename)
    
    if cls is None:
        return 'no invalid data'
        
    #tBoundsText = "ST_GeomFromText('POLYGON( ( %d %d ,%d %d ,%d %d ,%d %d ,%d %d ) )')"%(left,top,right,top,right,bottom,left,bottom,left,top) POLYGON( ( 118.27640380859377 29.806093648481777 ,118.52359619140627 29.806093648481777 ,118.52359619140627 29.913877250518823 ,118.27640380859377 29.913877250518823 ,118.27640380859377 29.806093648481777 ) )
    tBoundsText = 'POLYGON( ( %s %s ,%s %s ,%s %s ,%s %s ,%s %s ) )'%(left,top,right,top,right,bottom,left,bottom,left,top)
    
    tmptext = func.ST_GeomFromText(tBoundsText,0)
    
    
    
    geodata = db.session.query(func.ST_AsGeoJSON(cls.geomdata)).filter(cls.geomdata.ST_Intersects(tmptext)).all()
    #return dlzxc[0]
    #return jsonify(dlzxc)
    return return_feature_collection(geodata)
    
    
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
