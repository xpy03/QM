from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50,
                                verbose_name='账户')
    password = models.CharField(max_length=100,
                                verbose_name='口令')

    nickname = models.CharField(max_length=50,
                                verbose_name='昵称')

    phone = models.CharField(max_length=11,
                             verbose_name='手机号')

    # ajax头像上传
    photo = models.CharField(max_length=100,
                             verbose_name='头像',
                             blank=True)

    add_time = models.DateTimeField(verbose_name='注册时间',
                                    auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = make_password(self.password)
        super().save()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name