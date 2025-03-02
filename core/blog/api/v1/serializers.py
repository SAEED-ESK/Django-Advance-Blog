from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    post_url = serializers.SerializerMethodField()
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'post_url', 'status', 'category', 'published_date']
        read_only_fields = ['author']

    def get_post_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('post_url', None)
        else:
            rep.pop('content')
        rep['category'] = CategorySerializer(instance.category, context={'request': request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
