from content.models import Book
from utils import redis_cache


def add_cart(user_id, goods_id, cnt=1):
    # 查询 goods_id是否在 cart_{user_id}中
    name = get_cart_name(user_id)
    if redis_cache.hexists(name, goods_id):
        cnt += int(redis_cache.hget(name, goods_id).decode())

    # 更新数量
    redis_cache.hset(name, goods_id, cnt)


def get_cart_name(user_id):
    return 'cart_{}'.format(user_id)


def remove_cart(user_id, ids):
    # 判断goods_id是否在购物车
    name = get_cart_name(user_id)
    for goods_id in ids:
        if redis_cache.hexists(name, goods_id):
            redis_cache.hdel(name, goods_id)


def list_cart(user_id):
    name = get_cart_name(user_id)
    # [(Book, cnt)]
    # ？PEP8单行字符不能超过79个？
    goods = [(Book.objects.get(pk=id_.decode()), int(cnt.decode())) for id_, cnt in redis_cache.hgetall(name).items()]

    return goods  # goods模型类中包含price（单价）


def count_cart(user_id):
    # 统计当前用户下所有商品的数量和
    name = get_cart_name(user_id)
    return sum([int(cnt.decode()) for goods_id, cnt in redis_cache.hgetall(name).items()])


def get_cart_by_ids(user_id, ids):
    goods_list = list_cart(user_id)
    return [(goods, cnt) for goods, cnt in goods_list if goods.id in ids]