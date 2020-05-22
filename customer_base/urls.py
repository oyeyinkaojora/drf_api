from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app.views import DocumentViewSet ,CustomerViewSet,ProfessionViewSet,DataSheetViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'professions', ProfessionViewSet)
router.register(r'data_sheet', DataSheetViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("api-auth/", include('rest_framework.urls') ),
]
