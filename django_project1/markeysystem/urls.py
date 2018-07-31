from django.conf.urls import url
from . import views


urlpatterns = [

    # 登录
    url(r"^loginpage/$", views.loginpage, name="loginpage"),
    url(r"^login/$", views.login, name="login"),
    url( r"^loginsucess/$", views.loginsucess,name='loginsucess'),
    # 主页合成

    # 用户账单操作
    url( r"^admin_bill_list/$", views.admin_bill_list,name='admin_bill_list'),
    url( r"^addbill/$", views.addbill,name='addbill'),
    url( r"^addbillpre/$", views.addbillpre,name='addbillpre'),
    url( r"^modify/$", views.modify,name='modify'),
    url(r'^bill_getdata/(\d)+/$',views.bill_getdata, name='bill_getdata'),
    url(r'^bill_update/$',views.bill_update, name='bill_update'),

    url( r"^admin_letf/$", views.admin_left,name='admin_left'),
    url( r"^admin_top/$", views.admin_top,name='admin_top'),

    # 供应商操作
    url( r"^providerAddpre/$", views.providerAddpre,name='providerAddpre'),
    url( r"^providerAdd/$", views.providerAdd,name='providerAdd'),
    url( r"^provider_getdata/(\d)+/$", views.provider_getdata,name='provider_getdata'),
    url( r"^providermodefy/$", views.providermodefy,name='providermodefy'),
    url( r"^providerAdmin/$", views.providerAdmin,name='providerAdmin'),

    # 用户操作
    url(r"^userAddpre/$", views.userAddpre, name='userAddpre'),
    url( r"^userAdd/$", views.userAdd,name='userAdd'),
    url( r"^user_getdata/(\d)+/$", views.user_getdata,name='user_getdata'),
    url( r"^user_modefy/$", views.user_modefy,name='user_modefy'),
    url( r"^userAdmin/$", views.userAdmin,name='userAdmin'),


    # 安全退出
    url(r"^logouting/$", views.logouting, name='logouting'),


]