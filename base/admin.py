from django.contrib import admin

# Register your models here.
from .models import Product
from .models import categories
from .models import orders
from .models import orderDetail
from .models import profile
from .models import User

admin.site.register(Product)
admin.site.register(categories)
admin.site.register(orderDetail)
admin.site.register(orders)
admin.site.register(profile)
