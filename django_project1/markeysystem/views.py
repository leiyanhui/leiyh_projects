from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.http import *
from .models import *
from datetime import datetime
from django.contrib.auth import logout
from django.db.models import Q, F
import os


# Create your views here.

# 登录，清除session装饰器
def login_confirm(fun):
    def inner(request, *args, **kwargs):
        username = request.session.get("username")
        passwprd = request.session.get("password")
        if not _validlogin(username, passwprd):
            return render(request, 'marketsystem/login.html', {"msg": "该页面需要登录才可以访问"})
        else:
            return fun(request, *args, **kwargs)

    return inner


# 验证操作权限

def auth_update(fun):
    def inner(request):
        username = request.session.get("username")
        result = User_Form.user_objects.get(user_name=username)
        job_type = result.job_type
        print(job_type)
        if job_type:
            return fun(request)
        else:
            return render(request, "marketsystem/auth_login.html")

    return inner


# 判断账号密码是否正确
def _validlogin(username, password):
    return User_Form.user_objects.filter(user_name=username).filter(user_password=password)


# 配置完整网页

# 主页账单功能功能
@login_confirm
def admin_bill_list(request):
    supplier_list = Supplier_Form.supplier_objects.all()
    goods_name = request.GET.get("productName")
    select = request.GET.get("payStatus")
    if select == "" or select == None:
        select = None
    elif select == "0":
        select = False
    elif select == "1":
        select = True
    if goods_name == "" or goods_name == None:
        if select is None:
            bill_list = Bill_Form.bill_objects.all()
        else:
            bill_list = Bill_Form.bill_objects.filter(bill_spend=select)
        content = {'bill_list': bill_list, 'supplier_list': supplier_list}
        return render(request, 'marketsystem/admin_bill_list.html', content)
    else:
        if select is None:
            bill_list = Bill_Form.bill_objects.filter(bill_goods_name=goods_name)
        else:
            bill_list = Bill_Form.bill_objects.filter(bill_spend=select, bill_goods_name=goods_name)
        content = {'bill_list': bill_list, 'supplier_list': supplier_list}
        return render(request, 'marketsystem/admin_bill_list.html', content)


# 添加账单
@login_confirm
def addbillpre(request):
    supplier_list = Supplier_Form.supplier_objects.all()
    content = {'list': supplier_list}
    return render(request, 'marketsystem/modify.html', content)


@login_confirm
def addbill(request):
    bill_No = request.POST.get('billNum')
    bill_money = request.POST.get('money')
    bill_dealnum = request.POST.get('dealnum')
    bill_goodsname = request.POST.get('goodsname')

    bill_supplier_name = request.POST.get('supplier')
    foreigin_key = Supplier_Form.supplier_objects.get(id=bill_supplier_name)

    bill_isPay = request.POST.get('isPay')
    if bill_isPay is "0":
        bill_isPay = False
    else:
        bill_isPay = True

    bill_desc = request.POST.get('discription')
    Bill_Form.bill_objects.bill_create(bill_No, bill_goodsname, bill_dealnum, bill_money, bill_isPay, bill_desc,
                                       foreigin_key)
    return redirect(reverse('user:admin_bill_list'))


# 更新账单

# 获取数据
@login_confirm
def bill_getdata(request, id):
    bill = Bill_Form.bill_objects.filter(pk=id)
    sid = Supplier_Form.supplier_objects.all()
    if bill[0].bill_spend:
        isPay = 1
    else:
        isPay = 0
    result = {'billNum': bill[0].bill_No, "money": bill[0].bill_goods_money, 'dealnum': bill[0].bill_goods_num,
              "goodsname": bill[0].bill_goods_name, "discription": bill[0].bill_goods_des,
              "supplier": bill[0].bill_goods_supplier, "isPay": isPay, "supplier_list": sid}
    return render(request, 'marketsystem/bill_reset.html', result)


