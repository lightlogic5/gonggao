from django.forms import ModelForm
from .models import articale


class articaleForm(ModelForm):
    class Meta:
        model = articale
        fields = '__all__'



# class articaleForm(ModelForm):
#     class Meta:
#         model = articale
#
#     def __init__ (self, *args, **kwargs):
#         brand = kwargs.pop("brand")
#         super(articaleForm, self).__init__(*args, **kwargs)
#         self.fields["a_tag"].widget = forms.widgets.CheckboxSelectMultiple()
#         self.fields["a_tag"].help_text = "请选择多个适合标签"
#         self.fields["a_tag"].queryset = tags.objects.all()
#         self.fields["a_project"].widget = forms.widgets.Select()
#         self.fields["a_project"].help_text = "请选择所属项目"
#         self.fields["a_project"].queryset = project.objects.all()

