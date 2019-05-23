from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()



class TaskList(SelectRelatedMixin, generic.ListView):
    model = models.Task
    select_related = ("user",'message')


class UserTasks(generic.ListView):
    model = models.Task
    template_name = "tasks/user_task_list.html"

    def get_queryset(self):
        try:
            self.task_user = User.objects.prefetch_related("tasks").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        # else:
        #     return self.task_user.tasks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_user"] = self.task_user
        return context


class TaskDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Task
    select_related = ("user")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateTask(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.taskForm
    fields = ('message')
    model = models.Task

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Task
    select_related = ("user")
    success_url = reverse_lazy("tasks:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Task Deleted")
        return super().delete(*args, **kwargs)
