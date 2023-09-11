from django.urls import path
from .views import getall, getdetail, post, patch, put, delete, today, last_ten, status


urlpatterns=[
    path('getall/', getall.as_view()),
    path('getdetail/<int:forid>', getdetail.as_view()),
    path('post/', post.as_view()),
    path('patch/<int:forid>', patch.as_view()),
    path('put/<int:forid>', put.as_view()),
    path('delete/<int:forid>', delete.as_view()),
    path('today/', today.as_view()),
    path('last_ten/', last_ten.as_view()),
    path('status/', status.as_view())
]