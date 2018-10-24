from django.db import models


# Create your models here.
class Order(models.Model):

    pay_status_t = ((0, '未支付'), (1, '已支付'), (2, '正在支付'))

    # 日期+序号 ? 自定义自增字段
    cn = models.CharField(max_length=20,
                          verbose_name='单号')

    title = models.CharField(max_length=100,
                             verbose_name='标题')

    price = models.DecimalField(verbose_name='金额',
                                max_digits=10,
                                decimal_places=2)

    add_time = models.DateTimeField(verbose_name='下单时间',
                                    auto_now_add=True)

    modify_time = models.DateTimeField(verbose_name='更新时间',
                                       auto_now=True)

    pay_status = models.IntegerField(verbose_name='订单状态',
                                     choices=pay_status_t,
                                     default=0)

    def __str__(self):
        return self.title

    @property
    def pay_status_name(self):
        return self.pay_status_t[self.pay_status][1]

    class Meta:
        db_table = 't_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name