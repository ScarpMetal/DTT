from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from DTTApp.views import *

urlpatterns = [
    url(r'^$', main_page, name='Main-page'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)