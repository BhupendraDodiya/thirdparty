from django.urls import path
from data import views

urlpatterns = [
    path('',views.showdata),
    path('one/',views.showone),
    path('create/',views.createdata),
    path('updatedata/',views.updatedata),
    path('deletedata/',views.deletedata),
]