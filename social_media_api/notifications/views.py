from django.shortcuts import render
from .models import Notification
from django.contrib.contenttypes.models import ContentType 
from rest_framework.response import Response 

# Create your views here.
@api_view(['GET'])
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False)
    return Response({'notifications': list(notifications.values())})
