"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('test/', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('posts/add', views.add_post, name='add_post'),
    path('posts/add_model', views.add_model_post, name='add_Model_post'),
    path('posts/<int:id>', views.post, name='post'),
    path('posts/<str:id>', views.post, name='post'),
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
