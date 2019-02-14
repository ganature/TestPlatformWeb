from django import forms

from apps.project.models import Project


class ProjectForm(forms.Form):
    name = forms.CharField(required=True, empty_value='',
                           error_messages={'required': '项目名称不能为空', 'invalid': '请输入正确的测试名称'},
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入项目名称'}),
                           label='项目名称', label_suffix=':'

                           )

    type = forms.CharField(widget=forms.Select(choices=[], attrs={'class': 'selectpicker  bla bli form-control',
                                                                  'data-live-search': 'true',
                                                                  'style': 'display: none'}), label='项目类型')

    detail = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-success', 'placeholder': '请输入备注'}), label='备注')
    creator = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'style': "display:None"}),
                              label=' ')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.choices = Project.project_type
