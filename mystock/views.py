import json
import time

import simplejson as simplejson
from django.db.models import Q

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from mystock import tool
from mystock.models import lrb, codep, yydy


def index(request):
    return render(request,"mystock/index.html")

def getStock(request):

    username = request.POST.get('username')
    print(username)
    datalist=lrb.objects.filter(STOCKNAME=username).values_list('TOTALOPERATEREVE', 'REPORTDATE')
    print(datalist)
    r_data=[]
    for d in datalist:
        timeArray = time.strptime(d[1], "%Y/%m/%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))*1000
        r_data.append([timeStamp,d[0]])
    # 转换为时间戳
    json_r={'data':r_data,'name':'TOTALOPERATEREVE'}

    print(timeStamp)
    #return render(request, "mystock/result.html")
    return render(request, 'mystock/result.html', {'datalist': json.dumps(json_r)})

def bs(request):
    print(request.body)

    data_1=[]
    data_2 = []
    datalist1 = yydy.objects.filter(ch__ne=None).values_list('ch', 'en')
    datalist2 = codep.objects.values_list('area', 'name')
    for d in datalist2:
        data_2.append({'value':d[0],'title':d[1]})
    for d in datalist1:
        #print(d)
        data_1.append({'value':d[1],'title':d[0]})
    json_r = {'data_1':data_1,'data_2':data_2}
    return render(request, 'mystock/bs.html',{'datalist': json.dumps(json_r)})
