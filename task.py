from django.urls import  path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
  path("", include("app.urls")),
  path("signup", views.signup, name="Signup"),
  path("login", views.login, name="Login"),
  path("logout", views.logout, name="Logout"),
  path("home", views.home, name="Home"),
  path("error", views.error, name="Error"),
  path("settings", views.settings, name="Settings"),
  path("success", views.success, name="Success"),
  ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)