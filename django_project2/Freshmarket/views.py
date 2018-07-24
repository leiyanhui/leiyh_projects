from django.shortcuts import *
from .models import *
from django.http import *
import random
import json


# Create your views here.

# 登录验证装饰器

def valid_login(fun):
    def inner(request, *args, **kwargs):
        username = request.session.get("username")
        pwd = request.session.get("pwd")
        u = _valid(username, pwd)
        # print(u)
        if u:
            return fun(request, *args, **kwargs)
        else:
            content = {"msg": "请求该页面需要登录！"}
            return render(request, 'market_sys/login.html', content)

    return inner


# 控制台上传文件
def index(request):
    picture_list1 = Product_picture.objects.filter(picture_type=1)[:4]
    picture_list2 = Product_picture.objects.filter(picture_type=2)[:4]
    picture_list3 = Product_picture.objects.filter(picture_type=1)[4:8]
    products_list = Products.objects.all()
    username = request.session.get('username')
    user_name = User.objects.filter(user_name=username)
    car_total = Car.objects.all().count()
    if user_name:
        content = {'fruit1': picture_list1, 'fruit2': picture_list3, 'meat': picture_list2, 'products': products_list,
                   "username": user_name, 'count': car_total}
        return render(request, 'market_sys/index.html', content)
    else:
        content = {'fruit1': picture_list1, 'fruit2': picture_list3, 'meat': picture_list2, 'products': products_list,
                   "username": "游客", 'count': 0}
        return render(request, 'market_sys/index.html', content)


# 登录：

def _valid(username, password):
    return User.objects.filter(user_name=username, user_pwd=password)


def loginpage(request):  # 需要修改
    username1 = request.session.get("username")
    pwd = request.session.get("pwd")
    picture_list1 = Product_picture.objects.filter(picture_type=1)[:4]
    picture_list2 = Product_picture.objects.filter(picture_type=2)[:4]
    picture_list3 = Product_picture.objects.filter(picture_type=1)[4:8]
    products_list = Products.objects.all()
    car_total = Car.objects.all().count()
    u = _valid(username1, pwd)
    if u:
        content = {'fruit1': picture_list1, 'fruit2': picture_list3, 'meat': picture_list2,
                   'products': products_list,
                   "username": u[0].user_name, "count": car_total, "valid": 1}
        return render(request, 'market_sys/index.html', content)
    else:
        content = {"msg": "账号密码不正确，请重新登录"}
        result = render(request, 'market_sys/login.html', content)
        request.session.flush()
        return result


def login(request):  # 需要修改
    username1 = request.POST.get("username")
    pwd = request.POST.get("pwd")
    check = request.POST.get("checkbox1")
    picture_list1 = Product_picture.objects.filter(picture_type=1)[:4]
    picture_list2 = Product_picture.objects.filter(picture_type=2)[:4]
    picture_list3 = Product_picture.objects.filter(picture_type=1)[4:8]
    products_list = Products.objects.all()
    username = request.session.get('username')
    user_name = User.objects.filter(user_name=username)
    u = _valid(username1, pwd)
    if u:
        if check:
            request.session.set_expiry(0)
            request.session['username'] = u[0].user_name
            request.session['pwd'] = u[0].user_pwd
            car_total = Car.objects.all().count()
            content = {'fruit1': picture_list1, 'fruit2': picture_list3, 'meat': picture_list2,
                       'products': products_list,
                       "username": u[0].user_name, "count": car_total, "valid": 1}
            return render(request, 'market_sys/index.html', content)
        else:
            car_total = Car.objects.all().count()
            content = {'fruit1': picture_list1, 'fruit2': picture_list3, 'meat': picture_list2,
                       'products': products_list,
                       "username": u[0].user_name, "count": car_total, "valid": 1}
            return render(request, "market_sys/index.html", content)
    else:
        return redirect(reverse("user:loginpage"))


def registpage(request):  # 需要修改
    return render(request, "market_sys/register.html")


