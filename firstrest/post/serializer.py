from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id','title','body']
        fields ='__all__'
        write_only_fields =('title',)
