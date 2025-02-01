from django.urls import path
from .views import DatosView,EditarView,eliminar

urlpatterns = [
    path('', DatosView.as_view(),name='inicio'),
    path('editar/<int:pk>',EditarView.as_view(),name='editar'),
    path('eliminar/<int:pk>',eliminar,name='eliminar'),

   
]