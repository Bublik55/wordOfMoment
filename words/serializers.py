from django.contrib.auth.models import User, Group
from .models import Word
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class WordSerializer(serializers.HyperlinkedModelSerializer):
  model = Word
  fields = ['owner_id', 'content', 'count']
  owner_id = serializers.IntegerField(read_only = True)
  content = serializers.CharField()
  count = serializers.IntegerField(read_only = False)

  def create(self, validated_data):
        """
        Create and return a new `Word` instance, given the validated data.
        """
        return Word.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.owner_id = validated_data.get('owner_id', instance.owner_id)
    instance.content = validated_data.get('content', instance.content)
    instance.count = validated_data.get('count', instance.count)
    return instance
