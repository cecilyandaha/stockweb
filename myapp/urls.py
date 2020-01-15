# @Time : 2020/1/9 11:40
# @Author : lisalou
# @File : urls.py
# @Software : PyCharm
from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]