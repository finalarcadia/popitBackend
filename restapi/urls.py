from django.conf.urls import url, include
from rest_framework import routers

#from restAPI import views
from . import views
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'challenge', views.ChallengeViewSet)
router.register(r'user', views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
