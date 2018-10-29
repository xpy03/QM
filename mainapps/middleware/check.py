from django.http import JsonResponse


def ajax_login(func):
    def wrapper(request, *args, **kwargs):
        print('path->', request.path)
        if request.path.startswith('/cart/add/'):
            # 检查用户是否登录
            login_user = request.session.get('login_user')
            if not login_user:
                return JsonResponse({
                    'code': 100,
                    'msg': '用户未登录'
                })

            # kwargs['user_id'] = login_user.get('id')

        # 执行目标函数
        return func(request, *args, **kwargs)

    return wrapper