def regist(request):  # 需要修改
    username = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    cpwd = request.POST.get("cpwd")
    email = request.POST.get("email")
    allow = request.POST.get("allow")
    if pwd == cpwd:
        if allow:
            User.objects.user_create(username, pwd, email)
            return render(request, 'market_sys/index.html')
        else:
            content = {"msg": "请勾选注册协议"}
            return render(request, 'market_sys/index.html', content)
    else:
        content = {"msg": "两次输入的密码不一致"}
        return render(request, 'market_sys/register.html', content)


# 用户中心
@valid_login
def user_center_site(request):
    car_total = Car.objects.all().count()
    username = request.session.get('username')
    address_first = Address.objects.get(address_name=username)
    print(address_first)
    content = {"count": car_total, "valid": 1, "username": username, 'address_first': address_first}
    return render(request, 'market_sys/user_center_site.html', content)


# 用户订单
@valid_login
def user_center_order(request):
    username = request.session.get('username')
    car_total = Car.objects.all().count()
    content = {"count": car_total, "valid": "1", "username": username}
    return render(request, 'market_sys/user_center_order.html', content)


# 添加收件人
@valid_login
def add_address(request):
    address_name = request.POST.get("address_name")
    address_address = request.POST.get("address_address")
    address_phone = request.POST.get("address_phone")
    username = request.session.get('username')
    user_name = User.objects.get(user_name=username)
    try:
        Address.objects.add_create(address_address, address_name, address_phone, user_name)
        return render(request, "market_sys/user_center_info.html")
    except Exception as msg:
        print(msg)
        return render(request, "market_sys/user_center_info.html", {"msg": "添加失败"})


# 用户信息页
@valid_login
def user_center_info(request):
    username = request.session.get('username')
    # print(username)
    user = User.objects.get(user_name=username).user_name
    # print(user)
    car_total = Car.objects.all().count()
    user_info = Address.objects.get(address_name=user)
    print("*************************************")
    phone = user_info.address_phone
    print(phone)
    address = user_info.address_address
    print(address)
    scan_pro = Scan.objects.all()[:5]
    scan_pic = Product_picture.objects.all()
    content = {"count": car_total, "valid": 1, "username": username, 'user_info': user_info, "scan_pro": scan_pro,
               "scan_pic": scan_pic}
    return render(request, 'market_sys/user_center_info.html', content)


# 购物车

# 1、购物车展示页面
@valid_login
def cart(request):
    # 数据库获取数据
    username = request.session.get("username")
    picture = Product_picture.objects.all()
    car_total = Car.objects.all().count()
    user = User.objects.get(user_name=username)
    all_car = Car.objects.filter(car_user_foreignkey=user).all()
    num = len(all_car)
    content = {'product': all_car, 'picture': picture, "num": num, "count": car_total, "username": username, "valid": 1}
    return render(request, 'market_sys/cart.html', content)


# 点击更新数据库中物品的数量
@valid_login
def cart_update(request):  # ????????????????????????????????????
    try:
        num = request.POST.get("num")
        # print(num)
        p_name = request.POST.get("p_name")
        # print('p_name:', p_name)
        # print("**************************************")
        s = p_name[7:]
        # print(p_name.split("/media/"))
        # print(s)
        p = Product_picture.objects.get(picture_icron=s)
        # print(p)
        c = Car.objects.get(car_product_foreignkey=p.picture_foreKey)
        c.car_num = int(num)
        c.car_single_total = int(num) * int(c.car_product_foreignkey.product_price)
        c.save()
        # print("leiyh")
        # return HttpResponse(123)
    except Exception as msg:
        # print(msg)
        return HttpResponse("数据更新失败，服务器正在维护！")


# 购物车数据库添加数据页面
@valid_login
def cart_adddata(request, id):
    num = int(request.GET.get("num_show fl"))
    product = Products.objects.get(pk=id)
    single_total = num * product.product_price
    name = request.session.get("username")
    user_name = User.objects.get(user_name=name)
    # print(single_total)
    # 数据库添加数据
    try:
        Car.objects.car_create(num, product, user_name, single_total)
        picture_id = Product_picture.objects.get(picture_foreKey=product).id
        return redirect("user:detail", picture_id)
    except:
        p_exit = Car.objects.get(car_product_foreignkey=product)
        p_exit.car_num = p_exit.car_num + num
        p_exit.car_single_total = p_exit.car_single_total + single_total
        p_exit.save()
        picture_id = Product_picture.objects.get(picture_foreKey=product).id
        return redirect("user:detail", picture_id)


