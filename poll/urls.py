from . import views
from django.urls import path
app_name= "poll"
urlpatterns = [
    path('' ,views.index, name='index'),
    path('choices/<int:question_id>/', views.detail , name="detail"),
    path('<int:question_id>/results/', views.results, name="results"),
    path('<int:question_id>/vote', views.vote , name="vote"),
]
