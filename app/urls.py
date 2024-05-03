# from msilib.schema import _Validation_records
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import Register, EditInfoView

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', Register.as_view(), name="register"),
    path('editar/<slug:pk>', EditInfoView.as_view(), name="edit"),
    path('delete/account', views.delete_account, name="delete_account"),
    path('logout', views.logout_view, name="logout"),
]