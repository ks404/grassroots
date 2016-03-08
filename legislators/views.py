from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from sunlight.services.congress import Congress

from legislators.models import FedCongressPerson
from legislators.serializers import FedCongressPersonSerializer


class FedCongressListView(ListAPIView):
    queryset = FedCongressPerson.objects.all()
    serializer_class = FedCongressPersonSerializer
    paginate_by = 100

def sunlight_zipcode_query(zipcode):
    # Query the sunlight API for federal legislators based on zipcode
    # This is not a view, just a DRYing function
    congress = Congress()
    query = congress.locate_legislators_by_zip(zipcode)

    # Get the Bioguide IDs of the legislators returned
    bioguide_ids = [leg['bioguide_id'] for leg in query]

    #Query the database for all the legislators in that list
    legislators = FedCongressPerson.objects.filter(bioguide_id__in=bioguide_ids)
    return legislators

def enter_zip(request):
    if request.method == 'GET':
        # load index with simple zip form
        return render(request, 'legislators/index.html')
    elif request.method == 'POST':
        # get the zipcode and redirect to the details page
        return redirect('legislators:zip-detail', request.POST['zipcode'])

def zip_detail(request, zipcode):
    if request.method == 'GET':
        # get all legislators and populate the template with them
        legislators = sunlight_zipcode_query(zipcode)
        # render the details template with the legislators in the context
        return render(request, 'legislators/details.html', {'legislators': legislators})

####
# REST API VIEWS
####
@api_view(['GET'])
def federal_zip_lookup(request, zipcode):
    legislators = sunlight_zipcode_query(zipcode)

    #Set up the API response!
    serializer = FedCongressPersonSerializer(legislators, many=True)
    return Response(serializer.data)
