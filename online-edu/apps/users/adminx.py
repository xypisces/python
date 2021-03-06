# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2017/3/1 下午7:28'
"""

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import EmailVerifyRecord, UserProfile
from .models import Banner


class UserProfileAdmin(UserAdmin):
    pass


class BaseSetting(object):
    enable_themes = True  # 主题功能
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u"创客教育后台管理系统"
    site_footer = u"创客教育平台"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# django xadmin自动注册的User 卸载
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# UserProfile注册
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
