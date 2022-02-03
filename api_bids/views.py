from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.http import Http404

from .serializers import CategorySerializer, AuctionSerializer, CommentSerializer, ViewCommentsSerializer
from .models import Category, Auction, Comment

# Create your views here.

class CategoryList(APIView):

    """ 
    List all categories, or create a new one
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AuctionList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['user_id'] = request.user.id
        print(request.data)
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AuctionDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            auction = Auction.objects.get(pk=pk)
            serializer = AuctionSerializer(auction, many=False)
            comments = Comment.objects.filter(auction=pk)
            comm_serializer = ViewCommentsSerializer(comments, many=True)
            response = {
                'auction': serializer.data,
                'comments': comm_serializer.data
            }
            return Response(response)
        except:
            return Response({'message': 'Auction not found'}, status=404)


