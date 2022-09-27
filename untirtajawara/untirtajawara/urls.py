
from django.contrib import admin
from django.urls import path
from untirta.views import yubisayu
urlpatterns = [
    path('admin/', admin.site.urls),
    path('untirta/', yubisayu),
]
