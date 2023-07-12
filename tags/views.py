from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tags.models import Tags
from tags.serializers import WriteTagsSerializers, ReadTagsSerializers
from django.db.backends import slugify

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
            return Response(json_data, status=status.HHTP_201_CREATE)
        else:
            # return the serializer error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

