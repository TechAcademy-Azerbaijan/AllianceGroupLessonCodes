from rest_framework import serializers
from stories.models import Story, Category, Tag, Subscriber


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
            # 'slug',
            'image',
            # 'created_at',
            # 'updated_at'
        )
        read_only_fields = ('author',)

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['author'] = request.user
        return super(StorySerializer, self).validate(attrs)


class StoryListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'description',
            'category',
            'author',
            'tags',
            # 'slug',
            # 'image',
            # 'created_at',
            # 'updated_at'
        )
        read_only_fields = ('author',)


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
