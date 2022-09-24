from django.contrib import admin
from dashbord import views
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashbord.urls')),
    path('',include('accounts.urls')),
    path('api/', include('api.urls'))

]
