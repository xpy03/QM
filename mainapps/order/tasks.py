from QM.celery import app

import time

from utils.qbuy import *


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
