from django.http import JsonResponse
from django.shortcuts import render

from utils import cart


# Create your views here.
def add_cart(req, book_id):
    user_id = req.session.get('login_user').get('id')
    cart.add_cart(user_id, book_id)

    cnt = cart.count_cart(user_id)
    req.session['cart_cnt'] = cnt  # 更新购物车的总量

    return JsonResponse({'code': 200, 'msg': '添加成功'})


def list(req):
    user_id = req.session.get('login_user').get('id')
    goods_list = cart.list_cart(user_id)

    total_price = sum([book.price*cnt for book, cnt in goods_list])
    return render(req, 'cart/list.html', locals())

