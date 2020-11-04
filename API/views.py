from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from .models import *
from .serializers import *

class ProductViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class PrixViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	queryset = Prix.objects.all()
	serializer_class = PrixSerializer

class VenteViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	queryset = Vente.objects.all()
	serializer_class = VenteSerializer

class AchatViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	queryset = Achat.objects.all()
	serializer_class = AchatSerializer

class CustomAuthToken(ObtainAuthToken):
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={'request': request})
		serializer.is_valid(raise_exception=True);
		user = serializer.validated_data['user'];
		token, created = Token.objects.get_or_create(user=user);
		return Response({'token': token.key,})