from rest_framework import serializers
from .models import Advisor,Service,Review,Author,Blog
class AdvisorSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('id','name','expertise','bio','contact_info','profile_views','image','slug')


class ServiceSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','name','description','price','reviews_count','advisor','reviews_count','status','image')

class ReviewSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','service','rating','comment','likes','created_at')


class AuthorSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','first_name','last_name','nickname','bio','profile_views','image')

class BlogSerializerWeb(serializers.ModelSerializer):
    author = AuthorSerializerWeb()
    class Meta:
        model = Blog
        fields = ('id','title','content','author','blog_views','status','image','created_at')