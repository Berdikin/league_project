from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPassportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].empty_label = 'Регион не выбран'

    class Meta:
        model = passport_date
        fields = ['surname', 'name', 'patronymic', 'series', 'number', 'data_issue', 'division_code',
                  'issued_by', 'date_birth', 'place_birth', 'region']

    def clean_series(self):
        series = self.cleaned_data['series']
        if len(series) > 4:
            raise ValidationError('Серия равна 4 цифрам')

        return series

    def clean_number(self):
        number = self.cleaned_data['number']
        if len(number) > 10:
            raise ValidationError('Номер не может превышать 10 цифр')

        return number

    def clean_division_code(self):
        division_code = self.cleaned_data['division_code']
        if len(division_code) > 6:
            raise ValidationError('Код подразделения равен 6 цифрам')

        return division_code


class AddInsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Тип не выбран'
        self.fields['region_id'].empty_label = 'Регион не выбран'

    class Meta:
        model = insurance
        fields = ['max_payment', 'cost', 'period_start_date', 'period_end_date', 'type', 'client_id',
                  'agent_id', 'region_id']
        #widgets = {
          #  'max_payment': forms.TextInput(attrs={'class': 'form-input'}),
        #    'cost': forms.TextInput(attrs={'class': 'form-input'}),

      #  }
    def clean_cost(self):
        cost = self.cleaned_data['cost']
        if len(cost) > 18:
            raise ValidationError('Сумма не может быть такой большой')

        return cost
