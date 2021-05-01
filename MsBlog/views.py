from django.core import exceptions
from django.core import exceptions
from django.db.models import Q
from django.http import Http404
from rest_framework import status, authentication, permissions, authtoken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import *
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer, ContactUsSerializer, \
    CommentSerializer, GetCommentSerializer


class LatestPostsList(APIView):
    def get(self, request):
        post = Post.objects.all().order_by('-date_added')[0:10]
        serializers = PostSerializer(post, many=True)
        return Response(serializers.data)


class GetCommentsList(APIView):
    def get(self, request):
        comments = Comments.objects.all().order_by('-date')
        serializers = GetCommentSerializer(comments, many=True)
        return Response(serializers.data)


class CategoriesList(APIView):
    def get_object(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            raise Http404

    def get(self, request):
        category = self.get_object().order_by('-name')
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)


class SubCategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return SubCategory.objects.filter(category__slug=category_slug)
        except SubCategory.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        subcategory = self.get_object(category_slug).order_by('id')
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)


class SubCategoryPostList(APIView):
    def get_object(self, sub_category_slug):
        try:
            return Post.objects.filter(sub_category__slug=sub_category_slug).order_by('id')
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, sub_category_slug, format=None):
        posts = self.get_object(sub_category_slug)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get_object(self, sub_category_slug, post_slug):
        try:
            return Post.objects.filter(sub_category__slug=sub_category_slug).get(slug=post_slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, sub_category_slug, post_slug, format=None):
        posts = self.get_object(sub_category_slug, post_slug)
        serializer = PostSerializer(posts, many=False)
        return Response(serializer.data)


@api_view(['POST'])
def ContactUsData(request):
    serializer = ContactUsSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    try:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except exceptions:
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Search(request):
    query = request.data.get('query', '')

    if not query:
        return Response({"products": []})
    else:
        products = Post.objects.filter(Q(post_title__icontains=query) | Q(post_description__icontains=query))
        serializer = PostSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CommentOnPost(request):
    user = Token.objects.get(key=request.data['user'])
    dict = {'post': request.data['post'], 'user': user.user.id, 'comment': request.data['comment']}
    print(dict)
    serializer = CommentSerializer(data=dict)

    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except exceptions:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
