from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'SmartKTM Jobs'
admin.site.site_title = 'SmartKTM Jobs admin'
admin.site.index_title = 'SmartKTM Jobs administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('smartktmadmin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('jobs.urls')),
    path('', include('contact.urls')),
    path('', include('blog.urls')),
    path('', include('faq.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

