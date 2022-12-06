from django import forms


class GenerateCartForm(forms.Form):
    count_renge_cart = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date_end_cart = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        )
    )
