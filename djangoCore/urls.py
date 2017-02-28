from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include('restapi.urls')),
]
