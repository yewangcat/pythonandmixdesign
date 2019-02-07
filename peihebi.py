def Fcuo(fcuk=30): #默认设计强度30MP
    global fcuo
    fcuo = fcuk + 1.645 * 5 #确定配置强度
    print("配置强度为：",'%.2f'% fcuo)
    return fcuo #38.2 return终止


def WC(aa=0.53, ab=0.2, rf = 0.85, rs = 1): #回归系数的选用,粉煤灰影响系数
    fce = 42.5*1.16 #49.3强度等级富余系数
    fb = rf*rs*fce #41.91
    wc = (aa*fb) / (fcuo+aa*ab*fb)
    print("水胶比为：",'%.2f'% wc)

def Mwo(ex_mwater,jsj): #输入经验值用水量，减水率(小数值)
    global mwo
    mwo = ex_mwater * (1-jsj)
    print("每立方混凝土用水量mwo：",'%.2f'% mwo,'kg')
    #return mwo

def Mco(f=0.1,jsj=0.01):#粉煤灰占比,减水剂掺量
    global sumMco
    sumMco = mwo / 0.43#WC() #水胶比经验值增大或减小0.05对比试验(小数值)，原0.43
    global mco
    global mfo
    mco =sumMco-sumMco*f
    mfo = sumMco*f
    global mjs
    mjs = sumMco*jsj
    print("胶凝材料用量sumMco：", '%.2f'% sumMco,'kg')
    print("粉煤灰用量mfo：", '%.2f'% mfo,'kg')
    print("水泥用量mco：", '%.2f'% mco,'kg')
    print("减水剂用量mjs：",'%.2f'% mjs,'kg')#减水剂掺量

def Mso(sl=0.44):#输入砂率
    global mso
    mso = (2400-mwo-mco-mfo)*sl
    print("砂用量mso：",'%.2f'% mso,'kg')

def Mgo():
    global mgo
    mgo = 2400-mwo-sumMco-mso
    print("碎石用量mgo：",'%.2f'% mgo,'kg')

def cal():
    print("配合比为：\n水泥：粉煤灰：水：砂：碎石：外加剂 =",\
          '%.1f'% mco,': ''%.1f'% mfo,': ''%.1f'% mwo,\
          ': ''%.1f'% mso,': ''%.1f'% mgo,': ''%.2f'% mjs,"(kg)")


Fcuo(30)#输入设计强度
WC(0.53, 0.2, 0.85, 1)#输入回归系数的选用,粉煤灰掺量
Mwo(236, 0.25)#输入经验值用水量，减水率(小数值)
Mco(0.1, 0.01)#输入粉煤灰占比,减水剂掺量(小数值)
Mso(0.44)#输入砂率增大或减小0.01对比试验(小数值)，原0.44
Mgo()
cal()

















