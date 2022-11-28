from django.forms import ModelForm, Select, Textarea, TextInput, CheckboxInput
from .models import TbCssrespondents, TbCssrespondentsDetails, TbQuestions, TbEmployees, TbCmuoffices, Ticket
from django.contrib.auth.models import User


class TbCssrespondentsForm(ModelForm):
    class Meta:
        model = TbCssrespondents
        fields = ['respondentname',
                  'respondenttype',
                  'comments',]


class TbCssrespondentsDetailsForm(ModelForm):
    class Meta:
        model = TbCssrespondentsDetails
        fields = ['qid',
                  'respondentid',
                  'rating',]


class TbQuestionsForm(ModelForm):
    class Meta:
        model = TbQuestions
        fields = ['survey_question', 'display_status',]


class TbEmployeesForm(ModelForm):
    class Meta:
        model = TbEmployees
        fields = ['office_id', 'job_position', 'user', 'middlename', 'image',]
        widgets = {
            'office_id': Select(attrs={
                'class': "form-control",
                'id': "office_id",
                'name': "office_id",
            })
        }


class UserChangeUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = TbEmployees
        fields = ['job_position', 'office_id',]


class TbCmuOfficesForm(ModelForm):
    class Meta:
        model = TbCmuoffices
        fields = ['officename','officecode','is_active',]
        widgets = {
            'officename': Textarea(attrs={
                'class': "form-control",
                'id': "officename",
                'name': "officename",
            }),
            'officecode': TextInput(attrs={
                'class': "form-control",
                'id': "officecode",
                'name': "officecode",
            }),
            'is_active': CheckboxInput(attrs={
                'class': "custom-control-input",
                'id': "is_active",
                'name': "is_active",
                'type': "checkbox"
            }),
        }


class TbCmuOfficesAddForm(ModelForm):
    class Meta:
        model = TbCmuoffices
        fields = ['officename', 'officecode',]
        widgets = {
            'officename': Textarea(attrs={
                'class': "form-control",
                'id': "officename",
                'name': "officename",
            }),
            'officecode': TextInput(attrs={
                'class': "form-control",
                'id': "officecode",
                'name': "officecode",
            }),
        }


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['name','email','title','complaint',]
        widgets = {
            'ticket_no': TextInput(attrs={
                'class': "form-control",
                # 'id': "ticketno",
                # 'name': "ticketno",
            }),
            'title': TextInput(attrs={
                'class': "form-control",
                # 'id': "title",
                # 'name': "title",
                'placeholder': "Enter subject",
            }),
            'name': TextInput(attrs={
                'class': "form-control",
                # 'id': "name",
                # 'name': "name",
                'placeholder': "Enter name of client (optional)",
            }),
            'email': TextInput(attrs={
                'class': "form-control",
                # 'id': "email",
                # 'name': "email",
                'type': "email",
                'placeholder': "Enter email of client",
                'required': True,
            }),
            'complaint': Textarea(attrs={
                'class': "form-control",
                # 'id': "complaint",
                # 'name': "complaint",
                'placeholder': "Enter client's concern",
                'required': True,
            })
        }


class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_no','name','email','title','complaint','status',]
