from rest_framework import routers

from api.tag import TagViewSets
from api.category import CategoryViewSets
from api.book import BookViewSets

# 创建api的子路由
router = routers.DefaultRouter()
router.register('tag', TagViewSets)
router.register('category', CategoryViewSets)
router.register('book', BookViewSets)
