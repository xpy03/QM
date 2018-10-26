import json

import os

import time
from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from QM import settings
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


def logout(request):
    # 从哪个页面请求过来的
    print('Referer:', request.META.get('Referer'))
    del request.session['login_user']
    return redirect('/')


@csrf_exempt
def uploadImg(request):
    print(request.FILES)
    uploadFile: InMemoryUploadedFile = request.FILES.get('img')  # 前端上传文件的字段名

    # uploadFile.name  文件名
    # uploadFile.content_type  文件类型 image/jpeg
    # uploadFile.size  文件大小

    # 写入到服务器的用户头像存储的位置中
    photo_dir = os.path.join(settings.BASE_DIR, 'static/user/imgs')

    file_name = str(round(time.time())) + os.path.splitext(uploadFile.name)[-1]

    # 将上传的文件按段(缓存块)写入到目标文件中
    with open(os.path.join(photo_dir, file_name), 'wb') as f:
        for chunk in uploadFile.chunks():
            f.write(chunk)

    return JsonResponse({'path': 'user/imgs/%s' % file_name,
                         'code': 20})