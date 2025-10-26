from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from .models import News
from .forms import NewsModelForm
from .filters import NewsFilter

class NewsListView(FilterView):
    model = News
    template_name = "custom_blog/news.html"
    context_object_name = "news_list"
    filterset_class = NewsFilter
    paginate_by = 3

    def get_queryset(self):
        # показываем только активные новости
        return News.objects.filter(is_active=True).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости"
        # берём фильтр из встроенного filterset
        context["filter"] = context.get("filterset")
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = "custom_blog/news_detail.html"
    context_object_name = "news"

class NewsCreateView(CreateView):
    model = News
    form_class = NewsModelForm
    template_name = "custom_blog/news_form.html"
    success_url = reverse_lazy("news_list")

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsModelForm
    template_name = "custom_blog/news_form.html"
    success_url = reverse_lazy("news_list")

class NewsDeleteView(DeleteView):
    model = News
    template_name = "custom_blog/news_confirm_delete.html"
    success_url = reverse_lazy("news_list")
