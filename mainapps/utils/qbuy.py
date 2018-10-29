from utils import redis_cache


def get_isqbuy(key='qbuy', max_size=5):
    '''
    查询是否已抢完
    :return:  True 未抢完， False已抢完
    '''
    return redis_cache.hlen(key) < max_size


def is_buyed(key='qbuy', user_id=None):  # 判断是否已抢过了
    return redis_cache.hexists(key, user_id)


def add_qbuy(key='qbuy', user_id=None, goods_id=None):
    # 判断当前用户是否已抢
    if redis_cache.hexists(key, user_id):
        print('已抢了')
        return False  # 已抢了

    print('抢成功')
    redis_cache.hset(key, user_id, goods_id)
    return True  # 抢成功


def query_state(key='qbuy', user_id=None, goods_id=None):
    if redis_cache.hexists(key, user_id):
        # 再验证book_id是否与本次查询的book_id匹配
        book_id_ = int(redis_cache.hget(key, user_id).decode())  # 转成int类型
        if book_id_ != goods_id:
            return 301, '本次只限一件商品'
        else:
            return 200, '抢购成功'
    else:
        if get_isqbuy():
            return 201, '抢购中'

    return 300, '抢购失败'


