from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Thread

class ForumView(ListView):
    paginate_by = 2
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order','')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order =='answers':
            queryset = queryset.order_by('-answers')
        tag = self.kwargs.get('tag','')
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context
