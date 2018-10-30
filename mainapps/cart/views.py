from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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

    total_price = sum([book.price * cnt for book, cnt in goods_list])

    # 更新购物车的总量
    req.session['cart_cnt'] = cart.count_cart(user_id)

    return render(req, 'cart/list.html', locals())


def del_cart(req, goods_id):
    user_id = req.session.get('login_user').get('id')
    cart.remove_cart(user_id, goods_id)

    # 更新购物车的总量
    req.session['cart_cnt'] = cart.count_cart(user_id)

    return JsonResponse({'code': 200,
                         'msg': '删除成功!'})


@csrf_exempt
def go_pay(req):
    user_id = req.session.get('login_user').get('id')
    # 读取上传的ids
    ids = req.GET.get('ids').split(',')[:-1]

    # [(<Book>, cnt)]
    cart_goods = cart.get_cart_by_ids(user_id, ids)

    # 将ids的商品从购物车中去除
    cart.remove_cart(user_id, ids)

    req.session['cart_cnt'] = cart.count_cart(user_id)

    # 生成订单
    # 收货信息
    # 支付方式
    return render(req, 'cart/order_info.html', locals())