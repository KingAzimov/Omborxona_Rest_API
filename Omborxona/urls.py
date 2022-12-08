from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('asosiy/', include('asosiyapp.urls')),
    path('stats/', include('statsapp.urls')),
    # path('get_token/', obtain_auth_token, name='api_token_auth'),
]