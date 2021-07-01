from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('phone_book',views.phone_book,name='phone_book'),
    path('addContact',views.addContact,name='addContact'),
    path('show',views.show,name='show'),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name='delete'),
    path('update',views.update,name='update'),
    path('weather',views.weather,name='weather'),
]

