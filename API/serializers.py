from rest_framework import serializers

from .models import *

class PrixSerializer(serializers.ModelSerializer):
	class Meta:
		model = Prix
		fields = "__all__"

class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Music
		fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
	prix = serializers.SerializerMethodField()

	def get_prix(self, obj):
		prix = Prix.objects.filter(product=obj.id).last()
		return PrixSerializer(prix).data

	class Meta:
		model = Product
		fields = "__all__"

class VenteSerializer(serializers.ModelSerializer):
	product = serializers.SerializerMethodField()
	product_id = serializers.SerializerMethodField()
	prix = serializers.SerializerMethodField()

	def get_product(self, obj):
		return obj.product.name

	def get_product_id(self, obj):
		return obj.product.id

	def get_prix(self, obj):
		prix = Prix.objects.filter(product=obj.product).last()
		if prix:
			return prix.prix_vente
		return 0

	class Meta:
		model = Vente
		fields = "__all__"

class AchatSerializer(serializers.ModelSerializer):
	product = serializers.SerializerMethodField()
	product_id = serializers.SerializerMethodField()
	prix = serializers.SerializerMethodField()

	def get_product(self, obj):
		return obj.product.name

	def get_product_id(self, obj):
		return obj.product.id

	def get_prix(self, obj):
		prix = Prix.objects.filter(product=obj.product).last()
		if prix:
			return prix.prix_achat
		return 0;

	class Meta:
		model = Achat
		fields = "__all__"