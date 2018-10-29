from QM.celery import app

import time

from utils.qbuy import *
from order.models import Order, OrderDetail
from content.models import Book


@app.task  # 声明qbuy可以被异步执行
def qbuy(user_id, goods_id):
    print('用户{} 正在抢 {} 商品'.format(user_id, goods_id))
    time.sleep(5)
    if not get_isqbuy():
        return '未抢到'

    # 向qbuy缓存中添加当前用户和商品的信息
    if not add_qbuy(user_id=user_id, goods_id=goods_id):
        return '同一用户只限一本书'

    return '抢到了'


@app.task
def add_order():
    # 定时( 00:00:00 )将 抢购的商品存入到订单
    # [{'user_id': 8, 'goods_id': 2}]
    qbuy_goods = get_all_qbuy()
    if not qbuy_goods:
        return '无数据，无法生成订单'

    for goods in qbuy_goods:
        user_id = goods.get('user_id')
        book_id = goods.get('goods_id')

        order = Order()
        order.title = '抢读%s' % Book.objects.get(pk=book_id).title
        order.price = 0
        order.user_id = user_id
        order.pay_status = 1  # 1 已支付
        order.save()

        order_detail = OrderDetail()
        order_detail.order = order
        order_detail.price = 0
        order_detail.cnt = 1
        order_detail.book_id = book_id

        order_detail.save()

    # 清空qbuy缓存
    clear_qbuy()

    return '定时生成订单成功'


