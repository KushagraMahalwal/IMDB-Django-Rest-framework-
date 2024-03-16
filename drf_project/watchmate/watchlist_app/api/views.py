from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from watchlist_app.models import WatchList, StreamPlatform,Review
from rest_framework import mixins
from rest_framework import generics

from rest_framework.throttling import UserRateThrottle,AnonRateThrottle, ScopedRateThrottle
from watchlist_app.api.throttling import ReviewCreateThrottle,ReviewListThrottle
from watchlist_app.api.pagination import WatchListPagination,WatchListLOPagination,WatchListCPagination
from rest_framework.decorators import api_view


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



from rest_framework.views import APIView
from watchlist_app.api.serializers import ReviewSerializer, WatchListSerializer, StreamPlatformSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly




class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        # everything is stored in pk
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username)


# using generic views along with mixins

class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes=[ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()
    

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchList=WatchList.objects.get(pk=pk)

        review_user=self.request.user
        review_queryset=Review.objects.filter(watchlist=watchList, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie")

        if watchList.number_rating==0:

            # getting the new ratings/lastly posted rating
            watchList.avg_rating=serializer.validated_data['rating']

        else:
            # dividing previous avg rating with the new avg rating
            watchList.avg_rating=(watchList.avg_rating+serializer.validated_data['rating'])/2
        
        watchList.number_rating = watchList.number_rating+1
        
        # saving the instance
        watchList.save()
        serializer.save(watchlist=watchList,review_user=review_user)
        



class ReviewList(generics.ListAPIView):

    serializer_class = ReviewSerializer

    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']


    # overridding queryset
    def get_queryset(self):

        # everything is stored in pk
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    

class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    
    serializer_class = StreamPlatformSerializer
    queryset = StreamPlatform.objects.all()


class StreamPlatformAV(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self,request):

        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer=StreamPlatformSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors())
    
class StreamPlatformDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self,request,pk):

        try:
            platform=StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response({'data':'Does not exists'})

        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)

        serializer=StreamPlatformSerializer(platform)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors())

    def delete(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response({'data':'Task deleted successfully'})


class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self,request):

        movies=WatchList.objects.all()
        # serializing
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    
    def post(self,request):

        # deserializing
        serializer=WatchListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class WatchDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]


    def get(self,request,pk):
        
        try:
            movie=WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response({'data':'Movie does not exists'})

        serializer=WatchListSerializer(movie)
        return Response(serializer.data)

    
    def put(self,request,pk):

        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        else:
            return Response(serializer.errors)

    
    def delete(self,request,pk):
        
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({'data':'Task has been deleted successfully'})


