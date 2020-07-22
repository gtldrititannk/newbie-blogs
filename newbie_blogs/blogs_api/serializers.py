from django.apps import apps
from rest_framework import serializers

blog_model = apps.get_model('blogs', 'Blogs')  # Importing Blog Model.


class BlogSerializer(serializers.ModelSerializer):
    """
     This will serialize the blog data using Blog Model.
    """

    class Meta:
        model = blog_model
        fields = ['author', 'title', 'blog_content',
                  'created_at', 'updated_at'
                  ]

    def update(self, instance, validated_data):
        """
            This method will update the record.
        """
        instance.blog_content = validated_data.get('blog_content', instance.blog_content)
        instance.title = validated_data.get('title', instance.title)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
