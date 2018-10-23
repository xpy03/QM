from django.conf.urls import url

import xadmin as admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
