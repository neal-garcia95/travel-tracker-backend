from rest_framework import serializers
from .models import Entry, Trip

class TripSerializer(serializers.HyperlinkedModelSerializer):
    entry = serializers.HyperlinkedRelatedField(
        view_name='entry_detail',
        many=True,
        read_only=True
    )

    trip_url = serializers.ModelSerializer.serializer_url_field(
            view_name = 'trip_detail'
    )

    class Meta:
        model = Trip
        fields = ('id', 'location', 'start_date', 'end_date', 'entry', 'trip_url',)

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        view_name='trip_detail',
        many = False,
        read_only=True
    )

    trip_id = serializers.PrimaryKeyRelatedField(
            queryset = Trip.objects.all(),
            source = 'trip'
    )

    class Meta:
        model = Entry
        fields = ('photo_url', 'body', 'date', 'trip', 'trip_id')