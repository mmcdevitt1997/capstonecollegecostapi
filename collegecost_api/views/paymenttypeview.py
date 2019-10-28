"""View module for handling requests about cost type"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from collegecost_api.models import *

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentTypeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='paymenttype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'color', 'interst', 'terminyear', 'extramonthly')
        depth = 0

class PaymentType(ViewSet):
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_paymenttype = PaymentTypeModel()
        new_paymenttype.name = request.data["name"]
        new_paymenttype.color = request.data["color"]
        new_paymenttype.interst = request.data["interst"]
        new_paymenttype.terminyear = request.data["terminyear"]
        new_paymenttype.terminyear = request.data["extramonthly"]
        serializer = PaymentTypeSerializer(new_paymenttype, context={'request': request})
        return Response(serializer.data)

def retrieve(self, request, pk=None):
    """Handle GET requests for single park area
    Returns:
        Response -- JSON serialized park area instance
    """
    try:
       paymenttype = PaymentTypeModel.objects.get(pk=pk)
       serializer = PaymentTypeSerializer(paymenttype, context={'request': request})
       return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)

def destroy(self, request, pk=None):
    """Handle DELETE requests for a single product are
    Returns:
        Response -- 200, 404, or 500 status code
    """
    try:
        paymenttype = PaymentTypeModel.objects.get(pk=pk)
        paymenttype.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    except PaymentTypeModel.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    except Exception as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def list(self, request):
    """Handle GET requests to payment types resource

    Returns:
        Response -- JSON serialized list of payment types
    """
    paymenttypes = CollegeModel.object.all()
    name = self.request.query_params.get('name', None)
    color = self.request.query_params.get('color', None)
    interst = self.request.query_params.get('interst', None)
    terminyear = self.request.query_params.get('terminyear', None)
    extramonthly = self.request.query_params.get('extramonthly', None)

    serializer = PaymentTypeSerializer(
        paymenttypes, many=True, context={'request': request})
    return Response(serializer.data)
