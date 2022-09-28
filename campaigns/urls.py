from django.urls import path

from .views import (
    CampaignDetailAPIView,
    CampaignListAPIView,
    SubscribeToCampaignAPIView,
)

urlpatterns = [
    path("campaigns", CampaignListAPIView.as_view(), name="campaigns"),
    path("campaigns/subscribe", SubscribeToCampaignAPIView.as_view(), name="subscribe"),
    path("campaigns/<str:slug>", CampaignDetailAPIView.as_view(), name="campaign"),
]
