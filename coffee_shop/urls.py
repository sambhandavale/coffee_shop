from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login import views as login_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('register/', include('login.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('users.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

