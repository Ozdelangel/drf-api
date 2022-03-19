from django.urls import path
from .views import FightersList, FightersDetail


urlpatterns = [
    path('', FightersList.as_view(), name='fighters_list'),
    path('<int:pk>/', FightersDetail.as_view(), name='fighters_detail')
]