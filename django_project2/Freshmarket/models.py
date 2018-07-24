from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from django.conf import settings
import os


# Create your models here.

# 用户信息表1

class UserManage(models.Manager):

    def get_queryset(self):
        return super(UserManage, self).get_queryset().filter(user_isDelete=False)

    def user_create(self, user_name, user_pwd, user_email):
        create_in = self.create(user_name=user_name, user_pwd=user_pwd, user_email=user_email,
                                user_crate_time=datetime.now())
        create_in.user_isDelete = False
        return create_in


class User(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    user_pwd = models.CharField(max_length=20)

    user_email = models.EmailField()

    user_crate_time = models.DateTimeField(datetime.now())
    user_isDelete = models.BooleanField(default=False)
    objects = UserManage()

    class Meta():
        ordering = ["-id"]
        db_table = "User"

    def __str__(self):
        return "%d--%s--%s--%s--%s--%s" % (
            self.id, self.user_name, self.user_pwd, self.user_email, self.user_crate_time, self.user_isDelete)


# 产品信息表2

class ProductManage(models.Manager):
    def get_queryset(self):
        return super(ProductManage, self).get_queryset().filter(product_isDelete=False)

    def product_create(self, product_name, product_num, product_price, product_desc):
        create_in = self.create(product_name=product_name, product_num=product_num, product_price=product_price,
                                product_desc=product_desc)
        create_in.product_create_time = datetime.now()
        create_in.product_isDelete = False
        return create_in


class Products(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    product_num = models.IntegerField()
    product_price = models.FloatField()
    product_desc = models.CharField(max_length=255)
    product_crate_time = models.DateTimeField(datetime.now())
    product_isDelete = models.BooleanField(default=False)
    objects = ProductManage()

    class Meta():
        ordering = ["-id"]
        db_table = "Products"

    def __str__(self):
        return "%d--%s--%d--%f--%s--%s--%s" % (
            self.id, self.product_name, self.product_num, self.product_price, self.product_desc,
            self.product_crate_time,
            self.product_isDelete)


# 产品照片
class Product_pictureManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(picture_isDelete=False)


class Product_picture(models.Model):
    picture_name = models.CharField(max_length=50, )
    picture_icron = models.ImageField(upload_to='img/')
    picture_type = models.IntegerField()
    picture_datetime = models.DateTimeField(datetime.now())
    picture_foreKey = models.ForeignKey('Products', on_delete=models.CASCADE)
    picture_isDelete = models.BooleanField(default=False)
    objects = Product_pictureManage()

    # 1 代表水果，2 代表海鲜
    class Meta():
        db_table = "Picture"
        ordering = ['-id']

    def __str__(self):
        return "%d--%s--%s--%s--%d--%s" % (
            self.id, self.picture_name, self.picture_icron, self.picture_datetime, self.picture_type,
            self.picture_foreKey)

    def icon_img(self):
        return mark_safe("<img src='%s' width=100px;/>" % os.path.join(settings.MEDIA_ROOT, self.picture_icron.name))


# 最近浏览信息表3
class ScanMange(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(scan_isDelete=False)

    def scan_create(self, scan_products_foreignkey, scan_user_foreignkey):
        create_in = self.create(scan_products_foreignkey=scan_products_foreignkey,
                                scan_user_foreignkey=scan_user_foreignkey, scan_datatime=datetime.now())
        create_in.scan_isDelete = False
        return create_in


class Scan(models.Model):
    scan_isDelete = models.BooleanField(default=False)
    scan_products_foreignkey = models.ForeignKey("Products", on_delete=models.CASCADE)
    scan_user_foreignkey = models.ForeignKey("User", on_delete=models.CASCADE)
    scan_datatime = models.DateTimeField(datetime.now())
    objects = ScanMange()

    def __str__(self):
        return "%d--%s--%s--%s--%s" % (
            self.id, self.scan_isDelete, self.scan_products_foreignkey, self.scan_user_foreignkey, self.scan_datatime)

    class Meta():
        ordering = ["-id"]
        db_table = "Scan"


# 购物车表4
class Car_Manage(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(car_isDelete=False)

    def car_create(self, car_num, car_product_foreignkey, car_user_foreignkey, car_single_total):
        create_in = self.create(car_num=car_num, car_product_foreignkey=car_product_foreignkey,
                                car_user_foreignkey=car_user_foreignkey, car_single_total=car_single_total)
        create_in.car_datetime = datetime.now()
        create_in.scan_isDelete = False
        return create_in


class Car(models.Model):
    car_isDelete = models.BooleanField(default=False)
    car_num = models.IntegerField()
    car_product_foreignkey = models.ForeignKey("Products", unique=True, on_delete=models.CASCADE)
    car_user_foreignkey = models.ForeignKey("User", on_delete=models.CASCADE)
    car_single_total = models.FloatField()
    car_datetime = models.DateTimeField(default=datetime.now())

    objects = Car_Manage()

    def __str__(self):
        return "%d--%s--%d--%s--%s--%s--%d" % (
            self.id, self.car_num, self.car_isDelete, self.car_product_foreignkey, self.car_user_foreignkey,
            self.car_datetime, self.car_single_total)

    class Meta():
        db_table = "Car"
        ordering = ["-id"]


# 地址表5

class Address_Manage(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(address_isDelete=False)

    def add_create(self, address_address, address_name, address_phone, address_foreignkey):
        create_in = self.create(address_address=address_address, address_name=address_name, address_phone=address_phone,
                                address_foreignkey=address_foreignkey, address_datetime=datetime.now())
        create_in.product_isDelete = False
        return create_in


class Address(models.Model):
    address_address = models.CharField(max_length=255, default=False)
    address_name = models.CharField(max_length=20)
    address_phone = models.IntegerField()
    address_datetime = models.DateTimeField(datetime.now())
    address_foreignkey = models.ForeignKey("User", related_name="+", on_delete=models.CASCADE)
    address_isDelete = models.BooleanField(default=False)
    objects = Address_Manage()

    def __str__(self):
        return "%d--%s--%s--%d--%s--%s--%s" % (
            self.id, self.address_address, self.address_name, self.address_phone, self.address_datetime,
            self.address_foreignkey, self.address_isDelete)

    class Meta():
        db_table = "Address"
        ordering = ['-id']


# 订单表

class Order_Manage(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(order_isDelete=False)

    def order_create(self, order_No, order_post_spend, order_total_spend, order_address_foreignkey,
                     order_user_foreignkey):
        create_in = self.create(order_No=order_No, order_post_spend=order_post_spend,
                                order_total_spend=order_total_spend, order_address_foreignkey=order_address_foreignkey,
                                order_user_foreignkey=order_user_foreignkey, order_datetime=datetime.now())
        create_in.order_status = False
        create_in.product_isDelete = False
        return create_in


class Order(models.Model):
    order_No = models.CharField(max_length=20, unique=True)
    order_post_spend = models.FloatField()
    order_total_spend = models.FloatField()
    order_status = models.BooleanField(default=False)
    order_address_foreignkey = models.ForeignKey("Address", related_name="+", on_delete=models.CASCADE)
    order_user_foreignkey = models.ForeignKey("User", related_name="+", on_delete=models.CASCADE)
    order_datetime = models.DateTimeField(datetime.now())
    order_isDelete = models.BooleanField(default=False)
    order_object = Order_Manage()

    class Meta():
        db_table = "Order"
        ordering = ["-id"]

    def __str__(self):
        return "%d--%s--%.2f--%.2f--%s--%s--%s--%s--%s" % (
            self.id, self.order_No, self.order_post_spend, self.order_total_spend, self.order_status,
            self.order_address_foreignkey, self.order_user_foreignkey,
            self.order_datetime, self.order_isDelete)

    # 购物车订单中间过渡表


class Order_PManage(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def op_create(self, op_name, op_num, op_sing_price, op_user_foreignkey):
        create_in = self.create(op_name=op_name, op_num=op_num, op_sing_price=op_sing_price,
                                op_user_foreignkey=op_user_foreignkey)
        return create_in


class Order_Products(models.Model):
    op_name = models.CharField(max_length=254)
    op_num = models.IntegerField()
    op_sing_price = models.FloatField()
    op_user_foreignkey = models.ForeignKey("User", on_delete=models.CASCADE)
    op_objects = Order_PManage()

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return "%d--%s--%d--%f--%s" % (self.id, self.op_name, self.op_num, self.op_sing_price, self.op_user_foreignkey)


# 订单物品表

class OrPManage(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def orp_create(self, orp_name, orp_num, orp_sing_price, orp_user_foreignkey):
        create_in = self.create(orp_name=orp_name, orp_num=orp_num, orp_sing_price=orp_sing_price,
                                orp_user_foreignkey=orp_user_foreignkey)
        return create_in


class OrdPro(models.Model):
    orp_name = models.CharField(max_length=254)
    orp_num = models.IntegerField()
    orp_sing_price = models.FloatField()
    orp_user_foreignkey = models.ForeignKey("User", on_delete=models.CASCADE)
    orp_objects = OrPManage()

    class Meta():
        ordering = ['-id']

    def __str__(self):
        return "%d--%s--%d--%f--%s" % (
            self.id, self.orp_name, self.orp_num, self.orp_sing_price, self.orp_user_foreignkey)


# 订单与物品中间表
class Order_middle_OpManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def omo_create(self, omo_order_foreignkey, omo_ordPro_foreignkey):
        create_in = self.create(omo_order_foreignkey=omo_order_foreignkey, omo_ordPro_foreignkey=omo_ordPro_foreignkey)
        return create_in


class Order_middle_Op(models.Model):
    omo_order_foreignkey = models.ForeignKey("Order", on_delete=models.CASCADE)
    omo_ordPro_foreignkey = models.ForeignKey("OrdPro", on_delete=models.CASCADE)

    omo_objects = Order_middle_OpManage()

    def __str__(self):
        return "%d--%s--%s" % (self.id, self.omo_order_foreignkey, self.omo_ordPro_foreignkey)