# 更新删除方法
@login_confirm
def bill_update(request):
    billNum = request.POST.get('billNum')
    money = request.POST.get("money")
    goodsname = request.POST.get("goodsname")
    discription = request.POST.get('discription')
    supplier = request.POST.get('supplier')
    foreigin_key = Supplier_Form.supplier_objects.get(supplier_info=supplier)
    isPay = request.POST.get('isPay')
    if request.POST.get('submit') == "修改":
        bill_data = Bill_Form.bill_objects.get(bill_No=billNum)
        bill_data.bill_No = billNum
        bill_data.bill_goods_money = money
        bill_data.bill_goods_name = goodsname
        bill_data.bill_goods_des = discription
        bill_data.bill_goods_supplier = foreigin_key
        bill_data.bill_spend = isPay
        bill_data.save()
        return redirect(reverse('user:admin_bill_list'))
    # 删除数据
    else:
        Bill_Form.bill_objects.get(bill_No=billNum).delete()
        return redirect(reverse('user:admin_bill_list'))


@login_confirm
def admin_left(request):
    return render(request, 'marketsystem/admin_left.html')


@login_confirm
def admin_top(request):
    msg = request.session.get("username")
    content = {"msg": msg}
    return render(request, 'marketsystem/admin_top.html', content)


@login_confirm
def modify(request):
    return render(request, 'marketsystem/modify.html')


@login_confirm
@auth_update
def providerAddpre(request):
    return render(request, 'marketsystem/providerAdd.html')


@login_confirm
@auth_update
def providerAdd(request):
    provider_No = request.POST.get('proId')
    provider_info = request.POST.get('proName')
    supplier_des = request.POST.get("proDesc")
    supplier_name = request.POST.get("contact")
    supplier_phone = request.POST.get("phone")
    supplier_address = request.POST.get("address")
    Supplier_Form.supplier_objects.supplier_create(provider_No, provider_info, supplier_des, supplier_name,
                                                   supplier_phone, supplier_address)
    return redirect(reverse('user:providerAdmin'))


# 供应商更新、删除
@login_confirm
@auth_update
def provider_getdata(request, id):
    provider = Supplier_Form.supplier_objects.filter(pk=id)
    result = {'proId': provider[0].supplier_No, "proName": provider[0].supplier_info,
              'proDesc': provider[0].supplier_des,
              "contact": provider[0].supplier_name, "phone": provider[0].supplier_phone,
              "address": provider[0].supplier_address}
    return render(request, 'marketsystem/providermodefy.html', result)

@login_confirm
@auth_update
def providermodefy(request):
    proId = request.POST.get('proId')
    proName = request.POST.get("proName")
    proDesc = request.POST.get("proDesc")
    contact = request.POST.get('contact')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    if request.POST.get('button') == "修改":
        supplier_data = Supplier_Form.supplier_objects.get(supplier_No=proId)
        print(supplier_data)
        supplier_data.supplier_No=proId
        supplier_data.supplier_info = proName
        supplier_data.supplier_des = proDesc
        supplier_data.supplier_name = contact
        supplier_data.supplier_phone = phone
        supplier_data.supplier_address = address
        supplier_data.save()
        return redirect(reverse('user:providerAdmin'))
    # 删除数据
    else:
        Supplier_Form.supplier_objects.get(supplier_No=proId).delete()
        return redirect(reverse('user:providerAdmin'))


@login_confirm
@auth_update
def providerAdmin(request):
    providerName = request.POST.get("providerName")
    providerDesc = request.POST.get("providerDesc")
    if providerName == "" or providerName is None:
        if providerDesc == "" or providerDesc == None:
            supplier_list = Supplier_Form.supplier_objects.all()
        else:
            supplier_list = Supplier_Form.supplier_objects.filter(supplier_des=providerDesc)
        content = {'list': supplier_list}
        return render(request, 'marketsystem/providerAdmin.html', content)
    else:
        if providerDesc == "" or providerDesc == None:
            supplier_list = Supplier_Form.supplier_objects.filter(supplier_name=providerName)
        else:
            supplier_list = Supplier_Form.supplier_objects.filter(supplier_name=providerName,
                                                                  supplier_des=providerDesc)
        content = {'list': supplier_list}
        return render(request, 'marketsystem/providerAdmin.html', content)


