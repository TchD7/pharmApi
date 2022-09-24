from django.urls import include, path
from . import views

urlpatterns = [

    path('create/', views.create, name='create'),
    path('create/update/<int:pharm_id>', views.update),
    path('create/garde/<int:pharm_id>', views.garde),
    path('create/delete/<int:pharm_id>', views.delete),
    path('create/delete_on_garde/<int:pharm_id>', views.delete_on_garde)

]
