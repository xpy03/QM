import xadmin

from content.models import Category

# Register your models here.
class CategoryAdmin():
    # 列表显示的字段
    list_display = ['title', 'add_time', 'parent']

    list_per_page = 10  # 分页显示，每页显示10条


xadmin.site.register(Category, CategoryAdmin)