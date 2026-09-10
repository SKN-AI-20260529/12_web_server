"""
- 현재 프로젝트(서버)의 URL 입구
- 경로 앞부분으로 앱을 선택하고 나머지는 앱별로 존재하는 urls.py로 넘긴다.

URL configuration for _01_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'second'
urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]

# startapp 수행* 후 해야 할 일  *터미널에서 python manage.py startapp second 입력
# 1) settings.py > INSTALLED_APPS에 앱 등록
# 2) 설정폴더/urls.py > urlpatterns 등록
# 3) 생성한 앱 폴더/urls.py 생성