# 删除购物车的物品
@valid_login
def cart_del(request, id):
    c = Car.objects.get(pk=id)
    c.delete()
    return redirect(reverse("user:cart"))


# 提交订单页面
@valid_login
def submit_order(request):
    # order_product 中添加数据
    username = request.session.get("username")
    user = User.objects.get(user_name=username)
    try:
        order = request.POST.get("order")
        order_list = str(order).split('"')
        num = 0
        op_list = []
        for i in range(1, len(order_list), 2):
            op_name = order_list[i]
            op_list.append(op_name)
            num += 1
            if num == 3:
                p_names = op_list[0]
                p_singpri = float(op_list[1])
                p_num = int(op_list[2])
                Order_Products.op_objects.op_create(p_names, p_num, p_singpri, user)
                OrdPro.orp_objects.orp_create(p_names, p_num, p_singpri, user)
                op_list = []
                num = 0
        s = json.dumps({"123": 123})
        return JsonResponse(s, safe=False)
    except:
        # print(123)
        return JsonResponse(json.dumps({"123": 123}), safe=False)


# detail 页面
def detail(request, id):
    username = request.session.get("username")
    if username:
        # 购物车物品数量
        car_total = Car.objects.all().count()
        # 产品详细页
        p = Product_picture.objects.get(pk=id)
        product = p.picture_foreKey
        s = p.picture_name[-1]
        # 推荐的新品
        recommend = Products.objects.filter(product_name__contains=s)
        # print(recommend)
        picture_recommend = Product_picture.objects.filter(picture_name__contains=s)
        # print(picture_recommend)
        content = {"picture": p, 'product': product, "recommend": recommend, "picture_list": picture_recommend,
                   'count': car_total, "valid": 1, "username": username}

    else:
        p = Product_picture.objects.get(pk=id)
        product = p.picture_foreKey
        s = p.picture_name[-1]
        # 推荐的新品
        recommend = Products.objects.filter(product_name__contains=s)
        # print(recommend)
        picture_recommend = Product_picture.objects.filter(picture_name__contains=s)
        # print(picture_recommend)
        content = {"picture": p, 'product': product, "recommend": recommend, "picture_list": picture_recommend,
                   "valid": 0, "username": username}
    return render(request, 'market_sys/detail.html', content)


# list 页面
def list(request):
    car_total = Car.objects.all().count()
    pic_list = Product_picture.objects.filter(picture_type=1)
    pro_list = Products.objects.all()
    username = request.session.get("username")
    pro_recommend = pic_list[0:5]
    if username:
        content = {"count": car_total, "valid": 1, "pic_list": pic_list, "pro_list": pro_list, "username": username,
                   'pro_recommend': pro_recommend}
        return render(request, 'market_sys/list.html', content)
    else:
        content = {"count": car_total, "pic_list": pic_list, "pro_list": pro_list, 'pro_recommend': pro_recommend}
        return render(request, 'market_sys/list.html', content)


# 最近浏览页面

def scan_adddata(request, pic_id):
    # print(pic_id)
    username = request.session.get("username")
    if username:
        pro_id = Product_picture.objects.get(pk=pic_id)
        username = request.session.get("username")
        user = User.objects.get(user_name=username)
        Scan.objects.scan_create(pro_id.picture_foreKey, user)
        return redirect("user:detail", pic_id)
    else:
        return redirect("user:detail", pic_id)


@valid_login
def scan_show(request):
    username = request.session.get("username")
    scan_pro = Scan.objects.filter(scan_user_foreignkey=username)[0:5]
    scan_pic = Product_picture.objects.all()
    return render(request, 'market_sys/user_center_info.html', {"scan_pro": scan_pro, "scan_pic": scan_pic})


