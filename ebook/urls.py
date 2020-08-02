from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from homepage import views as user_views
from blog.views import PostDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
