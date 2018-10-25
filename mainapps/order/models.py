from django.db import models
from sqlite3 import Cursor

from datetime import date


class OrderNumberField(models.CharField):
    def get_db_prep_value(self, value, connection, prepared=False):
        print('--->value:', value)
        if not value:
            print('--预处理订单号--')
            cursor = connection.cursor()
            cursor.execute('select cn from t_order where id = (select max(id) from t_order)')

            current_date = date.strftime(date.today(), '%Y%m%d')
            print('--select rowcount--', cursor.rowcount)
            if cursor.rowcount > 0:  # 没有记录时，rowcount = -1
                cn = cursor.fetchone()[0]  # fetchone()返回是tuple
                date_, number = cn[:8], cn[8:]

                if date_ == current_date:
                    number = str(int(number)+1).rjust(4, '0')
                    return '%s%s' % (date_, number)

            return '%s0001' % current_date

        return value


# Create your models here.
class Order(models.Model):

    pay_status_t = ((0, '未支付'), (1, '已支付'), (2, '正在支付'))

    # 日期+序号 ? 自定义自增字段
    cn = OrderNumberField(max_length=20,
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