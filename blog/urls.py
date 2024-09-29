from django.contrib import admin
from django.views.decorators.cache import cache_control
from django.contrib.staticfiles.views import serve
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import *

urlpatterns = [
    path('',blog_view,name='blog_index'),
    path('4-challenges-international-students-face-in-the-us',challenges_international_students_view,name='4-challenges-international-students'),
    path('4-sources-to-find-scholarships-in-europe',challenges_international_students_europe_view,name='challenges-international-students-europe'),
    path('5-challenges-of-international-students-in-canada',challenges_international_students_canada_view,name='challenges-international-students-canada'),
    path('best-canadian-universities-for-indian-students',canada_indian_students_view,name='best-canadian-universities-for-indian-students'),
    path('test',test_view), 
    path('masters-programs-in-europe',master_europe_view,name='masters-programs-in-europe'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)