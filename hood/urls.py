from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import EditProfileView
from . import views



urlpatterns = [
    path('', views.landing_page,name='landing page'),
    path('login/', views.login_user,name='login_user'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('news/', views.neighbor_news,name='neighborhub_news'),
    path('events/', views.neighbor_events,name='neighborhub_events'),
    path('groups/',views.neighbor_groups,name = 'groups'),
    path('business/',views.neighborhood_businesses,name = 'businesses'),
    path('new-hood/',views.create_hood, name="create_hood"), 
    # path('register/',views.register_user,name='register'),
    path('register/',views.register_page,name='register'),
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