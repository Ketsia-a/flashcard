from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from insta import views as user_views




urlpatterns=[
    
    path('accounts/register/', views.register, name='register'),
    path('profile/', user_views.profile,name = 'profile'),
    path('update_profile/', user_views.update_profile,name = 'update_profile'),

]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
