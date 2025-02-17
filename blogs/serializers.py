from rest_framework import serializers
from .models import postComment

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = postComment
        fields = ['art_id', 'comment_user', 'comment_post', 'comment_text']