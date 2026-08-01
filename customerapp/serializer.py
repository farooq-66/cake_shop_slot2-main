from rest_framework import serializers
from .models import Customer_tbl

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_tbl
        fields ='__all__'