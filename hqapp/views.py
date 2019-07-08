import random
import string
import time
from uuid import UUID

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from hqapp.models import TUser,Text,TLog
# from ddapp.car import Cartitem,Cart

def login(request):
    print(15)
    return render(request, "hqapp/login.html")





def loginlogic(request):   #进不了主页
    print('loginlogic')
    userid = request.POST.get("userid")
    psw = request.POST.get("psw")
    user = TUser.objects.get(username=userid,password=psw)
    if user:
        print('进main')
        return redirect('main')
    else:
        return HttpResponse("用户名或密码错误，请重新登录")





def checklname(request):              #验证登录用户名
    lname = request.GET.get("lname")
    if lname == "":
        print("null")
        return HttpResponse("null")
    else:
        print("no", 29)
        return HttpResponse("ok")



def checklpwd(request):  # 验证登录密码
    lpwd = request.GET.get("lpwd")
    if lpwd == "":
        print("null")
        return HttpResponse("null")
    else:
        print("no", 29)
        return HttpResponse("ok")


def check(request):  #验证用户名和密码
    lname=request.GET.get("lname")
    upwd = request.GET.get("upwd")
    print(lname,upwd)
    user = TUser.objects.filter(username=lname,password=upwd)
    if user:
        print('好的')
        return HttpResponse("ok")
    else:
        print('没下去')
        return HttpResponse("no")






def register(request):
    print('进来吧')
    return render(request,"hqapp/register.html")


def registerlogic(request):
    try:
        print(24)
        with transaction.atomic():
            email = request.POST.get("email")
            username = request.POST.get("userid")
            password = request.POST.get("psw")
            phone = request.POST.get("usrtel")
            tuser = TUser.objects.create(email=email, username=username, password=password,status=phone)
            print('哈哈')
            return redirect('main')
    except:
        return HttpResponse("注册失败")





def checkrname(request):              #验证注册用户名
    rname = request.GET.get("rname")
    if rname == "":
        return HttpResponse("null")
    else:
        return HttpResponse("ok")




def checkrphone(request):              #验证注册手机号
    rphone = request.GET.get("rphone")
    print(rphone)
    if rphone == "":
        return HttpResponse("null")
    else:
        return HttpResponse("ok")



def checkremail(request):              #验证注册邮箱
    remail = request.GET.get("remail")
    print(remail)
    if remail == '':
        print('null')
        return HttpResponse("null")
    else:
        print('ok')
        return HttpResponse("ok")


def checkrpwd(request):              #验证密码
    rpwd = request.GET.get("rpwd")
    print(rpwd)
    if rpwd == '':
        print('null')
        return HttpResponse("null")
    else:
        print('ok')
        return HttpResponse("ok")


# with open('ips1.txt','w')as w:
#     for tr in html.xpath('//tr')[1:]:
#         # ./ 从当前对象开始选择
#         tds=tr.xpath('./td/text()')
#         ip={tds[5].lower():tds[0]+':'+tds[1]}
#         if ip:
#             w.write(str(ip))
#             w.write('\n')




def time(f):
    print('走了')
    def inner(*args,**kwargs):
        print(args,139)
        print(type(args),99)
        for i in args:
            print(i.META)
            url = i.META['HTTP_REFERER']
            print(url)
            cookie=i.META['CSRF_COOKIE']
            print(cookie,'cookie')
            port = i.META['PYCHARM_MATPLOTLIB_PORT']
            ip = i.META['REMOTE_ADDR']
            revision = i.META['PROCESSOR_REVISION']
            print(revision,149)
            print(port,'port')
            print(ip,'ip')
            TLog.objects.create(url=url,cookie=cookie,port=port,revision=revision)
            with open('data.txt','a+')as w:
                w.write(url)+w.write('\t')+w.write(cookie)+w.write('\t')+w.write(str(port))+w.write('\t')+ w.write(ip)
                w.write('\n')
            r = f(*args,**kwargs)
            return r
    return inner

