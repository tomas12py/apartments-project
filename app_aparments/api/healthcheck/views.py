from rest_framework.permissions import IsAuthenticated
from health_check.views import MainView



class Healthcheck(MainView):
    
 permissions = [IsAuthenticated]