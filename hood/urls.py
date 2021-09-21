from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.login_user,name='login_user'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    # path('home/',HomeView.as_view(), name='home'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)