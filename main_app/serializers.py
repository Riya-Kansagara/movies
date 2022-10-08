from .models import Genre, Movie
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_title']

class MovieSerializer(serializers.ModelSerializer):
    genres_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id','title', 'year', 'rating', 'genres', 'genres_name']

    def get_genres_name(self, obj):
        return GenreSerializer(obj.genres.all(), many=True).data 
        