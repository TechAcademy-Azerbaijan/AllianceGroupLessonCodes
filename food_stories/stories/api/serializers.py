from rest_framework import serializers
from stories.models import Story, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'created_at',
            'updated_at',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at'
        )


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'description',
            'category',
            'author',
            'tags',
            'title',
            'slug',
            'description',
            'image',
            'created_at',
            'updated_at'
        )


class StoryListSerializer(StorySerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)