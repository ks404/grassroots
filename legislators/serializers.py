from rest_framework import serializers
from legislators.models import FedCongressPerson

class FedCongressPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FedCongressPerson
        fields = ('birthday',
                  'facebook_id',
                  'fax',
                  'first_name',
                  'gender',
                  'last_name',
                  'in_office',
                  'middle_name',
                  'name_suffix',
                  'nickname',
                  'party',
                  'phone',
                  'state',
                  'state_name',
                  'term_end',
                  'term_start',
                  'title',
                  'twitter_id',
                  'website',
                  'district',
                  'bioguide_id',
                  'chamber',
                  'contact_form',
                  'crp_id',
                  'govtrack_id',
                  'leadership_role',
                  'oc_email',
                  'ocd_id',
                  'office',
                  'thomas_id',
                  )
