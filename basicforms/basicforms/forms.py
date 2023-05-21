from django import forms
from django.core import validators

#def check_for_a(value):
 #   if value[0].lower() !='a':
#        raise forms.ValidationError("Name should start with A")
class FormName(forms.Form):
    name = forms.CharField() #validators=[check_for_a]
    email=forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure email is matched!!")
    #botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

   # def clean_botcatcher(self):
   #      botcatcher = self.cleaned_data['botcatcher']
   #      if len(botcatcher) > 0 :
   #          raise forms.ValidationError("GOTCHA BOT")
   #      return botcatcher