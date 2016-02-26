from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from legislators.models import FedCongressPerson
from legislators.serializers import FedCongressPersonSerializer

from sunlight.services.congress import Congress


# Create your views here.
class FedCongressListView(ListAPIView):
    queryset = FedCongressPerson.objects.all()
    serializer_class = FedCongressPersonSerializer
    paginate_by = 100

@api_view(['GET'])
def federal_zip_lookup(request, zipcode):
    if request.method == 'GET':
        # Query the sunlight API for federal legislators based on zipcode
        congress = Congress()
        query = congress.locate_legislators_by_zip(zipcode)

        # Get the Bioguide IDs of the legislators returned
        bioguide_ids = [leg['bioguide_id'] for leg in query]

        #Query the database for all the legislators in that list
        legislators = FedCongressPerson.objects.filter(bioguide_id__in=bioguide_ids)

        #Set up the API response!
        serializer = FedCongressPersonSerializer(legislators, many=True)
        return Response(serializer.data)

