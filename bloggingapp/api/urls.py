'''api/urls.py'''
from django.urls import path, re_path, include
from .views import CreateView
from .views import DetailsView 

urlpatterns = [
    path('blogapp/', CreateView.as_view(), name="create"),
    re_path('blogapp/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
]
