from django.db import models
from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField
from imagekit.models import ImageSpecField


class NavMenu(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=128)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    caption = models.CharField(max_length=32, blank=True, null=True, default='')

    def get_caption(self):
        if self.caption == '':
            return self.title
        else:
            return self.caption

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return '%s' % (self.title, )

    def dropdowns(self):
        return DropdownMenu.objects.filter(navmenu=self)


class DropdownMenu(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=128)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    navmenu = models.ForeignKey(NavMenu)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return 'Dropdown - %s' % (self.title, )


class Holiday(models.Model):
    title = models.CharField(max_length=32)
    caption = models.CharField(max_length=32, blank=True, null=True, default='')
    article = models.TextField(max_length=1024)
    special_offer = models.TextField(max_length=256, blank=False, null=False, default='')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    mainimg = FileBrowseField('MainImage',  max_length=200, directory="holidays", extensions=['.jpg', '.jpeg', '.gif', '.png', '.bmp'], blank=True, null=True)
    url = models.CharField(max_length=64, blank=False, null=False, default='')
    first = models.BooleanField(default=False)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return 'Holiday-%s: %s' % (self.order, self.title,)

    def photos(self):
        return Photo.objects.filter(holiday=self)


class Photo(models.Model):
    title = models.CharField(max_length=32, default='', blank=True, null=True)
    description = models.TextField(max_length=1024, default='', blank=True, null=True)
    image = FileBrowseField('image', max_length=200, directory="holidays", extensions=['.jpg', '.jpeg', '.gif', '.png', '.bmp'], blank=True, null=True)
    holiday = models.ForeignKey(Holiday)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return 'Photo-%s: %s' % (self.order, self.title, )

    def get_slide_url(self):
        return self.image.version_generate('large')


class Trust_Us(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512, blank=True, null=True)
    logo = FileBrowseField('logo', max_length=200, directory="trusts/logos", extensions=['.jpg', '.jpeg', '.gif', '.png', '.bmp'], blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.name

    def get_logo_url(self):
        return self.logo.version_generate('small')

    def get_box_url(self):
        return self.logo.version_generate('large')


class History(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    date = models.DateField()

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return 'History | %s' % (self.date.strftime('%Y %M'))

    def get_ivents(self):
        return Ivent.objects.filter(history=self)


class Ivent(models.Model):
    title = models.CharField(max_length=128)
    article = models.CharField(max_length=512, blank=True, null=True)
    history = models.ForeignKey(History)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return '%s - %s' % (self.history.date.strftime('%Y %M'), self.title, )
