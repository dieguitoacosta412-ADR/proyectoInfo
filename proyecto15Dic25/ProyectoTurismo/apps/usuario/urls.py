from django.urls import path
from .views import (
    LoginUsuarioView,
    LogoutUsuarioView,
    RegistroUsuarioView,
    PerfilUsuarioView,
)

app_name = "usuario"

urlpatterns = [
    path("login/", LoginUsuarioView.as_view(), name="login"),
    path("logout/", LogoutUsuarioView.as_view(), name="logout"),
    path("registro/", RegistroUsuarioView.as_view(), name="registro"),
    path("perfil/", PerfilUsuarioView.as_view(), name="perfil"),
]