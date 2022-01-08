from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from docstore.models import Folders, Documents, Topics
from docstore.serializers import FoldersSerializer, DocumentsSerializer, TopicsSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def folders_list(request):
    # GET list of folders, POST a new folder
    if request.method == 'GET':
        folders = Folders.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            folders = folders.filter(name__icontains=name)

        folders_serializer = FoldersSerializer(folders, many=True)
        return JsonResponse(folders_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        folder_data = JSONParser().parse(request)
        folder_serializer = FoldersSerializer(data=folder_data)
        if folder_serializer.is_valid():
            folder_serializer.save()
            return JsonResponse(folder_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(folder_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def folders_detail(request, pk):
    # find folder by pk (id)
    try:
        folder = Folders.objects.get(pk=pk)
        if request.method == 'GET':
            folder_serializer = FoldersSerializer(folder)
            return JsonResponse(folder_serializer.data)
    except Folders.DoesNotExist:
        return JsonResponse({'message': 'The Folder does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def documents_list(request):
    if request.method == 'GET':
        documents = Documents.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            documents = documents.filter(name__icontains=name)

        documents_serializer = DocumentsSerializer(documents, many=True)
        return JsonResponse(documents_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        document_data = JSONParser().parse(request)
        document_serializer = DocumentsSerializer(data=document_data)
        if document_serializer.is_valid():
            document_serializer.save()
            return JsonResponse(document_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def documents_detail(request, pk):
    try:
        document = Documents.objects.get(pk=pk)
        if request.method == 'GET':
            document_serializer = DocumentsSerializer(document)
            return JsonResponse(document_serializer.data)
    except Documents.DoesNotExist:
        return JsonResponse({'message': 'The document does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def topics_list(request):
    if request.method == 'GET':
        topics = Topics.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            topics = topics.filter(name__icontains=name)

        topics_serializer = TopicsSerializer(topics, many=True)
        return JsonResponse(topics_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        topic_data = JSONParser().parse(request)
        topic_serializer = TopicsSerializer(data=topic_data)
        if topic_serializer.is_valid():
            topic_serializer.save()
            return JsonResponse(topic_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(topic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def topics_detail(request, pk):
    try:
        topic = Topics.objects.get(pk=pk)
        if request.method == 'GET':
            topic_serializer = TopicsSerializer(topic)
            return JsonResponse(topic_serializer.data)
    except Topics.DoesNotExist:
        return JsonResponse({'message': 'The topic does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def search_documents(request):
    folder = None
    topic = None
    try:
        folder = Folders.objects.get(name=request.query_params.get('folderName'))
    except Folders.DoesNotExist:
        return JsonResponse({'message': 'The folder does not exist'}, status=status.HTTP_404_NOT_FOUND)
    try:
        topic = Topics.objects.filter(shortDescription=request.query_params.get('shortDescription'), folder=folder)
    except Topics.DoesNotExist:
        return JsonResponse({'message': 'The topic does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        documentList = []
        for tp in topic:
            document_serializer = DocumentsSerializer(tp.document)
            documentList.append(document_serializer.data)

        return JsonResponse(documentList, safe=False)