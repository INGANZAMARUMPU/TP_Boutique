from django.db import models
from django.utils import timezone

class Product(models.Model):
	name = models.CharField(max_length=32)
	qtt = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.name}({self.qtt})"

class Prix(models.Model):
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	prix_achat = models.IntegerField()
	prix_vente = models.IntegerField()
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.product}(achat:{self.prix_achat} vente:{self.prix_vente})"

class Vente(models.Model):
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	qtt = models.IntegerField(default=0)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.product.name}({self.qtt})"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		produit = self.product
		produit.qtt -= self.qtt
		product.save()

class Achat(models.Model):
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	qtt = models.IntegerField(default=0)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.product.name}({self.qtt})"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		produit = self.product
		produit.qtt += self.qtt
		product.save()



