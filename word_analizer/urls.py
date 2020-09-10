from django.urls import path
from .views import TextDetailView, TextListView, TextCreateView


urlpatterns = [
    path("", TextCreateView.as_view(), name="text_create_view"),
    path("texts/", TextListView.as_view(), name="text_list_view"),
    path("<pk>/", TextDetailView.as_view(), name="text_detail_view"),
]