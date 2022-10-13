from django.contrib import admin
from .models import Photo, Fishing, PartnerLink, Shop
from django.utils.html import format_html


class FishingAdmin(admin.ModelAdmin):
    list_display = ['description', 'trophies', 'latitude', 'longitude', 'publication_date', 'tackle', 'bait', 'boat', 'motor'] # то, что отображается в админке
    list_filter = ['publication_date'] # возможность фильтроавть по данной позиции
    

class PartnerLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'publication_date'] # то, что отображается в админке
    list_filter = ['publication_date'] # возможность фильтроавть по данной позиции
    

class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'publication_date'] # то, что отображается в админке
    list_filter = ['publication_date'] # возможность фильтроавть по данной позиции

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['path', 'publication_date'] # то, что отображается в админке
    list_filter = ['publication_date'] # возможность фильтроавть по данной позиции

    def path_tag(self,obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.path.url))
    
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Fishing, FishingAdmin)
admin.site.register(PartnerLink, PartnerLinkAdmin)
admin.site.register(Shop, ShopAdmin)


