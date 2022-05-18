from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only='True'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'post')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field='username')
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username',
    )

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return data

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(queryset=Follow.objects.all(),
                      fields=['user', 'following'])]
