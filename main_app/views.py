from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response

from .models import *
from .serializers import *
import requests
import json

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'put','patch', 'delete']
    

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'year','rating', 'genres__genre_title']

    def get_queryset(self):
        data = self.queryset
        rating = self.request.GET.get('rating', '')

        if rating != '':
            data = data.filter(rating__gt = rating)

        return data

class TitleSearchView(viewsets.ViewSet):
   
    def list(self, request):
        queryset = Movie.objects.all()
        title = self.request.GET.get('title', '')

        if title != '':
            data = queryset.filter(title=title)
            print(data)

            if data==[]:
                apiKey="6db8dfbb"
                data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
                params = {
                    't': title
                }
                response = requests.get(data_URL,params=params).json()
                print(response)
                json_data = json.load(response)
                print("json",json_data)
                for i in json_data:
                    movies = Movie(title = i.Title, rating = i.Rated, year = i.Year)
                    movies.save()
                
                data = queryset.filter(title=title)
                print(data)

        serializer = MovieSerializer(data, many=True)
        return Response(serializer.data)