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
                  "date_added",
                  'name'
                  )

    name = serializers.SerializerMethodField('get_subcategory_name')

    def get_subcategory_name(self, obj):
        return obj.sub_category.name


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  "get_absolute_url",
                  )


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = SubCategory
        fields = ('id',
                  'name',
                  'get_image',
                  "get_absolute_url",
                  "category"
                  )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'subject',
            'message'
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            'id',
            'post',
            'user',
            'comment',
            'date',
        )


class GetCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comments
        fields = (
            'id',
            'post',
            'user',
            'comment',
            'date',
        )
