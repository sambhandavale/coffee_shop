from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('signup/', include('login.urls')),
    path('login/', include('login.urls')),
    path('blog/', include('blog.urls'))
]
