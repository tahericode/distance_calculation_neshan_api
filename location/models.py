from django.db import models
from django.contrib.gis.db import models as gis_models
from .utils import neshan_distance


class Cargo(models.Model):
    origin_location = gis_models.PointField(verbose_name='مختصات مکان مبدا')
    destination_location = gis_models.PointField(verbose_name=('مختصات مکان مقصد'))
    travel_distance = models.FloatField(verbose_name=("فاصله سفر"), default=0.0, help_text=("پس از ذخیره تغییرات به روز می شود"))

    def save(self, *args, **kwargs):
        # Get The Origin Lat & Long
        long_origin = self.origin_location[1]
        lat_origin = self.origin_location[0]
        # Get The Destination Lat & Long
        long_destination = self.destination_location[1]
        lat_destination = self.destination_location[0]
        # Calculate Final Distance Base On Neshan Api
        final_distance = neshan_distance(long_origin, lat_origin, long_destination, lat_destination)
        self.travel_distance = final_distance 
        return super(Cargo, self).save(*args, **kwargs)
