from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
  model = Post  # указываем модель, объекты которой мы будем выводить
  template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
  context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
  queryset = Post.objects.order_by('-dateCreation') # Сортируем от самой свежей по дате создания

class NewsItem(DetailView):
  model = Post
  template_name = 'news_item.html'
  context_object_name = 'news_item'