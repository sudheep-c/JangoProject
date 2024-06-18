from django import forms
from.models import Booking
class DateInput(forms.DateInput):
    input_type='date'
    
class Bookingform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'Booking_date':DateInput(),
        }

        labels={
            'cus_name':"Customer Name",
            'cus_ph':"Customer Phone",
            'name':"Event Name",
            'Booking_date':"Booking Date"
        }