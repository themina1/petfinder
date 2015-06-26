from django.contrib import admin
from .models import CommonInfo
from .models import Dog
from .models import Cat
from .models import UniqueAnimal

# Register your models here.
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(UniqueAnimal)