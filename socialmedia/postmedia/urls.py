from django.urls import path
from postmedia import views
urlpatterns = [
    path('',views.Login),
    path('main/',views.main_page),
    path('search',views.search),
    path('home/', views.index),
    path('createPost/',views.createPost),
    path('like_post',views.like_post),
    path('del_id',views.del_post),
    path('Sign/',views.Sign),
    path('logout/',views.logout),
    path('account/',views.accountsettings),
    path('profile/<str:pk>',views.profile)
    
]
