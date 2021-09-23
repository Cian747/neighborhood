from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import EditProfileView
from . import views



urlpatterns = [
    path('', views.login_user,name='login_user'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('home/',views.home, name='home'),
    path('post-message/',views.post_message,name='post_message'),
    path('profile/<int:id>',views.my_profile,name='profile'),
    # path('register-business/',views.register_business,name='register_business'),
    path('edit_profile/<int:pk>',EditProfileView.as_view(),name='edit_profile'),
    path('search_business/',views.search_for_business,name='search_business'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)