from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url('^index/$', views.index, name="index"),

    # 登录页
    url(r"^loginpage/$", views.loginpage, name="loginpage"),
    url(r"^login/$", views.login, name="login"),

    # 注册
    url(r"^registpage/$", views.registpage, name="registpage"),
    url(r"^regist/$", views.regist, name="regist"),

    # 用户中心
    url(r"^user_center_site/$", views.user_center_site, name="user_center_site"),
    url(r"^add_address/$", views.add_address, name="add_address"),

    # 用户订单
    url(r"^user_center_order/$", views.user_center_order, name="user_center_order"),

    # 用户信息页
    url(r"^user_center_info/$", views.user_center_info, name="user_center_info"),

    # 购物车
    url(r"^cart_adddata/(\d{1,5})/$", views.cart_adddata, name="cart_adddata"),
    url(r"^cart/$", views.cart, name="cart"),
    url(r"^cart_update/$", views.cart_update, name="cart_update"),
    url(r"^cart_del/(\d{1,5})/$", views.cart_del, name="cart_del"),
    url(r"^submit_order/$", views.submit_order, name='submit_order'),

    # detail 页面
    url(r"^detail/(\d{1,5})/$", views.detail, name="detail"),

    # list 页面
    url(r"^list/$", views.list, name="list"),

    # scan
    url(r"^scan_adddata/(\d{1,5})/$", views.scan_adddata, name="scan_adddata"),

    # place_order 页面
    url(r"^place_order/$", views.place_order, name="place_order"),
    url(r"^pay_order/$", views.pay_order, name="pay_order"),
    # url(r"^coperation/$", views.coperation, name="coperation"),

    # 完成订单
    url(r"^finish_order/$", views.finish_order, name="finish_order"),

    # 安全退出
    url(r"^logout/$", views.logout, name="logout"),
]
