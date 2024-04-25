from django.contrib import admin
from . models import Cart, Customer, OrderPlaced, Payment, product

# Register your models here.
@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title' , 'selling_price', 'discounted_price' , 'description' , 'height' , 'weight' , 'breadName',  'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality', 'city', 'state' , 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user', 'product', 'quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'amount' , 'razorpay_order_id' , 'razorpay_payment_status', 'razorpay_payment_id' , 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user', 'customer' , 'product' , 'quantity' , 'ordered_date' , 'status' , 'payment']