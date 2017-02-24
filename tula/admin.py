from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import *


class DropdownInLine(admin.TabularInline):
    model = DropdownMenu
    extra = 0


class PhotosInline(admin.TabularInline):
    model = Photo
    extra = 0
    fields = ['show_title', 'title', 'description', 'image', 'order']
    readonly_fields = ['show_title']
    exclude = []
    verbose_name = ''

    def show_title(self, obj):
        url = reverse('admin:tula_photo_change', args=[obj.id])
        return mark_safe('<a href="%s" class="" >%s</a>' % (url, obj.__str__()))

    show_title.allow_tags = True


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter = ['holiday']
    model = Photo
    readonly_fields = ['thumb_image', 'show_holiday', 'go_to_gallery']
    list_display = ('__str__', 'description', 'thumb_image', 'show_holiday')
    fieldsets = (
        (
            None, {'fields': ('title', 'description', 'image', 'order', 'go_to_gallery')},
        ),
    )

    def show_holiday(self, obj):
        return '<a href="%s">"%s"</a>' % (reverse("admin:tula_holiday_change", args=[obj.holiday.id]), obj.holiday.title)

    show_holiday.allow_tags = True

    def go_to_gallery(self, obj):
        return '<a href="%s">"%s"</a>' % (reverse('admin:tula_holiday_change', args=[obj.holiday.id]), obj.holiday.title)

    go_to_gallery.allow_tags = True

    def thumb_image(self, obj):
        return '<a href="%s"><img src="/assets/%s" style="margin-right:5px;border:solid 1px black" /></a>' % (reverse('admin:tula_photo_change', args=[obj.id]), obj.image.version_generate('medium'))

    thumb_image.allow_tags = True

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    model = Holiday
    inlines = (PhotosInline,)
    list_display = ['__str__', 'mainimg_thumb', 'photos_thumbs']
    readonly_fields = ['photos_thumbs', 'mainimg_thumb']

    def mainimg_thumb(self, obj):
        if obj.mainimg:
            return '<a href="%s"><img style="margin-right:5px;border:solid 1px black" src="/assets/%s"></a>' % (reverse('admin:tula_photo_change', args=[obj.id]), obj.mainimg.version_generate('medium'))

    mainimg_thumb.allow_tags = True

    def photos_thumbs(self, obj):
        html = ''
        for p in obj.photos():
            html += '<a href="%s"><img style="margin-right:5px;border:solid 1px black" src="/assets/%s" /></a>' % (reverse('admin:tula_photo_change', args=[p.id]), p.image.version_generate('small'))
        return mark_safe(html)

    photos_thumbs.allow_tags = True


@admin.register(NavMenu)
class NavMenuAdmin(admin.ModelAdmin):
    model = NavMenu
    list_display = ['title', 'url', 'get_caption', 'order']
    inlines = [DropdownInLine, ]


# @admin.register(Ivent)
# class IventAdmin(admin.ModelAdmin):
#     model = Ivent

class IventInline(admin.StackedInline):
    model = Ivent
    extra = 1
    exclude = []


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    model = History
    inlines = [IventInline, ]


@admin.register(Trust_Us)
class Trust_Us_Admin(admin.ModelAdmin):
    model = Trust_Us
    readonly_fields = ['show_logo']
    list_display = ['__str__', 'show_logo']
    list_filter = ['logo', ]

    def show_logo(self, obj):
        if obj.logo:
            return '<img style="margin-right:5px;border:solid 1px black" src="/assets/%s">' % (obj.logo.version_generate('small'), )
        else:
            return None

    show_logo.allow_tags = True
