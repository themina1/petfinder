from django.contrib import admin
from .models import CommonInfo
from .models import Dog
from .models import Cat
from .models import Unique

# Register your models here.
admin.site.register(CommonInfo)
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(Unique)