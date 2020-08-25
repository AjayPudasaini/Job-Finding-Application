from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('a/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('jobs.urls')),
    path('', include('contact.urls')),
    path('', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

