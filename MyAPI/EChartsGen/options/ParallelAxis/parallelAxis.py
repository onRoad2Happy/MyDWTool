from MyAPI.EChartsGen.options.Common.echartBase import EchartBaseObject
#TODO 优先级较低，暂时不实现

class ParallelAxis(EchartBaseObject):
    def __init__(self, value):
        pass

    def make_json(self):
        raise Exception("请重写make_json函数来生成对应属性的json数据")