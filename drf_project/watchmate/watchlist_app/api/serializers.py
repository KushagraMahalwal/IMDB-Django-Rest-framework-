from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review
from django.utils.timezone import now


class ReviewSerializer(serializers.ModelSerializer):

    review_user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review
        # fields="__all__"
        exclude=('watchlist',)


# For watchlist model
class WatchListSerializer(serializers.ModelSerializer):

   # Serializer method field do not need to define in the models
    # reviews=ReviewSerializer(many=True,read_only=True)
    platform=serializers.CharField(source='platform.name')
  
    class Meta:
        model=WatchList

        # used to extract all the field present in the model
        fields="__all__"


# For stremplatform model  
class StreamPlatformSerializer(serializers.ModelSerializer):

    # Nested Serializer ---- Watchlist --> related_name=WatchList ----> models
    Watchlist=WatchListSerializer(many=True,read_only=True)
    
    class Meta:
        model=StreamPlatform

        fields="__all__"
