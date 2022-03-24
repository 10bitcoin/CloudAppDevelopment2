from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.get_dealerships, name='index'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
