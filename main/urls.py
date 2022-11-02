from django.urls import path
from. import views
from .views import collection_details
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:pk>/', collection_details.as_view(), name='collection-details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)