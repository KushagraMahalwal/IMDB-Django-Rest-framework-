from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review
from django.utils.timezone import now

# admin username =kushagra | pass -kushagra
# user 2 John:john@1234


# we are using here serializer.ModelSerializer, do not need to define each field again here
# like we did in serializer.serializer and also we do not need to create the create and put
# methods seperatly 


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



    # this is used when we want to extract only a specific field instead of all
    
    # Watchlist=serializers.StringRelatedField(many=True)

#when we have to extract links 

    # Watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='WatchDetailsAV'
    # )


    # Serializer takes complex data and convert it into python native datatype 
# we are using here serializer.serializer  

## validators

# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError('Name is too short')

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()


#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description', instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()

#         return instance


## Field Level Validation

#     def validate_name(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError('Name is too short')
#         return value

## Object Level Validation

#     def validate(self,data):
#             if data['name']==data['description']:
#                 raise serializers.ValidationError('Name and Description cannot be same')
#             return data

