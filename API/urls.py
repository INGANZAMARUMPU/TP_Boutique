from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("product", ProductViewset)
router.register("prix", PrixViewset)
router.register("achat", AchatViewset)
router.register("vente", VenteViewset)
router.register("music", MusicViewset)

urlpatterns = [
	path("", home, name="home"),
	path('music/<str:video_file>', video_stream, name='v_stream'),
	path("api/", include(router.urls)),
	path("login/", CustomAuthToken.as_view()),
]
