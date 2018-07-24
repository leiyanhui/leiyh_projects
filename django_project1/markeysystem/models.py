from django.db import models
from datetime import datetime


# Create your models here.

# 用户户管理对象
class User_Form_Manage(models.Manager):
    # 定义获取数据的筛选方式
    def get_queryset(self):
        return super(User_Form_Manage, self).get_queryset().filter(user_isDelete=False)

    # 定义插入数据的方式
    def user_create(self, user_No, user_name, user_password, user_gender, user_age, user_phone, user_address, job_type):
        create_in = self.create(user_No=user_No, user_name=user_name, user_password=user_password,
                                user_gender=user_gender, user_age=user_age, user_phone=user_phone,
                                user_address=user_address, job_type=job_type)
        create_in.user_isDelete = False
        return create_in


# 用户管理表
class User_Form(models.Model):
    user_No = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=20, null=True)
    user_password = models.CharField(max_length=10, null=True)
    user_gender = models.BooleanField(default=True)
    user_age = models.IntegerField()
    user_phone = models.IntegerField()
    user_address = models.CharField(max_length=4000)
    user_isDelete = models.BooleanField(default=False)
    job_type = models.BooleanField(default=False)
    user_objects = User_Form_Manage()

    # False表示普通员工
    class Meta():
        db_table = "_user"
        ordering = ['id']

    def __str__(self):
        return "%d--%d--%s--%s--%s--%d--%d--%s--%s" % (
            self.id, self.user_No, self.user_name, self.user_password, self.user_gender, self.user_age, self.user_phone,
            self.user_address, self.job_type)

# 账单信息管理器
class Bill_Form_Manage(models.Manager):
    def get_querryset(self):
        return super(Bill_Form_Manage,self).get_queryset().filter(bill_isDelete=False)

    def bill_create(self,bill_No, bill_goods_name, bill_goods_num, bill_goods_money, bill_spend, bill_goods_des, bill_goods_supplier):
        create_in = self.create(bill_No=bill_No, bill_goods_name=bill_goods_name, bill_goods_num=bill_goods_num, bill_goods_money=bill_goods_money,bill_spend=bill_spend, bill_goods_des=bill_goods_des, bill_goods_supplier=bill_goods_supplier, bill_finish_time =datetime.now(), bill_isDelete=False)
        return create_in

# 账单信息表
class Bill_Form(models.Model):
    bill_No=models.CharField(max_length=20,unique=True)
    bill_goods_name=models.CharField(max_length=20)
    bill_goods_num=models.IntegerField()
    bill_goods_money=models.FloatField()
    bill_spend=models.BooleanField(default=True)
    bill_goods_des=models.CharField(max_length=4000)
    bill_goods_supplier=models.ForeignKey("Supplier_Form")
    bill_finish_time=models.DateTimeField(datetime.now())
    bill_isDelete=models.BooleanField(default=False)
    bill_objects = Bill_Form_Manage()

    def __str__(self):
        return "%d--%s--%s--%d--%d--%s--%s--%s--%s--%s" % (
            self.id, self.bill_No, self.bill_goods_name, self.bill_goods_num, self.bill_goods_money, self.bill_spend, self.bill_goods_des,
            self.bill_goods_supplier, self.bill_finish_time, self.bill_isDelete)

# 供应商管理对象
class Supplier_Form_Manage(models.Manager):
    # 定义获取数据的筛选方式
    def get_queryset(self):
        return super(Supplier_Form_Manage, self).get_queryset().filter(supplier_isDelete=False)
    # 定义添加供应商的方式
    def supplier_create(self, supplier_No, supplier_info, supplier_des, supplier_name, supplier_phone, supplier_address ):
        create_in = self.create(supplier_No=supplier_No, supplier_info=supplier_info,supplier_des=supplier_des,supplier_name=supplier_name, supplier_phone=supplier_phone,supplier_address=supplier_address)
        create_in.supplier_isDelete=False
        return create_in

# 供应商管理表
class Supplier_Form(models.Model):
    supplier_No = models.IntegerField(unique=True)
    supplier_info = models.CharField(max_length=20, null=True)
    supplier_des = models.CharField(max_length=4000)
    supplier_name = models.CharField(max_length=20, null=True)
    supplier_phone = models.IntegerField()
    supplier_address = models.CharField(max_length=4000)
    supplier_isDelete = models.BooleanField(default=False)
    supplier_objects = Supplier_Form_Manage()

    class Meta():
        db_table = "_supplier"
        ordering = ['id']

    def __str__(self):
        return "%d--%d--%s--%s--%s--%d--%s"%(self.id, self.supplier_No, self.supplier_info, self.supplier_des, self.supplier_name, self.supplier_phone, self.supplier_address)

