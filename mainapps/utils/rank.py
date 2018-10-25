from utils import redis_cache


from content.models import Book

# 加入周排行
def add_week_rank(book_id):
    flag = redis_cache.exists('WeekRank')
    redis_cache.zincrby('WeekRank', book_id)

    if not flag:  # 新的一周开始的时候
        redis_cache.expire('WeekRank', 604800)


# 获取周排的前几名
def get_week_rank(top=5):
    rank_ids = redis_cache.zrevrange('WeekRank', 0, top-1, withscores=True)
    return [(Book.objects.get(pk=id.decode()), round(score))
            for id, score in rank_ids]