# place_order 页面
@valid_login
def place_order(request):
    address = Address.objects.all()
    op_products = OrdPro.orp_objects.all()
    pictures = Product_picture.objects.all()
    products = Products.objects.all()
    username = request.session.get("username")
    total_spend = 0
    num = 0
    for each in op_products:
        total_spend = total_spend + float(each.orp_sing_price)
        num += 1
    post_spend = random.randint(1, 100)
    post_total = round(post_spend + total_spend, 2)
    total_spend1 = round(total_spend, 2)
    content = {"address": address, "op_products": op_products, 'products': products, "pictures": pictures, "num": num,
               "total_spend": total_spend1, "post_total": post_total, "post_spend": post_spend, "username": username,
               "valid": 1}
    return render(request, 'market_sys/place_order.html', content)
    # return HttpResponse("提交成功")


# 付款
@valid_login
def pay_order(request):
    import time
    address_id = request.GET.get("add")
    # print("address_id", address_id)
    username = request.session.get("username")
    # print('username', username)
    #  leiyh
    user = User.objects.get(user_name=username)
    # print("user", user)
    #  1--leiyh--12345678--18817380161@163.com--2018-06-20 23:47:08+00:00--False
    order_products = Order_Products.op_objects.filter(op_user_foreignkey=user)
    # print("产品名字：", order_products[0].op_name)
    total_spend = 0
    flag = False
    for i in range(len(order_products)):
        orp_name = order_products[i].op_name
        # print("产品名字：", orp_name)
        orp_num = order_products[i].op_num
        # print("产品数量：", orp_num)
        orp_sing_price = order_products[i].op_sing_price
        # print("产品单价：", orp_sing_price)
        orp_user_foreignkey = user
        # print("产品外键：", orp_user_foreignkey)
        #  1--leiyh--12345678--18817380161@163.com--2018-06-20 23:47:08+00:00--False
        total_spend = total_spend + float(orp_sing_price)
        # try:
        #     OrdPro.orp_objects.orp_create(orp_name, orp_num, orp_sing_price,
        #                                   user)
        #     flag = True
        # except Exception as msg:
        #     print("错误信息", msg)
        #     return HttpResponse("服务器正在维护，请稍后再试，谢谢！")
    if flag:
        order_No = int(time.time())
        # print("订单编号：", order_No)
        order_post_spend = 10
        order_total_spend = total_spend + 10
        # print("订单总花费：", order_total_spend)
        order_address_foreignkey = Address.objects.filter(address_foreignkey=user).get(pk=address_id)
        order_user_foreignkey = user
        Order.order_object.order_create(order_No, order_post_spend, order_total_spend, order_address_foreignkey,
                                        order_user_foreignkey)

        username = request.session.get("username")
        user = User.objects.get(user_name=username)
        omo_order_foreignkey = Order.order_object.filter(order_user_foreignkey=user).first()
        omo_ordPro_foreignkeys = OrdPro.orp_objects.filter(
            orp_user_foreignkey=user)  # ???????????????????????????????????????
        for each in omo_ordPro_foreignkeys:
            # print(each)
            Order_middle_Op.omo_objects.omo_create(omo_order_foreignkey, each)
        # content = {"count": car_total, "valid": "1", "username": username}
        # return render(request, 'market_sys/user_center_order.html', content)
        return redirect(reverse("user:finish_order"))


def finish_order(request):
    username = request.session.get("username")
    op_products = Order_Products.op_objects.all()
    print(op_products)
    products = Products.objects.all()
    user = User.objects.get(user_name=username)
    try:
        for each_product in op_products:
            p_name = Products.objects.get(product_name=each_product.op_name)
            car_finish_order = Car.objects.filter(car_product_foreignkey=p_name).filter(car_user_foreignkey=user)
            print('car_finish_order', car_finish_order)
            car_finish_order.delete()
            print("*******************************************")
        user_finish_pro = OrdPro.orp_objects.filter(orp_user_foreignkey=user)
        print("/////////////////////////////////////////////////////")
        user_finish_pro.delete()
        content = {"valid": "1", "username": username}
        return render(request, 'market_sys/user_center_order.html', content)
    except Exception as msg:
        user_finish_pro = OrdPro.orp_objects.filter(orp_user_foreignkey=user)
        user_finish_pro.delete()
        print('error:', msg)
        return HttpResponse("订单异常，请重新提交")


# 安全退出页面
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('user:index')
