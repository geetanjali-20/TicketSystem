from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your forms here.
class PersonalDataForm(UserCreationForm):
    Name = forms.CharField(label='Your name',required=True)
    Gender = forms.TypedChoiceField(
       label="Choose Gender",
       choices=((0, "Male"), (1, "Female"), (2, "Others")),
       coerce=lambda x: bool(int(x)),
       widget=forms.RadioSelect,
       initial='0',
       required=True)

    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("Name","Gender","username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(PersonalDataForm, self).save(commit=False)
        user.email = self.cleaned_data['email'],
        user.FirstName = self.cleaned_data['Name'],
        # user.Age = self.cleaned_data['Age']
        if commit:
            user.save()
        return user