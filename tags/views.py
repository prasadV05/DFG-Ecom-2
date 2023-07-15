from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tags.models import Tags
from tags.serializers import WriteTagsSerializers, ReadTagsSerializers
from django.utils.text import slugify

class CreateTagViews(APIView):
    
    def post(self, request):
        serializer = WriteTagsSerializers(data= request.data)
        if serializer.is_valid():
            # if the serializer is valid we create the tag from valid data
            name = serializer.validated_data.get('name')
            tag_object = Tags.objects.create(
                name = name,
                slug=slugify(name)
            )
            json_data = ReadTagsSerializers(instance=tag_object).data
            return Response(json_data, status=status.HTTP_201_CREATED)
        else:
            # return the serializer error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailTagView(APIView):
    def get(self,request,slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            response_data =ReadTagsSerializers(instance=tag_object).data 
            return Response(response_data, status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message": "Tag not found"}, status=status.HTTP_404_NOT_FOUND)
        except Tags.MultipleObjectsReturened:
            return Response({"message": "multiple tags exist for the given slug"}, status=status.HTTP_400_BAD_REQUEST)