from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class PrixSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prix
		fields = "__all__"

class VenteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vente
		fields = "__all__"

class AchatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Achat
		fields = "__all__"