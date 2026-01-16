from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from health_check.views import MainView

class Healthcheck(APIView, MainView):
   pass
  
 