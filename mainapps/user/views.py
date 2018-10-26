import json

from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user.forms import UserForm
from user.models import UserProfile


@csrf_exempt
def regist(request):
    if request.method == 'POST':
        # 创建UserForm表单对象
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()  # 写入数据库
            return redirect('/')

        errors = json.loads(form.errors.as_json())
    return render(request, 'user/regist.html', locals())


@csrf_exempt
def login(request):
    if request.method == 'POST':

        errors = {'msg': ''}
        username = request.POST.get('username')
        password = request.POST.get('password')  # 明文

        queryset = UserProfile.objects.filter(username=username)
        if not queryset.exists():
            errors['msg'] = '%s 用户不存在，请先注册!' % username
        else:
            user = queryset.first()  # user.password 密文
            # 验证口令
            if check_password(password, user.password):
                # 将登录后的信息存入到session中
                request.session['login_user'] = {
                    'id': user.id,
                    'nickname': user.nickname,
                    'photo': user.photo
                }
                return redirect('/')
            else:
                errors['msg'] = '登录口令不正确！'

    return render(request, 'user/login.html', locals())