@login_confirm
@auth_update
def userAddpre(request):
    return render(request, 'marketsystem/userAdd.html')


@login_confirm
@auth_update
def userAdd(request):
    user_No = request.POST.get('userId')
    user_name = request.POST.get('username')
    user_password = request.POST.get('userpassword')
    user_rpassword = request.POST.get('userpassword1')
    user_gender = request.POST.get('sex')
    if user_gender == '0':
        user_gender = False
    else:
        user_gender = True

    user_age = request.POST.get('age')
    user_phone = request.POST.get('mobile')
    user_address = request.POST.get('address')
    user_job_type = request.POST.get("auth")
    if user_password == user_rpassword:
        password = user_rpassword
        User_Form.user_objects.user_create(user_No, user_name, password, user_gender, user_age, user_phone,
                                           user_address,
                                           user_job_type)
        return redirect(reverse("user:userAdmin"))
    else:
        content = {'msg': '两次密码不一致'}
        return render(request, 'marketsystem/userAdd.html', content)


@login_confirm
@auth_update
def userAdmin(request):
    username = request.POST.get("userName")
    if username:
        user_list = User_Form.user_objects.filter(user_name=username)
    else:
        user_list = User_Form.user_objects.all()
    content = {"list": user_list}
    return render(request, 'marketsystem/userAdmin.html', content)

# 账户添加以及删除
@login_confirm
def user_getdata(request, id):
    user_acount = User_Form.user_objects.filter(pk=id)
    if user_acount[0].user_gender:
        sex = 1
    else:
        sex = 0
    if user_acount[0].job_type:
        auth = 1
    else:
        auth = 0

    result = {'userId':user_acount[0].user_No, "username":user_acount[0].user_name,
              'password': user_acount[0].user_password,
              "sex": sex, "age": user_acount[0].user_age,
              "mobile": user_acount[0].user_phone, 'address':user_acount[0].user_address, "auth":auth}
    return render(request, 'marketsystem/usemodefy.html', result)

@login_confirm
def user_modefy(request):
    userId = request.POST.get('userId')
    username = request.POST.get("username")
    password = request.POST.get("password")
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')
    auth = request.POST.get('auth')
    if request.POST.get('button') == "修改":
        user_data = User_Form.user_objects.get(user_No=userId)
        user_data.user_No = userId
        user_data.user_name=username
        user_data.user_password = password
        user_data.user_gender = sex
        user_data.user_age = age
        user_data.user_phone = mobile
        user_data.user_address = address
        user_data.job_type = auth
        user_data.save()

        return redirect(reverse('user:userAdmin'))
    # 删除数据
    else:
        User_Form.user_objects.filter(user_No=userId).delete()
        return redirect(reverse('user:userAdmin'))


@login_confirm
def loginsucess(request):
    return render(request, 'marketsystem/loginsucess.html')


# 登录
def loginpage(request):
    username = request.POST.get("userName")
    password = request.POST.get("passWord")
    if username is None or password is None:
        return render(request, 'marketsystem/login.html', {"msg": '账户或密码不能为空'})


def login(request):
    username = request.POST.get("userName")
    password = request.POST.get("passWord")
    if username is None or password is None:
        return render(request, 'marketsystem/login.html', {"msg": '账户或密码不能为空'})
    else:
        u = _validlogin(username, password)
        if u:
            request.session.set_expiry(0)
            request.session["username"] = u[0].user_name
            request.session["password"] = u[0].user_password
            req = render(request, 'marketsystem/admin_index.html')
            return req
        else:
            return render(request, 'marketsystem/login.html', {"msg": '账户或密码不正确'})


# 安全退出登录
def logouting(request):
    logout(request)
    return redirect(reverse('user:loginpage'))
