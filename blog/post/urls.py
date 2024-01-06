from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostView

router = DefaultRouter()
router.register("", PostView)

urlpatterns = [
    path("posts/", include(router.urls))
]
