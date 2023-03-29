from django.urls import path
from board import views
from .views import (
    PostList, ResponseList, AdvertList,
    PostUpdate, PostDelete,
    RespUpdate, RespDelete
)

urlpatterns = [
    path('', PostList.as_view(), name='board'),
    path('<int:pk>', AdvertList.as_view(), name='advert'),
    path('create/', views.post_add, name='create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/resp/', views.resp_add, name='resp_create'),
    path('response/', ResponseList.as_view(), name='response'),
    path('response/<int:pk>/update/', RespUpdate.as_view(), name='resp_up'),
    path('response/<int:pk>/delete/', RespDelete.as_view(), name='resp_del'),
]
