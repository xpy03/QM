import xadmin
from xadmin import views

from content.models import Category, Tag, Book


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSetting():
    site_title = '趣文管理后台'
    site_footer = '西安趣文科技'

    # 公共搜索模型(问题： 一个模型类不显示搜索框)
    global_search_models = [Category, Tag]

    # 设置模型图标
    global_models_icon = {
        Category: 'glyphicon glyphicon-th-list',
        Tag: 'glyphicon glyphicon-bookmark',
        Book: 'glyphicon glyphicon-list-alt'
    }

    # 设置app模块的图标
    apps_icons = {
        'content': 'glyphicon glyphicon-book'
    }

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


# Register your models here.
class CategoryAdmin():
    # 列表显示的字段
    list_display = ['title', 'add_time', 'parent']

    list_per_page = 10  # 分页显示，每页显示10条


class TagAdmin():
    list_display = ['title']


class BookAdmin():
    list_display = ['title',
                    'author',
                    'summary',
                    'tags',
                    'category'
                    ]

    # 设置字段的样式（编辑表单使用的样式）
    style_fields = {
        'info': 'ueditor'
    }


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Book, BookAdmin)