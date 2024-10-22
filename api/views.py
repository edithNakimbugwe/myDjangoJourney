from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BLogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer  
