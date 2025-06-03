from rest_framework.response import Response
from rest_framework import status

def validate_id(id):

    if id.isdigit():
        id = int(id)

    if not isinstance(id,int):
        return None,Response({"error_message":"The id must be an integer value"},status=status.HTTP_400_BAD_REQUEST)
    if  not id > 0:
        return None,Response({"error_message":"The id value must be greater than 0"},status=status.HTTP_400_BAD_REQUEST)
    
    return id,None