@time
def menu(request):
    houvalue=request.GET.get('houvalue')
    objzhi=request.GET.get('objzhi')
    print(houvalue,'我是后边的')
    print(objzhi,'我是后边的吱吱吱')
    num = request.GET.get("num")
    parentID = request.GET.get("parentID")   #接收城市id
    print(parentID,143)
    resourceName = request.GET.get("resourceName")   #接收职位
    print(resourceName,145)
    l = []
    city=['北京','上海','广州','深圳']   #城市
    zhiwei=['web','大数据','爬虫','AI']   #职业
    if parentID in city and resourceName in zhiwei:  #左边
        request.session["parentID"] = parentID
        request.session["resourceName"] = resourceName
        print('我走了if')
        l = []
        infos = Text.objects.filter(qiwaddr=parentID, qiwzhiwei__contains=resourceName)  # Z城市精确，模糊
        print(infos)
        for i in infos:
            l.append(i)
        pagtor = Paginator(l, per_page=4)
        pcount = pagtor.num_pages  # 这是要传给前端的总页数
        print(pcount, 149)
        count = pagtor.count
        print(count, 88)
        if not num or not num.isdigit() or int(num) < 1:
            num = 1
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html', {"parentID":parentID,"resourceName":resourceName,"page": page, "pcount": pcount, "count": count, "num":num})
#原来这里有东西
        else:
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html',
                          {"parentID":parentID,"resourceName":resourceName,"page": page, "pcount": pcount, "count": count, "num": num})  # 有传过来页码


    elif  houvalue=="职位" and   objzhi in zhiwei:
        print('我进了elif我是职位匹配')
        infos = Text.objects.filter(qiwzhiwei=objzhi, qiwaddr__in=('北京','上海','广州','深圳'))
        for i in infos:
            print(i, 44)
            l.append(i)
        pagtor = Paginator(l, per_page=4)
        pcount = pagtor.num_pages  # 这是要传给前端的总页数
        print(pcount, 149)
        count = pagtor.count
        print(count, 88)

        if not num or not num.isdigit() or int(num) < 1:
            num = 1
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html', {"houvalue":houvalue,"objzhi":objzhi,"page": page, "pcount": pcount, "count": count, "num": num})
        else:
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html',
                          {"page": page, "pcount": pcount, "count": count, "num": num})  # 有传过来页码


    elif  houvalue=="城市" and   objzhi in city:
        print('我进了elif')
        infos = Text.objects.filter(qiwaddr=objzhi, qiwzhiwei__in=('开发','设计','测试','培训'))
        for i in infos:
            # print(i, 44)
            l.append(i)
        pagtor = Paginator(l, per_page=4)
        pcount = pagtor.num_pages  # 这是要传给前端的总页数
        print(pcount, 149)
        count = pagtor.count
        print(count, 88)

        if not num or not num.isdigit() or int(num) < 1:
            num = 1
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html', {"houvalue":houvalue,"objzhi":objzhi,"page": page, "pcount": pcount, "count": count, "num": num})
        else:
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html',
                          {"houvalue":houvalue,"objzhi":objzhi,"page": page, "pcount": pcount, "count": count, "num": num})  # 有传过来页码

    else:
        print('我没走if')
        for c in city:
            for z in zhiwei:
                infos = Text.objects.filter(qiwaddr=c,qiwzhiwei__contains=z)
                for i in infos:
                    # print(i, 44)
                    l.append(i)
        pagtor = Paginator(l, per_page=4)
        pcount = pagtor.num_pages  # 这是要传给前端的总页数
        print(pcount, 149)
        count = pagtor.count
        print(count, 88)
        if not num or not num.isdigit() or int(num) < 1:
            num = 1
            page = pagtor.page(num)
            print(page, 151)
            return render(request, 'hqapp/menu.html', {"page": page, "pcount": pcount, "count": count, "num": num})
        else:
            page = pagtor.page(num)
            print(page, 151)
            print('我应该进这里的')
            return render(request, 'hqapp/menu.html',
                          {"page": page, "pcount": pcount, "count": count, "num": num})  # 有传过来页码








def introduce(request):
    return render(request,'hqapp/introduce.html')



def main(request):

    return render(request,'hqapp/main.html')



