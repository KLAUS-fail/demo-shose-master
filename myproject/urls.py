"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import settings

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name="myapp/login.html",
        next_page="entity_list"
    ),
    name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("guest/", views.guest_entity, name="guest"),
    path("", views.entity_list, name="entity_list", include("myapp.urls", )),
    path("add/", views.entity_form, name="entity_add"),
    path("edit/<int:pk>/", views.entity_form, name="entity_edit"),
    path("del/<int:pk>/", views.entity_delete, name="entity_delete"),

    # path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



