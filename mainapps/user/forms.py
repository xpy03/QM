import re

from django import forms
from django.core.exceptions import ValidationError

from user.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8,
                               label='口令',
                               error_messages={'required': '登录口令不能为空!',
                                               'min_length': '不能少于8位字符！'})
    password2 = forms.CharField(min_length=8,
                                label='重复口令',
                                error_messages={'required': '重复口令不能为空!',
                                                'min_length': '不能少于8位字符！'})

    class Meta:
        model = UserProfile
        fields = '__all__'  # 所有字段

        error_messages = {
            'username': {
                'required': '用户名不能为空!'
            },
            'phone': {
                'required': '联系电话不能为空!'
            },
            'nickname': {
                'required': '昵称不能为空!'
            },
        }

    def clean_password2(self):
        # 以上password2 字段的验证通过了，之后再进一步调用此函数进行另外的验证
        pwd = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('password2')

        if pwd != pwd2:
            # 向errors中添加验证错误
            raise ValidationError('两次口令不相同!')

        return pwd

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'1[3-9]\d{9}', phone):
            raise ValidationError('手机号不存在！')

        return phone