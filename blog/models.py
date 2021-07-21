from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User


#class CategoryManager(models.Model):
#    def active(self):
#        return self.objects.filter(status==True)


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200)
    status = models.BooleanField(default=True, verbose_name='نمایش')
    position = models.IntegerField()

    parent = models.ForeignKey(
        'self',
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='زیردسته'
    )


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']


    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish'),
    )

    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name='وضعیت انتشار'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='وضعیت'
    )

    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles',
        verbose_name='نویسنده'
    )
    category = models.ManyToManyField(Category, related_name='articles')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"


    def __str__(self):
        return self.title

    def get_thumbnail(self):
        return format_html(
            "<img src='{}' with=40 height=40'>".format(self.thumbnail.url)
        )

    def get_absolute_url(self):
        return reverse("blog:index")

    get_thumbnail.short_description = 'تصویر'

    objects = ArticleManager()

