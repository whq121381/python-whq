# '''
# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体
# '''
# class shuibei:
#     __height = 0
#     __volume = 0
#     __color = ""
#     __material = ""
#
#     def setHeight(self,height):
#         if height <= 0 and type != int:
#             print("输入错误！")
#         else:
#             self.__height = height
#     def getHeight(self):
#         return self.__height
#     def setVolume(self,volume):
#         if volume <= 0:
#             print("error!")
#         else:
#             self.__volume = volume
#     def getVolume(self):
#         return self.__volume
#     def setColor(self,color):
#         self.__color = color
#     def getColor(self):
#         return self.__color
#     def setMaterial(self,material):
#         if material != '陶瓷' and material != '玻璃' \
#         and material != '塑料' and material != '不锈钢':
#             print("输入错误！\n 请在以下范围内选择：陶瓷、玻璃、塑料、不锈钢")
#         else:
#             self.__material = material
#     def getMaterial(self):
#         return self.__material
#     def dayin(self):
#         print("这个杯子高度",self.__height,"厘米，最大容积",self.__volume,"升，颜色",self.__color,\
#               "色，材质",self.__material,"。")
#
# b = shuibei()
#
# b.setHeight(0)
# b.setColor("银")
# b.setVolume(0.5)
# b.setMaterial("不锈钢")
# b.dayin()
# # print(b.getHeight(),b.getVolume(),b.getColor(),b.getMaterial())

class computer:
    __scrsize = ""
    __price = ""
    __cputype = ""
    __memsize = ""
    __standbydur = ""

    def setScrsize(self,scrsize):
        self.__scrsize = scrsize
    def getScrsize(self):
        return self.__scrsize

    def setPrice(self,price):
        if price <= 0:
            print("error")
        else:
            self.__price = price
    def getPrice(self):
        return self.__price

    def setCputype(self,cputype):
        self.__cputype = cputype
    def getCputype(self):
        return self.__cputype

    def setMemsize(self,memsize):
        self.__memsize = memsize
    def getMemsize(self):
        return self.__memsize

    def setStandbydur(self,standbydur):
        if standbydur <= 0:
            print("error")
        else:
            self.__standbydur = standbydur
    def getStandbydur(self):
        return self.__standbydur

    def showcomputer(self):
        print("这台电脑的屏幕尺寸：",self.__scrsize,"英寸，价格：",self.__price,"元，CPU型号：",self.__cputype,"型,内存：",\
              self.__memsize,"G,待机时长：",self.__standbydur,"小时。"
              )
c = computer()
c.setScrsize(15.6)
c.setPrice(8998.98)
c.setCputype('第十一代英特尔酷睿i7-11800H')
c.setMemsize(512)
c.setStandbydur(10)
c.showcomputer()