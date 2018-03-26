from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(widget =  forms.TextInput(attrs={'class':'form-control','placeholder':'Name', 'type':'text'}), required=True)
    contact_email = forms.EmailField(widget =  forms.TextInput(attrs={'class':'form-control','placeholder':'Email', 'type':'email'}), required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs = {'placeholder' : 'Comment', 'class' : 'form-control', 'rows' : '5'})
    )