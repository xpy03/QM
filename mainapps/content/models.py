from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='名称')
    add_time = models.DateTimeField(auto_now_add=True,
                                    verbose_name='添加时间')
    parent = models.ForeignKey('self',
                               blank=True,   # 不是必填项(admin form验证),
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