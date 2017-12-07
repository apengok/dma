# -*- coding: utf-8 -*-

from collections import OrderedDict
#分区资料
dma_file = OrderedDict()

dma_file['name']={'value':'somecity','name':'分区名称','note':''}
dma_file['zone']={'value':'1000','name':'分区面积（平方公里）','note':''}
dma_file['water_in']={'value':14490,'name':'分区进水量（ m3）','note':''}
dma_file['regist_home']={'value':10000,'name':'注册用户总数（万户）','note':''}
dma_file['pipeline_length']={'value':2000,'name':'管线长度（ km）','note':''}
dma_file['next_distribute_num']={'value':10,'name':'下一级分区数量（个）','note':''}
dma_file['dma_num']={'value':20,'name':'分区中 DMA 数量（个）','note':''}
dma_file['measure_read_rate']={'value':89,'name':'水表抄见率（ %）','note':''}
dma_file['measure_right_rate']={'value':95,'name':'抄表准确率（ %）','note':''}
dma_file['distribute_sale']={'value':12345,'name':'分区销售水量（ m3）','note':'该分区销售水量'}
dma_file['night_min_flow']={'value':2000,'name':'夜间最小流量（ m3）','note':'仅适用于 DMA'}
dma_file['online_presspoint_num']={'value':10,'name':'在线压力点数量（个）','note':''}
dma_file['online_flow_calc_num']={'value':20,'name':'在线流量计数量（个）','note':''}
dma_file['online_water_quality_m_num']={'value':30,'name':'在线水质监测点数量（个）','note':''}
dma_file['charge_remote_water_num']={'value':1000,'name':'收费用远传水表数量（只）','note':''}
dma_file['charge_remote_water_percent']={'value':70,'name':'收费用远传水表水量占分区销 水量比（ %）','note':''}
dma_file['distribute_detect_leak_num']={'value':5,'name':'分区探出漏点总数（个）','note':''}
dma_file['leak_water']={'value':100,'name':'漏失水量（ m3）','note':''}
dma_file['leak_obscur_water']={'value':30,'name':'暗漏水量（ m3）','note':''}
dma_file['leak_obvious_water']={'value':70,'name':'明漏水量（ m3）','note':''}
dma_file['leak_rate']={'value':12,'name':'漏损率（ %）','note':''}
dma_file['pressure_quality']={'value':90,'name':'压力合格率（ %）','note':''}
dma_file['water_quality']={'value':99,'name':'水质合格率（ %）','note':''}
dma_file['distribute_pressure']={'value':30,'name':'分区内压力（ MPa）','note':''}


#汇总资料
summary_file = OrderedDict()
summary_file['totol_water_yearly']={'value':10000,'name':'年供水总量（万 m3）','note':''}
summary_file['registed_user_use_water_yearly']={'value':1000,'name':'年注册用户用水量（万 m3）','note':''}
summary_file['leak_obvious_water']={'value':14490,'name':'明漏水量（万 m3）','note':''}
summary_file['leak_obscur_water']={'value':10000,'name':'暗漏水量（万 m3）','note':''}
summary_file['background_leak_water']={'value':2000,'name':'背景漏失水量（万 m3）','note':''}
summary_file['box_sank_leak']={'value':10,'name':'水箱、水池的渗漏和溢流水量 （万 m3）','note':''}
summary_file['resident_loss_distant']={'value':20,'name':'居民用户总分表差损失水量（万 m3）','note':''}
summary_file['no_resident_loss_distant']={'value':89,'name':'非居民用户表具误差损失水量（万m3）','note':''}
summary_file['measure_read_resident_use']={'value':95,'name':'抄表到户居民用户用水量（万 m3）','note':''}
summary_file['average_press_out']={'value':12345,'name':'年平均出厂压力（ MPa）','note':''}
summary_file['max_frozone_depth']={'value':2000,'name':'最大冻土深度（ m）','note':''}
summary_file['pipenet_length']={'value':10,'name':'管网长度（ km）','note':''}
summary_file['pipenet_distribute_level']={'value':20,'name':'管网分区计量级别数','note':''}
summary_file['distribute_num_1']={'value':30,'name':'一级分区数量（个）','note':''}
summary_file['distribute_cover_water_1']={'value':1000,'name':'一级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_1']={'value':70,'name':'一级分区覆盖管网长度（ km）','note':''}
summary_file['distribute_num_2']={'value':30,'name':'二级分区数量（个）','note':''}
summary_file['distribute_cover_water_2']={'value':1000,'name':'二级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_2']={'value':70,'name':'二级分区覆盖管网长度（ km）','note':''}
summary_file['distribute_num_n']={'value':30,'name':'N级分区数量（个）','note':''}
summary_file['distribute_cover_water_n']={'value':1000,'name':'N级分区覆盖水量（万 m3）','note':''}
summary_file['distribute_cover_pipeline_n']={'value':70,'name':'N级分区覆盖管网长度（ km）','note':''}
summary_file['pipenet_press_qulity']={'value':5,'name':'管网压力合格率','note':''}
summary_file['pipenet_water_qulity']={'value':100,'name':'管网水质合格率','note':''}
summary_file['service_content_rate']={'value':30,'name':'用户服务综合满意率','note':''}
summary_file['pipeline_leak_rate']={'value':70,'name':'管网漏损率','note':''}
summary_file['measure_read_rate']={'value':12,'name':'水表抄见率（ %）','note':''}
summary_file['measure_right_rate']={'value':90,'name':'抄表准确率（ %）','note':''}
summary_file['online_presspoint_num']={'value':99,'name':'在线压力点数量（个）','note':''}
summary_file['online_flow_calc_num']={'value':30,'name':'在线流量计数量（个）','note':''}
summary_file['online_water_quality_m_num']={'value':12,'name':'在线水质监测点数量（个）','note':''}
summary_file['charge_remote_water_num']={'value':90,'name':'收费用远传水表数量（只）','note':''}
summary_file['charge_remote_water_percent']={'value':99,'name':'收费用远传水表水量占销售水量比（ %）','note':''}
summary_file['detect_leak_num']={'value':30,'name':'探出漏点总数（个）','note':''}
summary_file['water_leakloss']={'value':30,'name':'漏失水量(万 m3)','note':''}
summary_file['leak_rate']={'value':12,'name':'漏损率（ %）','note':''}
summary_file['pressure_quality']={'value':90,'name':'压力合格率（ %）','note':''}
summary_file['water_quality']={'value':99,'name':'水质合格率（ %）','note':''}
summary_file['distribute_pressure']={'value':30,'name':'压力（ MPa）','note':''}
summary_file['economic_invest']={'value':12,'name':'经济投入','note':''}
summary_file['economic_benefit']={'value':90,'name':'经济效益','note':''}
summary_file['socity_benefit']={'value':99,'name':'社会效益','note':''}

