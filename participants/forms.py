from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import PreEvent


class PreEventForm(forms.ModelForm):
    Member1_contact_no = PhoneNumberField(
        help_text='Add country code before the contact no.')
    Member1_are_you_a_thapar_student = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                              choices=((True, 'Yes'), (False, 'No')))

    Member2_contact_no = PhoneNumberField(
        help_text='Add country code before the contact no.',required = False)
    Member2_are_you_a_thapar_student = forms.TypedChoiceField(
                                                              choices=((True, 'Yes'), (False, 'No')))

    class Meta:
        model = PreEvent
        fields = ['Team_name', 'Member1_name', 'Member1_email', 'Member1_contact_no', 'Member1_roll_no', 'Member1_are_you_a_thapar_student', 'Member1_year_of_study', 
                  'Member2_name', 'Member2_email', 'Member2_contact_no', 'Member2_roll_no', 'Member2_are_you_a_thapar_student', 'Member2_year_of_study']
    

    def init(self, args, **kwargs):
        super(PreEventForm, self).init(args, **kwargs)
        self.fields['Member2_contact_no','Member2_name','Member2_email','Member2_year_of_study'].required = False