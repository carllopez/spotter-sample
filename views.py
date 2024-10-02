# app/users/views.py
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import KuhlUser
from .serializers import KuhlUserPermissionsSerializer


class KuhlUserPermissionsList(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return KuhlUser.objects.get(pk=pk)
        except KuhlUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = KuhlUserPermissionsSerializer(user)
        return Response(serializer.data)
