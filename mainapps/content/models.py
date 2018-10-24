import uuid

import os
from django.db import models


from DjangoUeditor.models import UEditorField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='名称')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')
    parent = models.ForeignKey('self',
                               blank=True,  # 不是必填项(admin form验证),
                               null=True,
                               on_delete=models.CASCADE,  # 级联操作
                               verbose_name='所属分类')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_category'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']


class Tag(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='名称')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Book(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='书名')
    author = models.CharField(max_length=20,
                              verbose_name='作者')

    summary = models.TextField(max_length=100,
                               verbose_name='简介')

    # info = models.TextField(max_length=200,
    #                         verbose_name='作品信息')
    info = UEditorField(verbose_name='作品信息',
                        blank=True, default='',
                        width=640, height=480,
                        imagePath='ueditor/imgs/',
                        filePath='ueditor/files/',
                        toolbars='full')  # mini, normal, full

    cover = models.ImageField(verbose_name='封面',
                              upload_to='book',
                              blank=True, null=True)  # 相对于MEDIA_ROOT目录

    tags = models.ManyToManyField(Tag,
                                  verbose_name='标签')

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='分类')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.cover.name) < 30:
            self.cover.name = str(uuid.uuid4()).replace('-', '')+ os.path.splitext(self.cover.name)[-1]
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_book'
        verbose_name = '小说'
        verbose_name_plural = verbose_name