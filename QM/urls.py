from django.conf.urls import url, include
from django.shortcuts import render

import xadmin as admin

from content.models import Category

def toIndex(request):
    # 查询一级分类
    cates = Category.objects.filter(parent__isnull=True).all()
    return render(request, 'index.html', locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'', toIndex),
]
