from django.http import JsonResponse
from django.shortcuts import render

from order.tasks import qbuy
from utils.qbuy import get_isqbuy, query_state, is_buyed


# Create your views here.
def q_read(req, book_id):
    msg = {'code': 201, 'msg': '抢购中'}
    # 验证当前用户是否登录: session['login_user']
    login_user = req.session.get('login_user')
    if not login_user:
        msg['code'] = 100
        msg['msg'] = '当前用户未登录'
    else:
        user_id = login_user.get('id')
        # 判断是否已抢过
        if is_buyed(user_id=user_id):
            msg['code'] = 301
            msg['msg'] = '同一用户只能抢一次'
        else:
            # 判断当前是否已抢完
            if not get_isqbuy():
                msg['code'] = 300
                msg['msg'] = '抢购失败'
            else:
                # 异步执行
                qbuy.delay(user_id, book_id)

    return JsonResponse(msg)


def qbuy_query(req, book_id):
    msg = {}
    # 查询抢购的状态
    # 验证当前用户是否登录: session['login_user']
    login_user = req.session.get('login_user')
    if not login_user:
        msg['code'] = 100
        msg['msg'] = '当前用户未登录'

    user_id = login_user.get('id')  # ?之前是user_id
    msg['code'], msg['msg'] = query_state(user_id=user_id, goods_id=int(book_id))
    return JsonResponse(msg)