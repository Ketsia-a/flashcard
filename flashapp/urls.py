from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name = 'home'),
  path('register/', views.register, name='register'),
  path('profile/<username>', views.profile, name='profile'),
  path('subject/<subject>',views.card_category,name = 'subject'),  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
