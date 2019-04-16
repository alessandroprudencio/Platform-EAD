from django.shortcuts import render,redirect

from django.views.generic import TemplateView, ListView,DetailView

from .models import Thread

from django.contrib import messages

from .forms import ReplyForm    

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

class ThreadView(DetailView):

    model = Thread
    template_name = 'thread.html'

    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, *kwargs)
        if not self.request.user.is_authenticated or  (self.object.author != self.request.user):
            self.object.views = self.object.views + 1
            self.object.save()
        return response

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = ReplyForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Para responder a dúvida é necessario estar logado')
            return redirect(self.request.path)
        self.object = self.get_object()
        context = self.get_context_data(object = self.object)
        form = context['form']
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = self.object
            reply.author = self.request.user
            reply.save()
            messages.success(self.request, 'Reposta adicionado com sucesso!')
            context['form'] = ReplyForm()
        return self.render_to_response(context)