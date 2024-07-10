from django.urls import path , re_path
from . import views 
app_name = 'prediction_model_app'
urlpatterns = [
    path("", views.home, name="home"),
    path('sofi_ui', views.sofi_ui, name='sofi_ui'),
]