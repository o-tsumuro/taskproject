from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse

class FormAndListView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        order = self.request.GET.get('order', 'pk')
        
        order_options = {
            'pk': 'pk',
            'priority': '-priority',
            'date': 'date',
        }

        context['tasks'] = Task.objects.filter(user=self.request.user).order_by(order_options.get(order, 'pk'))
        context['form'] = kwargs.get('form', TaskForm())
        context['is_guest_user'] = self.request.user.username.startswith("guest_")
        context['selected_order'] = order
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        postdata = form.save(commit=False)
        if form.is_valid():
            postdata.user = self.request.user
            form.save()
            return redirect('taskapp:index')
        return render(request, self.template_name, self.get_context_data(form=form))


def task_detail(request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_detail.html', {'task': task})

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return JsonResponse({'message': 'タスクが削除されました'})
    return JsonResponse({'message': '無効なリクエスト'}, status=400)