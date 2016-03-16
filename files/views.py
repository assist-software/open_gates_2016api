from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .serializers import AppFileSerializer
from .models import AppFile


class AppFileView(generics.CreateAPIView):
    serializer_class = AppFileSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser,)

    def post(self, request, format=None):
        serializer = AppFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppFileViewSet(viewsets.ModelViewSet):
    queryset = AppFile.objects.all()
    serializer_class = AppFileSerializer


class AppFileList(generics.ListAPIView):
    serializer_class = AppFileSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_pk = self.kwargs['pk']
        return AppFile.objects.filter(user__pk=user_pk)
