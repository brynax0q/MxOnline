# -*- coding:utf-8 -*-
__author__ = 'brynao'
__date__ = '2017/7/27 下午6:36'
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile



# 登陆 form 处理
class LoginForm(forms.Form):
    # 相当于预处理
    # 指定为Char类型，（required=True）：如果为空则报错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

# 注册 form 处理
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 出错信息
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    # 出错信息
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


# 密码修改
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UploadInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birday', 'gender', 'address', 'mobile']




