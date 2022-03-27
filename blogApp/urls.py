from django.urls import path
from . import views
from .views import blog, search, CategoryView, blogdetail, schedules, home


urlpatterns = [
path('', home, name="home"),
path('choreographers', blog.as_view(), name="choreographers"),
path('search', search, name="search"),
path('category/<str:cats>/', CategoryView, name="category"),
path('<slug:slug>/send-comment', views.send_comment, name="send_comment"),
path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
path('schedules', schedules, name="schedules"),
]
