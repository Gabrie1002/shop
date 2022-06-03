from django.db import models


POSITIONS = (
    ('left', u'картинка слева'),
    ('right', u'картинка справа')
)


class Page(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', blank=True, null=True, unique=True)

    def __str__(self):
        return self.title


class PageInLine(models.Model):
    title = models.CharField('title', max_length=255)
    page = models.ForeignKey(Page, related_name='page_page_items', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='page')
    text = models.TextField('text')
    url = models.URLField('url', blank=True, null=True)
    position = models.CharField('position', max_length=255, choices=POSITIONS)

    def __str__(self):
        return self.page.title


class Slide(models.Model):
    title = models.CharField('title', max_length=255)
    ordering = models.IntegerField('ordering', default=0)
    image = models.ImageField('image', upload_to='slider')
    text = models.TextField('text')
    button_text = models.CharField('button_text', max_length=255)
    button_link = models.URLField('button_link')
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk', ]
