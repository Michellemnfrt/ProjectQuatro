from django import forms
from .models import repair, Car


class repairForm(forms.ModelForm):

    class Meta:
        model = repair
        fields = ('date', 'area_serviced', 'invoice_num', 'location', 'car',)


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('owner', 'vin_num', 'license_plate',
                  'serv_hist', 'make', 'model',)
# superuser name caruser1
# pw usedcars
