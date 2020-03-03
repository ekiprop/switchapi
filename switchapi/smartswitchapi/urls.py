from django.urls import path, include
from smartswitchapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'switchapi', views.SwitchapiViewSet)


urlpatterns = [
    path('', include(router.urls)),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
