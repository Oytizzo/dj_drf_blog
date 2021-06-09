from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def create(self, validated_data):
        post = Post(
            title=validated_data['title'],
            content=validated_data['content'],
            author=self.context['request'].user
        )
        post.save()
        return post
