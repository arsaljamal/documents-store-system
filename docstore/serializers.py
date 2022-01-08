from rest_framework import serializers
from docstore.models import Folders, Documents, Topics


class FoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folders
        fields = ('id',
                  'name',
                  'size',)


class DocumentsSerializer(serializers.ModelSerializer):
    folder = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Folders.objects.all())

    class Meta:
        model = Documents
        fields = ('id',
                  'name',
                  'size',
                  'folder',)


class TopicsSerializer(serializers.ModelSerializer):
    folder = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Folders.objects.all())
    document = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Documents.objects.all())

    class Meta:
        model = Topics
        fields = ('id',
                  'longDescription',
                  'shortDescription',
                  'document',
                  'folder',)