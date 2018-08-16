from django import forms
from .models import Repair, Car


class RepairForm(forms.ModelForm):

    class Meta:
        model = Repair
        fields = ('date', 'area_serviced', 'invoice_num', 'location', 'Car',)


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('owner', 'vin_num', 'license_plate',
                  'serv_hist', 'make', 'model',)
# superuser name caruser1
# pw usedcars
