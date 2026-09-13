from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from .views import registration

app_name = 'djangoapp'
urlpatterns = [
        path("register", registration, name="register"),

    path(route='login', view=views.login_user, name='login'),
        path(route='logout', view=views.logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
