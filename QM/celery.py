from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

from QM import settings

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QM.settings')

# 创建Celery对象
app = Celery('QbuyCelery')

# 配置app
app.config_from_object('django.conf:settings')


# 自动查询或发现异步任务的函数
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
