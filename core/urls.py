
from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolimlar/', BolimlarView.as_view()),
    path('kitoblar/', KitoblarView.as_view()),
    path('tirik/', TirikKitobView.as_view()),
    path('kitoblar/<int:pk>', Kitob, name ='kitob'),
    path('kitoblar/<int:pk>/o\'chirish', kitob_ochirish, name='kitob_ochirish')

]
