from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

class GetWhishList(generics.ListAPIView):
    serializer_class = serializers.WhishListSerializers
    permisson_classes = [IsAuthenticated]

    def get_queryset(self):

        return models.Whishlists.objects.filter(userId = self.request.user)
    
class ToggleWishList(APIView):
    permisson_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        product_id = request.query_params.get('id')

        if not user_id or not product_id:
            return Response({'message': 'Invalid Request a user id and product id is required'}, status = status.HTTP_400_BAD_REQUEST)
        
        try :
            product = models.Product.objects.get(id=product_id)
        except models.Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status = status.HTTP_404_BAD_REQUEST)
        
        whishlist_item, created = models.Whishlists.objects.get_or_create(userId = request.user, product = product)

        if created:
            return Response({'message': 'Product addes to whish list'}, status = status.HTTP_201_CREATED)
        else :
            whishlist_item.delete()
            return Response({'message': 'Product removed from whish list'}, status = status.HTTP_204_NO_CONTENT)
