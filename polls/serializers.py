from rest_framework import serializers


class AddNewMusicSerializer(serializers.Serializer):
    composer = serializers.CharField(max_length=1000)
    executor = serializers.CharField(max_length=1000)
    genre = serializers.CharField(max_length=1000)
    label = serializers.CharField(max_length=1000)
    nominations = serializers.CharField(max_length=1000)
    release_date = serializers.CharField(max_length=1000)
    songwriter = serializers.CharField(max_length=1000)
    file_in_binary = serializers.CharField(max_length=1000)