from rest_framework import serializers
from .models import cake_tbl

class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = cake_tbl
        fields = '__all__'