from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, PermissionDenied
from .models import Post, Categoria, Comentario
from .forms import PostForm, ComentarioForm
from allauth.socialaccount.models import SocialAccount
from .utils import encode, convertir_datos_comentarios


class ListaPost(ListView):
    """
    Esta clase mustra la lista de posts.
    """
    template_name = 'post/lista_post.html'
    paginate_by = 3
    pagina_actual = None
    context_object_name = 'posts'
    model = Post

    def get(self, request, *args, **kwargs):
        try:
            user = SocialAccount.objects.get(user=request.user)
            print vars(request.user)
            print user.get_avatar_url()
        except:
            pass

        #print request.user.get_avatar_url()

        if 'page' in request.GET:
            self.pagina_actual = int(request.GET['page'])
        else:
            self.pagina_actual = 1

        return super(ListaPost, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListaPost, self).get_context_data(**kwargs)

        if 'categoria' in kwargs:
            categoria = kwargs['categoria']
            objeto_categoria = get_object_or_404(Categoria, filtro=categoria)
            posts = Post.objects.filter(categoria=objeto_categoria.id)
            context['posts'] = posts

        context['categorias'] = Categoria.objects.all()

        if not self.pagina_actual is None:
            context['pagina_actual'] = self.pagina_actual

        return context


class ListaPostCategoria(ListView):

    template_name = 'post/lista_post.html'
    paginate_by = 3
    pagina_actual = None
    context_object_name = 'posts'
    model = Post
    categoria = None

    def get(self, request, *args, **kwargs):
        if 'categoria' in kwargs:
            filtro= kwargs['categoria']
            self.categoria = get_object_or_404(Categoria, filtro=filtro)

        if 'page' in request.GET:
            self.pagina_actual = int(request.GET['page'])
        else:
            self.pagina_actual = 1

        return super(ListaPostCategoria, self).get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        queryset = super(ListaPostCategoria, self).get_queryset()

        if not self.categoria is None:
            queryset = Post.objects.filter(categoria=self.categoria.id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListaPostCategoria, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()

        if not self.pagina_actual is None:
            context['pagina_actual'] = self.pagina_actual

        return context


class VerPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/ver_post.html'
    context_object_name = 'post'
    login_url = reverse_lazy('account_login')
    usuario = None

    def get(self, request, *args, **kwargs):
        self.usuario = str(request.user.id)
        return super(VerPost, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VerPost, self).get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['user_id'] = encode(self.usuario)
        post = kwargs['object']

        comentarios = Comentario.objects.filter(post=post)
        context['comentarios'] = comentarios

        return context


class CrearPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Esta clase crea un nuevo post.
    """

    model = Post
    form_class = PostForm
    template_name = 'post/crear_post.html'
    success_url = reverse_lazy('post:lista')
    login_url = reverse_lazy('account_login')
    success_message = u'El post %(titulo)s ha sido creado exitosamente.'

    def post(self, request, *args, **kwargs):
        id = str(request.user.id)
        request.POST['autor'] = id

        return super(CrearPost, self).post(request, *args, **kwargs)


class EditarPost(SuccessMessageMixin, UpdateView):

    model = Post
    form_class = PostForm
    template_name = 'post/editar_post.html'
    success_url = reverse_lazy('post:lista')

    success_message = u'El post %(titulo)s ha sido editado.'


class EliminarPost(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'post/eliminar.html'
    success_url = reverse_lazy('post:lista')


class CrearComentario(CreateView):
    model = Comentario
    template_name = 'post/crear_comentario.html'
    form_class = ComentarioForm
    success_url = ''


def comentar(request):

    if request.method == 'POST':
        data_form = convertir_datos_comentarios(request.body)

        print data_form

        form = ComentarioForm(data=data_form)

        if form.is_valid():
            form.save()
            return HttpResponse('El comentario se ha guardado.')
        else:
            return HttpResponse('Error al guardar el comentario.')

