from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from datetime import date
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm
from .models import Todo


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/home.html'
    login_url = '/login/'  # URL para redirecionar se não estiver logado


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todos/create.html'
    fields = ['title', 'deadline']
    success_url = reverse_lazy('list')
    login_url = '/login/'

    def form_valid(self, form):
        # Associa a tarefa ao usuário logado antes de salvar
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todos/update.html'
    fields = ['title', 'deadline']
    success_url = reverse_lazy('list')
    login_url = '/login/'


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('list')
    login_url = '/login/'


class TodoFinishView(LoginRequiredMixin, View):
    model = Todo
    login_url = '/login/'

    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished = date.today()  # Mark as finished with today's date
        todo.save()
        return redirect('list')


# A view de registro não deve ter login_required pois é para novos usuários
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o registro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('list')  # Mudei para redirecionar para a lista de todos
    else:
        form = UserRegisterForm()
    
    return render(request, 'todos/register.html', {'form': form})


# Adicione esta view para a página de login (opcional)
@login_required(login_url='/login/')
def pagina_inicial(request):
    return redirect('list')  # Redireciona para a lista de todos após login
class CustomLoginView(LoginView):
    template_name = 'todos/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        # Autentica o usuário
        email = form.cleaned_data.get('username')  # Lembre-se que username é o email no seu caso
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, f'Bem-vindo(a) de volta, {user.name}!')
            return redirect('list')
        else:
            messages.error(self.request, 'E-mail ou senha incorretos.')
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('list')

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Você foi desconectado com sucesso.")
        logout(request)
        return redirect('login')  # Redireciona para a página de login após logout    