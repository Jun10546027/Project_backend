    
from django.contrib import admin
from django.urls import path,include,re_path
from ProjectDB.views import homepage
from MangerDB.views import detail
from MangerDB.viewset import DataViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'data',DataViewSet)


urlpatterns = [
    path('', homepage),
    path('detail/<str:post_id>/',detail),
    path('api/',include(router.urls)),
    path("api-auth.",include('rest_framework.urls',namespace='rest_framework')),
    path('admin/', admin.site.urls),
]