from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", include("calendarapp.urls")),
    path("admin/", admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
