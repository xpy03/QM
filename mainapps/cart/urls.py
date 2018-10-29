from django.conf.urls import url

from cart import views
urlpatterns = [
    url(r'^add/(\d+)/', views.add_cart),
    url(r'^list/', views.list),
]
