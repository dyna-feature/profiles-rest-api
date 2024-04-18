from django.urls import path, include
from profile_api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hellow-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # tidak pakai base_name karena di views sudah ada queryset, basename di tambah kalau di vies tidak ada query

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
