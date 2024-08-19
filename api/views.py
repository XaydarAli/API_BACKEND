from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from .models import Advisor,Author,Blog,Review,Service
from .serializers import AuthorSerializerWeb,BlogSerializerWeb,AdvisorSerializerWeb,ReviewSerializerWeb,ServiceSerializerWeb
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
class AdvisorViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AdvisorSerializerWeb
    def get_queryset(self):
        return Advisor.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'slug')



    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    # def get(self, request):
    #     query=self.get_queryset()
    #     search_data=request.query_params.get("search")
    #     if search_data is  not None:
    #         query=query.filter(name__icontains=search_data) | query.filter(slug__icontains=search_data)
    #     serializer = AdvisorSerializerWeb(query, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET', ])
    def profile_views(self, request, *args, **kwargs):
        advisor = self.get_object()
        advisor.profile_views += 1
        advisor.save()
        return Response(data={"Profile Viewed": advisor.profile_views})


    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        advisors = self.get_queryset().order_by('-profile_views')[:3]
        serializer = AdvisorSerializerWeb(advisors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def not_viewed(self, request, *args, **kwargs):
        advisors = self.get_queryset().filter(profile_views=0)
        serializer = AdvisorSerializerWeb(advisors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ServiceViewSetWeb(viewsets.ModelViewSet):
    queryset = Service.objects.filter(status='pb')
    serializer_class = ServiceSerializerWeb
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'slug')

    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)




    @action(detail=True, methods=['GET', ])
    def num_of_reviews(self, request, *args, **kwargs):
        service= self.get_object()
        service.reviews_count += 1
        service.save()
        return Response(data={"Service viewed": service.reviews_count})

    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        services = self.get_queryset().order_by('-reviews_count')[:3]
        serializer = ServiceSerializerWeb(services, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def not_reviewed(self, request, *args, **kwargs):
        services = self.get_queryset().filter(reviews_count=0)
        serializer = ServiceSerializerWeb(services, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)





    @action(detail=False, methods=['GET', ])
    def to_draft(self, request, *args, **kwargs):
        services = self.get_queryset()
        for service in services:
            service.pb_to_df()
        return Response(data={"message": "All services  are drafted "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        services = Service.objects.all()
        for service in services:
            service.df_to_pb()
        return Response(data={"message": "All services  are published "}, status=status.HTTP_200_OK)




class ReviewViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ReviewSerializerWeb
    def get_queryset(self):
        return Review.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'slug')

    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET', ])
    def like(self, request, *args, **kwargs):
        review = self.get_object()
        review.likes += 1
        review.save()
        return Response(data={"Likes": review.likes})

    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        reviews = self.get_queryset().order_by('-likes')[:3]
        serializer = ReviewSerializerWeb(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




    @action(detail=False, methods=['GET', ])
    def not_liked(self, request, *args, **kwargs):
        reviews = self.get_queryset().filter(likes=0)
        serializer = ReviewSerializerWeb(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class AuthorViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AuthorSerializerWeb
    def get_queryset(self):
        return Author.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ('nickname', 'slug')

    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET', ])
    def profile_views(self, request, *args, **kwargs):
        author = self.get_object()
        author.profile_views += 1
        author.save()
        return Response(data={"Profile Viewed": author.profile_views})

    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        authors = self.get_queryset().order_by('-profile_views')[:3]
        serializer = AuthorSerializerWeb(authors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['GET', ])
    def not_viewed(self, request, *args, **kwargs):
        authors = self.get_queryset().filter(profile_views=0)
        serializer = AuthorSerializerWeb(authors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class BlogViewSetWeb(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(status='pb')
    serializer_class = BlogSerializerWeb
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'slug')

    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    @action(detail=True, methods=['GET', ])
    def blog_views(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.blog_views += 1
        blog.save()
        return Response(data={"Blog Viewed": blog.blog_views})

    @action(detail=False, methods=['GET', ])
    def top(self, request, *args, **kwargs):
        blogs = self.get_queryset().order_by('-blog_views')[:3]
        serializer = BlogSerializerWeb(blogs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_draft(self, request, *args, **kwargs):
        blogs = self.get_queryset()
        for blog in blogs:
            blog.pb_to_df()
        return Response(data={"message": "All blog posts  are drafted "}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ])
    def to_publish(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        for blog in blogs:
            blog.df_to_pb()
        return Response(data={"message": "All blogs  are published "}, status=status.HTTP_200_OK)





