# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class Account(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    memberid = models.ForeignKey(
        'Member', models.DO_NOTHING, db_column='memberID')
    # Field name made lowercase.
    Permissionid = models.ForeignKey(
        'Permission', models.DO_NOTHING, db_column='PermissionID')
    # Field name made lowercase.
    username = models.CharField(
        db_column='Username', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    password = models.CharField(
        db_column='Password', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'account'


class Address(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)

    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    district = models.CharField(
        db_column='District', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    ward = models.CharField(
        db_column='Ward', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(
        db_column='Address', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'address'


class Bank(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    logo = models.CharField(
        db_column='Logo', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'bank'


class Bill(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    orderid = models.ForeignKey(
        'Order', models.DO_NOTHING, db_column='OrderID')
    # Field name made lowercase.
    company = models.CharField(
        db_column='Company', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tax_code = models.CharField(
        db_column='Tax_code', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(
        db_column='Address', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'bill'


class Book(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    publisher = models.CharField(
        db_column='Publisher', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    published_date = models.DateField(
        db_column='Published_date', blank=True, null=True)
    # Field name made lowercase.
    size = models.CharField(
        db_column='Size', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cover = models.CharField(
        db_column='Cover', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    pages = models.IntegerField(db_column='Pages', blank=True, null=True)
    # Field name made lowercase.
    released_company = models.CharField(
        db_column='Released_company', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'book'


class BussinessStaff(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    memberid = models.ForeignKey(
        'Member', models.DO_NOTHING, db_column='memberID')

    class Meta:

        db_table = 'bussiness_staff'


class Cart(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    orderid = models.ForeignKey(
        'Order', models.DO_NOTHING, db_column='OrderID')
    customerid = models.ForeignKey(
        'Customer', models.DO_NOTHING, db_column='CustomerID', null=True)
    # Field name made lowercase. This field type is a guess.
    is_order = models.TextField(db_column='Is_order')

    class Meta:

        db_table = 'cart'


class CartItem(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    cartid = models.ForeignKey(
        Cart, on_delete=models.CASCADE, db_column='CartID')
    # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID')
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.

    class Meta:

        db_table = 'cart_item'


class Category(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'category'


class CategoryProduct(models.Model):
    # Field name made lowercase.
    categoryid = models.OneToOneField(
        Category, models.DO_NOTHING, db_column='CategoryID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')

    class Meta:

        db_table = 'category_product'
        unique_together = (('categoryid', 'productid'),)


class Clothes(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    material = models.CharField(
        db_column='Material', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    brand = models.CharField(
        db_column='Brand', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    origin = models.CharField(
        db_column='Origin', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    color = models.CharField(
        db_column='Color', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'clothes'


class ClothesColor(models.Model):
    # Field name made lowercase.
    clothesid = models.OneToOneField(
        Clothes, models.DO_NOTHING, db_column='ClothesID', primary_key=True)
    # Field name made lowercase.
    colorid = models.IntegerField(db_column='ColorID')

    class Meta:

        db_table = 'clothes_color'
        unique_together = (('clothesid', 'colorid'),)


class ClothesSize(models.Model):
    # Field name made lowercase.
    clothesid = models.OneToOneField(
        Clothes, models.DO_NOTHING, db_column='ClothesID', primary_key=True)
    # Field name made lowercase.
    sizeid = models.ForeignKey('Size', models.DO_NOTHING, db_column='SizeID')

    class Meta:

        db_table = 'clothes_size'
        unique_together = (('clothesid', 'sizeid'),)


class Comment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    content = models.CharField(
        db_column='Content', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    updated_date = models.DateTimeField(
        db_column='Updated_date', default=datetime.now, blank=True)

    class Meta:

        db_table = 'comment'


class Customer(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    memberid = models.ForeignKey(
        'Member', models.DO_NOTHING, db_column='memberID')

    class Meta:

        db_table = 'customer'


class DeliveryAddress(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    orderid = models.ForeignKey(
        'Order', models.DO_NOTHING, db_column='OrderID')
    # Field name made lowercase.
    addressid = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='AddressID')
    # Field name made lowercase.
    customerid = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='CustomerID')
    # Field name made lowercase.
    receiver = models.CharField(
        db_column='Receiver', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'delivery_address'


class Discount(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID')
    # Field name made lowercase.
    discount_value = models.FloatField(db_column='Discount_value')
    # Field name made lowercase.
    from_date = models.DateTimeField(
        db_column='From_date', blank=True, null=True)
    # Field name made lowercase.
    to_date = models.DateTimeField(db_column='To_date', blank=True, null=True)

    class Meta:

        db_table = 'discount'


class Electro(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    brand = models.CharField(
        db_column='Brand', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    model = models.CharField(
        db_column='Model', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    origin = models.CharField(
        db_column='Origin', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    size = models.CharField(
        db_column='Size', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    color = models.CharField(
        db_column='Color', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'electro'


class ElectroColor(models.Model):
    # Field name made lowercase.
    electroid = models.OneToOneField(
        Electro, models.DO_NOTHING, db_column='ElectroID', primary_key=True)
    # Field name made lowercase.
    colorid = models.IntegerField(db_column='ColorID')

    class Meta:

        db_table = 'electro_color'
        unique_together = (('electroid', 'colorid'),)


class Event(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    from_date = models.DateTimeField(
        db_column='From_date', blank=True, null=True)
    # Field name made lowercase.
    to_date = models.DateTimeField(db_column='To_date', blank=True, null=True)

    class Meta:

        db_table = 'event'


class Feedback(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.DO_NOTHING, db_column='ItemID')
    # Field name made lowercase.
    commentid = models.ForeignKey(
        Comment, models.DO_NOTHING, db_column='CommentID')
    # Field name made lowercase.
    liked = models.IntegerField(db_column='Liked')
    # Field name made lowercase.
    rate_score = models.IntegerField(db_column='Rate_score')
    # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column='Created_date', default=datetime.now, blank=True)

    class Meta:

        db_table = 'feedback'


class Image(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    caption = models.CharField(
        db_column='Caption', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    path = models.CharField(
        db_column='Path', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'image'


class ImportFile(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column='Created_date', default=datetime.now, blank=True)

    class Meta:

        db_table = 'import_file'


class ImportProduct(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    import_fileid = models.ForeignKey(
        ImportFile, models.DO_NOTHING, db_column='Import_fileID')
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.

    class Meta:

        db_table = 'import_product'


class Item(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        'Product', models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    price = models.CharField(
        db_column='Price', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'item'


class Member(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)

    addressid = models.ForeignKey(
        Address, models.DO_NOTHING, db_column='AddressID')
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dob = models.DateField(db_column='Dob', blank=True, null=True)
    # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender')
    # Field name made lowercase.
    avatar = models.CharField(
        db_column='Avatar', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'member'


class Order(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    shipmentid = models.ForeignKey(
        'Shipment', models.DO_NOTHING, db_column='ShipmentID')
    # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column='Created_date', default=datetime.now, blank=True)

    class Meta:

        db_table = 'order'


class OrderHistory(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    saler_staffid = models.ForeignKey(
        'SalerStaff', models.DO_NOTHING, db_column='Saler_staffID')
    # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')
    # Field name made lowercase.
    status = models.CharField(
        db_column='Status', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)

    class Meta:

        db_table = 'order_history'


class Payment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    paymentmethodid = models.ForeignKey(
        'PaymentMethod', models.DO_NOTHING, db_column='PaymentMethodID')
    # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')

    class Meta:

        db_table = 'payment'


class PaymentDetail(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    customerid = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='CustomerID')
    # Field name made lowercase.
    bankid = models.ForeignKey(Bank, models.DO_NOTHING, db_column='bankID')
    # Field name made lowercase.
    card = models.CharField(
        db_column='Card', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'payment_detail'


class PaymentMethod(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    method_name = models.CharField(
        db_column='Method_name', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'payment_method'


class PaymentmethodBank(models.Model):
    # Field name made lowercase.
    paymentmethodid = models.OneToOneField(
        PaymentMethod, models.DO_NOTHING, db_column='PaymentMethodID', primary_key=True)
    # Field name made lowercase.
    bankid = models.ForeignKey(Bank, models.DO_NOTHING, db_column='bankID')

    class Meta:

        db_table = 'paymentmethod_bank'
        unique_together = (('paymentmethodid', 'bankid'),)


class Permission(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)

    # Field name made lowercase.
    level = models.IntegerField(db_column='Level')
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'permission'


class Product(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    warehouseid = models.ForeignKey(
        'Warehouse', models.DO_NOTHING, db_column='WarehouseID')
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    qty_in_stock = models.IntegerField(db_column='Qty_in_stock')

    class Meta:

        db_table = 'product'


class Respone(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    commentid = models.ForeignKey(
        Comment, models.DO_NOTHING, db_column='CommentID')
    # Field name made lowercase.
    content = models.CharField(
        db_column='Content', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    created_date = models.DateTimeField(
        db_column='Created_date', blank=True, null=True)
    # Field name made lowercase.
    updated_date = models.DateTimeField(
        db_column='Updated_date', default=datetime.now, blank=True)

    class Meta:

        db_table = 'respone'


class SalerStaff(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    memberid = models.ForeignKey(
        Member, models.DO_NOTHING, db_column='memberID')

    class Meta:

        db_table = 'saler_staff'


class Shipment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    shipperid = models.ForeignKey(
        'Shipper', models.DO_NOTHING, db_column='ShipperID')
    fee = models.FloatField(db_column='Fee')  # Field name made lowercase.

    class Meta:

        db_table = 'shipment'


class ShipmentMethod(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    shipmentid = models.ForeignKey(
        Shipment, models.DO_NOTHING, db_column='ShipmentID')
    # Field name made lowercase.
    method_name = models.CharField(
        db_column='Method_name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')
    fee = models.FloatField(db_column='Fee')  # Field name made lowercase.

    class Meta:

        db_table = 'shipment_method'


class Shipper(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    memberid = models.ForeignKey(
        Member, models.DO_NOTHING, db_column='memberID')

    class Meta:

        db_table = 'shipper'


class Shop(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    logo = models.CharField(
        db_column='Logo', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(
        db_column='Address', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    desc = models.CharField(
        db_column='Desc', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'shop'


class Size(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    size = models.CharField(
        db_column='Size', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    weight = models.FloatField(db_column='Weight')

    class Meta:

        db_table = 'size'


class Tax(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    productid = models.ForeignKey(
        Product, models.DO_NOTHING, db_column='ProductID')
    # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=255,
                          blank=True, null=True)
    # Field name made lowercase.
    value = models.CharField(
        db_column='Value', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'tax'


class Warehouse(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'warehouse'


class WarehouseStaff(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    import_fileid = models.ForeignKey(
        ImportFile, models.DO_NOTHING, db_column='Import_fileID')
    # Field name made lowercase.
    memberid = models.ForeignKey(
        Member, models.DO_NOTHING, db_column='memberID')

    class Meta:

        db_table = 'warehouse_staff'


class Notification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    customerid = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, db_column="customerID")
    content = models.CharField(db_column='content', max_length=255, blank=True, null=True
                               )
    time = models.DateTimeField(db_column='time', null=True, blank=True)

    class Meta:

        db_table = 'notification'