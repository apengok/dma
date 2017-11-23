# coding: utf-8
from sqlalchemy import Column, Float, Integer, LargeBinary, SmallInteger, String, Table, Text
from geoalchemy2.types import Geometry
from apps import db



class AlarmShareDayTax(db.Model):
    __tablename__ = 'alarm_share_day_tax'

    pid = Column(Integer, primary_key=True)
    readtime = Column(String(20), nullable=False)
    simid = Column(String(20), nullable=False)
    flux = Column(Float(53))
    totalflux = Column(Float(53))
    pressure = Column(Float(53))
    warning = Column(String(50), nullable=False)
    warningdesc = Column(String(20), nullable=False)


class Amrsparam(db.Model):
    __tablename__ = 'amrsparam'

    paramkey = Column(String(64), primary_key=True)
    paramvalue = Column(String(64), nullable=False)


class DmDeviceType(db.Model):
    __tablename__ = 'dm_device_type'

    typename = Column(String(100), primary_key=True)
    tablename = Column(String(100), nullable=False, unique=True)


class DmEnumConfig(db.Model):
    __tablename__ = 'dm_enum_config'

    tablename = Column(String(100), primary_key=True, nullable=False)
    fieldname = Column(String(100), primary_key=True, nullable=False)
    itemid = Column(Integer, primary_key=True, nullable=False)
    itemcaption = Column(String(100), nullable=False)


class DmFieldsConfig(db.Model):
    __tablename__ = 'dm_fields_config'

    tablename = Column(String(100), primary_key=True, nullable=False)
    fieldname = Column(String(100), primary_key=True, nullable=False)
    fieldcaption = Column(String(100))
    fieldlength = Column(Integer)
    fieldtype = Column(Integer, nullable=False)
    fieldisrequired = Column(String(1), nullable=False)
    fieldisunique = Column(String(1))
    fieldisprimary = Column(String(1))


class DmGlobalDevice(db.Model):
    __tablename__ = 'dm_global_device'

    deviceid = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    type = Column(String(100), nullable=False)
    parent_name = Column(String(100))


class FlowShareDayTax(db.Model):
    __tablename__ = 'flow_share_day_tax'

    pid = Column(Integer, primary_key=True)
    readtime = Column(String(20), nullable=False)
    simid = Column(String(20), nullable=False)
    flux = Column(Float(53))
    plustotalflux = Column(Float(53))
    reversetotalflux = Column(Float(53))
    warning = Column(String(50), nullable=False)
    warningdesc = Column(String(20), nullable=False)


t_g_cloudlayer = Table(
    'g_cloudlayer', db.Model.metadata,
    Column('layername', String(200), nullable=False),
    Column('tablename', String(200), nullable=False),
    Column('layerdesc', String(250)),
    Column('fastquery', SmallInteger)
)


class GCloudlayerMetaDlzxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_dlzxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaDmdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_dmdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaDmxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_dmxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaDwjcdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_dwjcdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaFzdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_fzdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaFzxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_fzxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaGxdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_gxdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaGxxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_gxxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJmddc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jmddc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJmdmc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jmdmc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJmdxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jmdxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJtdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jtdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJtmc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jtmc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaJtxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_jtxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaMczjc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_mczjc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaSxGsWsConcentrator(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_concentrator'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsConnector(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_connector'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsDrainValve(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_drain_valve'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsExEquipment(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_ex_equipment'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsFireHydrant(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_fire_hydrant'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsFlowMeter(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_flow_meter'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsForcePump(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_force_pump'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsMetabox(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_metabox'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsPipe(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_pipe'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsSourceWater(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_source_water'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsValve(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_valve'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsValveWell(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_valve_well'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsVentValve(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_vent_valve'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsWaterMeter(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_water_meter'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxGsWsWatermeterBasin(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_gs_ws_watermeter_basin'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry, nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxQdzdtMapLayer(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sx_qdzdt_map_layer'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    user_define = Column(String(50))
    id = Column(String(20), index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)


class GCloudlayerMetaSxdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sxdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaSxmc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sxmc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaSxxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sxxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaSxzxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_sxzxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaZbdc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_zbdc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaZbmc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_zbmc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


class GCloudlayerMetaZbxc(db.Model):
    __tablename__ = 'g_cloudlayer_meta_zbxc'

    metaid = Column(Integer, primary_key=True)
    metaname = Column(String(200))
    bounds_size = Column(Float(53), index=True)
    blockdata = Column(LargeBinary)
    bounds_geom = Column(Geometry(u'POLYGON'), nullable=False, index=True)
    geomdata = Column(Geometry, index=True)
    geomjson = Column(Text)
    id = Column(String(20), index=True)
    user_define = Column(String(50))


t_geography_columns = Table(
    'geography_columns', db.Model.metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', db.Model.metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)


class HdbTianhouBig(db.Model):
    __tablename__ = 'hdb_tianhou_big'

    id = Column(Integer, primary_key=True)
    rvalue = Column(String(30))
    fvalue = Column(String(30))
    meterstate = Column(String(30))
    commstate = Column(String(30))
    rtime = Column(String(30))
    lastrvalue = Column(String(30))
    lastrtime = Column(String(30))
    dosage = Column(String(30))
    user_watermeter_id = Column(String(32), nullable=False)


class Hdbrecord(db.Model):
    __tablename__ = 'hdbrecord'

    id = Column(Integer, primary_key=True)
    hdate = Column(String(30))


class PressShareDayTax(db.Model):
    __tablename__ = 'press_share_day_tax'

    pid = Column(Integer, primary_key=True)
    readtime = Column(String(20), nullable=False)
    simid = Column(String(20), nullable=False)
    pressure = Column(Float(53))
    warning = Column(String(50), nullable=False)
    warningdesc = Column(String(20), nullable=False)


class UserWatermeter(db.Model):
    __tablename__ = 'user_watermeter'

    id = Column(String(32), primary_key=True)
    numbersth = Column(String(30))
    roomname = Column(String(128))
    nodeaddr = Column(String(30))
    wateraddr = Column(String(30))
    rvalue = Column(String(30))
    metertype = Column(String(30))
    fvalue = Column(String(30))
    meterstate = Column(String(30))
    commstate = Column(String(30))
    rtime = Column(String(30))
    lastrvalue = Column(String(30))
    lastrtime = Column(String(30))
    dosage = Column(String(30))
    islargecalibermeter = Column(Integer)
    metering_equipment_id = Column(String(20), nullable=False)


class WsConcentrator(db.Model):
    __tablename__ = 'ws_concentrator'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    community = Column(String(128), unique=True)
    address = Column(String(128), unique=True)
    commdev = Column(String(30))
    devaddr = Column(String(30))
    commmodel = Column(String(64))
    commparam = Column(String(64))
    tel = Column(String(30))
    netparam = Column(String(30))
    manufacturer = Column(String(32))
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))


class WsConnector(db.Model):
    __tablename__ = 'ws_connector'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    type = Column(String(10))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsDrainValve(db.Model):
    __tablename__ = 'ws_drain_valve'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsExEquipment(db.Model):
    __tablename__ = 'ws_ex_equipment'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsExResourceProperty(db.Model):
    __tablename__ = 'ws_ex_resource_property'

    tablename = Column(String(128), primary_key=True, nullable=False)
    fieldname = Column(String(128), primary_key=True, nullable=False)
    fieldtype = Column(Integer)
    fieldlength = Column(Integer)
    caption = Column(String(128), unique=True)
    enabled = Column(Integer)
    mapping_column_no = Column(Integer)


class WsExResourcePropertyEnumDefine(db.Model):
    __tablename__ = 'ws_ex_resource_property_enum_define'

    tablename = Column(String(128), primary_key=True, nullable=False)
    fieldname = Column(String(128), primary_key=True, nullable=False)
    enumvalue = Column(Integer, primary_key=True, nullable=False)
    enumcaption = Column(String(128), nullable=False)


class WsExResourceType(db.Model):
    __tablename__ = 'ws_ex_resource_type'

    tablename = Column(String(128), primary_key=True)
    caption = Column(String(128), unique=True)
    input_time = Column(String(20))


class WsFireHydrant(db.Model):
    __tablename__ = 'ws_fire_hydrant'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsFlowMeter(db.Model):
    __tablename__ = 'ws_flow_meter'

    id = Column(String(20), primary_key=True)
    name = Column(String(128))
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    simid = Column(String(20))
    memo = Column(String(256))


class WsForcePump(db.Model):
    __tablename__ = 'ws_force_pump'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsMetabox(db.Model):
    __tablename__ = 'ws_metabox'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    buildingno = Column(String(128))
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    concentrator_id = Column(String(20))


class WsPipe(db.Model):
    __tablename__ = 'ws_pipe'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    material = Column(String(256))
    caliber = Column(Float(53))
    length = Column(Float(53))
    pipe_first = Column(String(20))
    pipe_end = Column(String(20))
    memo = Column(String(256))
    buried = Column(Float(53))
    start_depth = Column(Float(53))
    end_depth = Column(Float(53))
    burying = Column(String(256))
    start_altitude = Column(Float(53))
    end_altitude = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsPipeType(db.Model):
    __tablename__ = 'ws_pipe_type'

    id = Column(String(5), primary_key=True)
    name = Column(String(128))


class WsProjectInfo(db.Model):
    __tablename__ = 'ws_project_info'

    id = Column(String(32), primary_key=True, nullable=False)
    number = Column(String(64), primary_key=True, nullable=False)
    project_name = Column(String(255), nullable=False)
    manager_unit = Column(String(255))
    owner = Column(String(255))
    area = Column(String(255))
    completion_time = Column(String(20))
    measurement_unit = Column(String(64))
    input_staff = Column(String(50))
    input_staff_id = Column(String(32))
    state = Column(Integer)
    minx = Column(Float(53))
    miny = Column(Float(53))
    maxx = Column(Float(53))
    maxy = Column(Float(53))
    input_time = Column(String(20))
    modify_staff_id = Column(String(32))
    modify_time = Column(String(20))


class WsProjectMeasurementRecord(db.Model):
    __tablename__ = 'ws_project_measurement_record'

    id = Column(String(32), primary_key=True)
    project_id = Column(String(32), nullable=False)
    equipement_id = Column(String(20), nullable=False)
    type = Column(String(255), nullable=False)


class WsResource(db.Model):
    __tablename__ = 'ws_resource'

    id = Column(String(20), primary_key=True)
    tablename = Column(String(128), nullable=False)


class WsSourceWater(db.Model):
    __tablename__ = 'ws_source_water'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsUserOpCascadeLog(db.Model):
    __tablename__ = 'ws_user_op_cascade_log'

    id = Column(Integer, primary_key=True)
    op_mode = Column(Integer)
    topo_old = Column(String(62))
    topo_old_points = Column(String(255))
    topo_new = Column(String(62))
    topo_new_points = Column(String(255))
    attr_id = Column(String(20))
    attr_tablename = Column(String(128))
    meta_id = Column(Integer)
    meta_tablename = Column(String(128))
    op_cascade_id = Column(String(255))


class WsValve(db.Model):
    __tablename__ = 'ws_valve'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsValveWell(db.Model):
    __tablename__ = 'ws_valve_well'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsVentValve(db.Model):
    __tablename__ = 'ws_vent_valve'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))


class WsWaterMeter(db.Model):
    __tablename__ = 'ws_water_meter'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))


class WsWatermeterBasin(db.Model):
    __tablename__ = 'ws_watermeter_basin'

    id = Column(String(20), primary_key=True)
    name = Column(String(128), unique=True)
    input_time = Column(String(20))
    input_staff = Column(String(50))
    modify_time = Column(String(20))
    modify_staff = Column(String(50))
    location_x = Column(Float(53))
    location_y = Column(Float(53))
    memo = Column(String(256))
    altitude = Column(Float(53))
    depth = Column(Float(53))
    caliber = Column(Float(53))
    material = Column(String(256))
    burying = Column(String(256))
    angle = Column(Float(53))
    area = Column(String(256))
    road = Column(String(256))
    unit = Column(String(256))
    project_ref_count = Column(Integer)
    op_vaild = Column(Integer)
    project_no = Column(String(256))
    external_code = Column(String(256))
