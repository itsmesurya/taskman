from django import forms

from tasks import models


class TaskForm(forms.ModelForm):
    class Meta:
        fields = ('message','created_at')
        model = models.Task

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)
    #     super().__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields["group"].queryset = (
    #             models.Group.objects.filter(
    #                 pk__in=user.groups.values_list("group__pk")
    #             )
    #         )
