
from django.urls import path
from .views import MobileListView,MobileDetailView
urlpatterns = [
   path('', MobileListView.as_view(), name='thing_list'),
   path('<int:pk>', MobileDetailView.as_view(),name='thing_detail')
]
