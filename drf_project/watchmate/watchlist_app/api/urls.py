from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import *

router=DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='WatchListAV'),
    path('<int:pk>/',WatchDetailsAV.as_view(),name='WatchDetailsAV'),

    path('',include(router.urls)),
   
    # to create a new review
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),

    # to get the review for the particular id
    path('<int:pk>/review/',ReviewList.as_view(),name='ReviewList'),

    # To get the review by review id
    path('review/<int:pk>/',ReviewDetails.as_view(),name='ReviewDetails'),

    # path('review/<str:username>',UserReview.as_view(),name='user-review-detail'),
    path('review/',UserReview.as_view(),name='user-review-detail'),
]
