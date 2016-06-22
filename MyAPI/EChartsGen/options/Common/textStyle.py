from MyAPI.EChartsGen.options.Common.color import Color,EchartBaseObject



class TextStyle(EchartBaseObject):
    def __init__(self,color= Color('#333'),
                fontStyle= 'normal',
                fontWeight= 'normal',
                fontFamily= 'sans-serif',
                fontSize= 18
                 ):
        self.color	=	color
        self.fontStyle	=	fontStyle
        self.fontWeight	=	fontWeight
        self.fontFamily	=	fontFamily
        self.fontSize	=	fontSize


    def make_json(self):
        json = "textStyle:{"
        json += "color:'{color}',".format(color=self.color) if self.color else ""
        json += "fontStyle:'{fontStyle}',".format(fontStyle=self.fontStyle) if self.fontStyle else ""
        json += "fontWeight:'{fontWeight}',".format(fontWeight=self.fontWeight) if self.fontWeight else ""
        json += "fontFamily:'{fontFamily}',".format(fontFamily=self.fontFamily) if self.fontFamily else ""
        json += "fontSize:{fontSize},".format(fontSize=self.fontSize) if self.fontSize else ""
        json += "},"

        return json

    def __repr__(self):
        return self.make_json()