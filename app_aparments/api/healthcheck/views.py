from rest_framework.views import APIView
from health_check.views import MainView

class Healthcheck(APIView, MainView):
   pass
  
 