static_monthly = OrderedDict() 
static_monthly['total_in']={'name':'1、供水总量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['provid_self']={'name':'    其中：1.1 自产供水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['provid_out']={'name':'        1.2 外购供水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['register_resident_use']={'name':'2、注册用户用水量(有效供水量)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['charge_water']={'name':'2.1 计费用水量(售水量)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['charge_measure_water']={'name':'2.1.1 计费计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['resisent_use']={'name':'2.1.1.1 居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['measure_read_resident_use']={'name':'其中:抄表到户的居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['no_measure_read_resident_use']={'name':'未抄表到户的居民用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['no_resident_use']={'name':'2.1.1.2 非居民用水量(含特殊行业)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['high_precise_meter_use']={'name':'其中:高精度水表用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['other_meter_use']={'name':'其他类型水表用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['uncharge_unmeter_use']={'name':'2.1.2 计费未计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['new_pipeline_wash']={'name':'其中:新建管线冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipeline_rebuild_use']={'name':'管网改造冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['urgent_vihicle_use']={'name':'应急供水车水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['project_leak']={'name':'工程漏水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_use']={'name':'2.2免费用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_measure_use']={'name':'2.2.1免费计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['free_unmeasure_use']={'name':'2.2.2免费未计量用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['fireproof_use']={'name':'其中消防用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['new_pipeline_wash_2']={'name':'新建管线冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipeline_rebuild_use_2']={'name':'管网改造冲洗水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['pipenet_maintain_use']={'name':'管网维护用水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['leakloss']={'name':'3、漏损水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['leak_rate']={'name':'漏损率(%)','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['produce_loss']={'name':'4、产销差水量','last_month_total':'','cur_month':'','cur_month_total':'','note':''}
static_monthly['produce_loss_rate']={'name':'产销差率','last_month_total':'','cur_month':'','cur_month_total':'','note':''}

dma_tree = [
          {
            'text': '分区管理',
            'href': '#',
            'tags': ['4'],
            'nodes': [
              {
                'text': '某市(一级分区)',
                'href': '#',
                'tags': ['2'],
                'nodes': [
                  {
                    'text': '南区(二级分区)',
                    'href': '#',
                    'tags': ['0'],
                    'nodes':[
                        {
                            'text':'DMA1',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA2',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA3',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA4',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA5',
                            'href':'#',
                            'tags':['0']
                        }
                    ]
                  },
                  {
                    'text': '北区(二级分区)',
                    'href': '#',
                    'tags': ['0'],
                    'nodes':[
                        {
                            'text':'DMA6',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA7',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA8',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA9',
                            'href':'#',
                            'tags':['0']
                        },
                        {
                            'text':'DMA10',
                            'href':'#',
                            'tags':['0']
                        }
                    ]
                  }
                ]
              }
            ]
          },
          {
            'text': '汇总资料',
            'href': "/dma_summary/",
            'tags': ['0']
          },
          
        ]