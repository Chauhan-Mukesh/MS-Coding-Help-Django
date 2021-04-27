from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    sub_category = serializers.StringRelatedField()
    date_added = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Post
        fields = ('id',
                  'post_title',
                  'sub_category',
                  "get_absolute_url",
                  'slug',
                  'post_description',
                  "get_image",
                  "get_thumbnail",
                  "date_added"
                  )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  "get_absolute_url",
                  )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id',
                  'name',
                  'get_image',
                  "get_absolute_url",
                  )
