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
	product = serializers.SerializerMethodField()
	product_id = serializers.SerializerMethodField()

	def get_product(self, obj):
		return obj.product.name

	def get_product_id(self, obj):
		return obj.product.id

	class Meta:
		model = Vente
		fields = "id", "qtt", "date", "product", "product_id"

class AchatSerializer(serializers.ModelSerializer):
	product = serializers.SerializerMethodField()
	product_id = serializers.SerializerMethodField()

	def get_product(self, obj):
		return obj.product.name

	def get_product_id(self, obj):
		return obj.product.id

	class Meta:
		model = Achat
		fields = "id", "qtt", "date", "product", "product_id"