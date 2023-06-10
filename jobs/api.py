from .serializers import JobSerializers
from rest_framework import generics
from rest_framework.response import Response
from .models import Job



class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers



class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    lookup_field = 'id'