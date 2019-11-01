from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
   url(r'^$',views.home,name = 'home'),
   url(r'^search/', views.search_results, name='search_results'),
   url(r'^hood/(\d+)',views.hoods,name = 'hood')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)