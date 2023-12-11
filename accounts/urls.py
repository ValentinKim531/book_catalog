from django.urls import path

from accounts.views import (
    LoginView,
    logout_view,
    RegisterView,
    ProfileView,
    UserChangeView,
    UserPasswordChangeView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("account/<int:pk>", ProfileView.as_view(), name="profile"),
    path("account/<int:pk>/change", UserChangeView.as_view(), name="change"),
    path(
        "<int:pk>/password_change",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
]
