from django import forms

from apps.test_case.models import TestCase as Cases
class CaseForm(forms.Form):
    case_num = forms.CharField(max_length=20, required=True, label='用例编号',empty_value='111',
                               error_messages={
                                   'required': '用例编号不能为空',
                                   'invalid': '请重新输入用例编号'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入测试编号'}),
                               )
    name = forms.CharField(max_length=20, required=True, label='用例标题',empty_value='111',
                           error_messages={
                               'required': '用例标题不能为空',
                               'invalid': '请重新输入用例标题'
                           },
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入测试编号'}),
                           )
    type = forms.CharField(widget=forms.Select(choices=[],
                                               attrs={'class': 'selectpicker  bla bli form-control',
                                                      'data-live-search': 'true',
                                                      'style': 'display: none'}), label='用例类型')
    level = forms.CharField(widget=forms.Select(choices=[],
                                                attrs={'class': 'selectpicker  bla bli form-control',
                                                       'data-live-search': 'true',
                                                       'style': 'display: none'}), label='优先级')

    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.choices = Cases.case_type
        self.fields['level'].widget.choices = Cases.case_level