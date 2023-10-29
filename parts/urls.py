from django.urls import path
from . import views

app_name = 'parts'

urlpatterns = [
    path('get_component_tree/', views.get_component_tree, name='get_component_tree'),

]
