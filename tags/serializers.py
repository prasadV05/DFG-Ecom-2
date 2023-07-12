from rest_framework import serializers
from tags.models import Tags

# serializer is used to convert orm data into json
#write operation into database
class WriteTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']





# serializer is used to convert orm data into json
#read operation into database
class ReadTagsSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tags
        fields = ['id', 'name','slug','created_at']
