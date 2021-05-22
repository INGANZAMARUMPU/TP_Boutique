from django.shortcuts import render
from django.http import HttpResponseNotFound

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from ranged_response import RangedFileResponse

import os, mimetypes

from .models import *
from .serializers import *


def video_stream(request, video_file):
	_file = "music/" + video_file
	if not os.path.isfile(_file): return HttpResponseNotFound()
	response = RangedFileResponse(
		request, open(_file, 'rb'),
		content_type=mimetypes.guess_type(_file)[0]
	)
	response['Content-Length'] = os.path.getsize(_file)
	return response

class ProductViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	# permission_classes = [IsAuthenticatedOrReadOnly, ]
	permission_classes = []
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class MusicViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	# permission_classes = [IsAuthenticatedOrReadOnly, ]
	permission_classes = []
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class PrixViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	# permission_classes = [IsAuthenticatedOrReadOnly, ]
	permission_classes = []
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

def home(request):
	return render(request, 'index.html', {})