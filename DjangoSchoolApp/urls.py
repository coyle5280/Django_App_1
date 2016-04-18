"""DjangoSchoolApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from college import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^students/', views.student, name='student'),
    url(r'^student/(?P<id>\d+)/', views.student_detail, name='student_detail'),
    url(r'^professor/(?P<id>\d+)/', views.professor_detail, name='professor_detail'),
    url(r'^professors/', views.professor, name='professor'),
    url(r'^courses/', views.course, name='course'),
    url(r'^course/(?P<id>\d+)/', views.course_detail, name='course_detail'),
    url(r'^login/$', admin.site.login, name='login'),
    url(r'^accounts/login/$', admin.site.login, name='login'),
    url(r'^student/new/$', views.new_student, name='new_student'),
    url(r'^professor/new/$', views.new_professor, name='new_professor'),
    url(r'^course/new/$', views.new_course, name='new_course'),
    url(r'^sections/', views.section, name='section'),
    url(r'^section/(?P<id>\d+)/', views.section_detail, name='section_detail'),
    url(r'^section/new/$', views.new_section, name='new_section')
]
