from django.urls import path, include
from . import views
app_name = 'party'
urlpatterns = [
    path('', views.party,name='party'),
    path('data_analysis/', views.data_analysis, name='data_analysis'),
    path('decrease_credits/<int:amount>', views.decrease_credits, name='decrease_credits'),
    path('sentiment_analysis/single', views.sentiment_analysis_single, name='sentiment_analysis_single'),
    path('sentiment_analysis/batch', views.sentiment_analysis_batch, name='sentiment_analysis_batch'),
]