"""semester_preregistration_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from adminpanel import views
from student import views as sviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('adminpanel/',include('adminpanel.urls')),
    path('advisor/',include('advisor.urls')),
    path('accounts/', include('users.urls')),
    path('', include('users.urls')),
    path('error404/<msg>',views.error404, name='error404' ),
    path('prevpage',views.prevPage, name='prevPage' ),
    path('gototohomepage',sviews.gototohomepage, name='gototohomepage' ),

    # path('accounts/', include('allauth.urls')),
    # path('profile/', user_views.home, name='profile'),
]
# handler404 = 'views.error404'