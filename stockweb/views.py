# @Time : 2020/1/9 9:57
# @Author : lisalou
# @File : views.py
# @Software : PyCharm

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")