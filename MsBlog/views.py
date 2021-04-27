from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import *
from .serializers import PostSerializer, CategorySerializer, SubCategorySerializer


class LatestPostsList(APIView):
    def get(self, request):
        post = Post.objects.all().order_by('-date_added')[0:10]
        serializers = PostSerializer(post, many=True)
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