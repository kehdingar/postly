from django.urls import path
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'', PostViewSet)
# The router object is used to register the PostViewSet viewset with the default router. 
# This creates the standard URL patterns for the viewset, such as /posts/ and /posts/<int:pk>/

urlpatterns = [
    path('<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='like'),    
]

urlpatterns += router.urls
