from django.contrib import admin
from .models import Animal, RedditPost

# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    #To make the contact info into a collapseable box.
    fieldsets = ((None,{'fields': ('animal','petId','firstSeen','lastSeen', 'petName','petDescription','petBreed',
                                   'petStatus', 'petAge', 'petSex','petSize', 'petMix', 'petFeatures','petPhoto' )}),
                 ('Contact Info', {'classes': ('collapse',), 'fields':('address','city','email','fax','phone',
                                                                       'state','zip')
                                   }
                  ))
    # To display Id Animal and Name in a list view.
    list_display = ('petId','animal','petName','petStatus')
    list_filter = ['animal', 'petStatus']
    search_field = ['petId']
class RedditPostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'up_votes')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(RedditPost, RedditPostAdmin)