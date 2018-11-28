from jpbusformat.models.agency import Agency
from jpbusformat.models.fare_attribute import FareAttribute
from jpbusformat.models.fare_rule import FareRule
from jpbusformat.models.feed_info import FeedInfo
from jpbusformat.models.office import Office
from jpbusformat.models.route import Route
from jpbusformat.models.service import Service
from jpbusformat.models.service_date import ServiceDate
from jpbusformat.models.shape import Shape
from jpbusformat.models.stop import Stop
from jpbusformat.models.stop_time import StopTime
from jpbusformat.models.transfer import Transfer
from jpbusformat.models.translation import Translation
from jpbusformat.models.trip import Trip
from rest_framework import viewsets

from gtfs.serializers import (
    AgencySerializer,
    StopSerializer,
    StopTimeSerializer,
    RouteSerializer,
    ServiceSerializer,
    ServiceDateSerializer,
    TripSerializer,
    OfficeSerializer,
    FareAttributeSerializer,
    FareRuleSerializer,
    ShapeSerializer,
    TransferSerializer,
    FeedInfoSerializer,
    TranslationSerializer,
)
from settings.viewsets import ListModelViewSet


class AgencyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class StopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


class StopTimeViewSet(ListModelViewSet):
    serializer_class = StopTimeSerializer

    def get_queryset(self):
        if self.kwargs.get("stop_pk"):
            return StopTime.objects.filter(stop__id=self.kwargs["stop_pk"]).order_by(
                "departure_time"
            )
        elif self.kwargs.get("trip_pk"):
            return StopTime.objects.filter(trip__id=self.kwargs["trip_pk"]).order_by(
                "sequence"
            )


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDateViewSet(ListModelViewSet):
    serializer_class = ServiceDateSerializer

    def get_queryset(self):
        return ServiceDate.objects.filter(service_id=self.kwargs["service_pk"])


class TripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        if self.kwargs.get("route_pk"):
            return Trip.objects.filter(route_id=self.kwargs["route_pk"])
        else:
            return Trip.objects.all()


class OfficeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def filter_queryset(self, queryset):
        if self.kwargs.get("trip_pk"):
            return queryset.filter(trip__id=self.kwargs["trip_pk"])
        else:
            return queryset


class FareAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FareAttribute.objects.all()
    serializer_class = FareAttributeSerializer


class FareRuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FareRule.objects.all()
    serializer_class = FareRuleSerializer


class ShapeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer


class TransferViewSet(ListModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    search_fields = ("from_stop", "to_stop")


class FeedInfoViewSet(ListModelViewSet):
    queryset = FeedInfo.objects.all()
    serializer_class = FeedInfoSerializer


class TranslationViewSet(ListModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    search_fields = ("trans_id", "lang")
