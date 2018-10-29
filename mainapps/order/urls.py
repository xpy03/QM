from django.conf.urls import url

from order import views
urlpatterns = [
    url(r'^qbuy/(\d+)/', views.q_read),
    url(r'^qbuy_query/(\d+)/', views.qbuy_query),
]
