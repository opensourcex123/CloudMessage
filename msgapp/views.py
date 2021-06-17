from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,JsonResponse
from django.template import Template,Context
# Create your views here.

def msgproc(request):
    datalist=[]
    if request.method == 'POST':
        userA=request.POST.get('userA')
        userB=request.POST.get('userB')
        msg=request.POST.get('msg')
        time=datetime.now()
        with open('msgdata.txt','a+') as f:
            f.write('{}--{}--{}--{}--\n'.format(userB,userA,msg,time.strftime('%Y-%m-%d %H:%M:%S')))
    if request.method=='GET':
        userC=request.GET.get('userC')
        if userC!=None:
            with open('msgdata.txt','r') as f:
                cnt=0
                for line in f:
                    linedata=line.split('--')
                    if linedata[0]==userC:
                        cnt+=1
                        d={"userA":linedata[1], "msg":linedata[2]
                             , "time":linedata[3]}
                        datalist.append(d)
                    if cnt>=10:
                        break
    return render(request,'MsgSingleWeb.html',{'data':datalist})

def homeproc(request):
    return HttpResponse("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")

def homeproc1(request):
    response = JsonResponse({'key':'value'})
    return response

def pgproc(request):
    template=Template('<h1>这个程序的名字是{{name}}</h1>')
    context=Context({'name':'实验平台'})
    return HttpResponse(template.render(context))