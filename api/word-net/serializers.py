from rest_framework import serializers
from .models import WordNet

class WordNetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordNet
        fields = "__all__"
