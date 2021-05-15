from django import forms


class contactformemail(forms.form):
    frommail-form.EmailField(required=True)
    subject-form.CharField(required=True)
    message-form.Charfield(required=True)


