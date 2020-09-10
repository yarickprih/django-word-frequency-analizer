from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import TextForm
from .models import Text


class TextListView(ListView):
    """List View of analized texts."""

    model = Text
    template_name = "word_analizer/text_list.html"


class TextDetailView(DetailView):
    """Detail View of specific analized text."""

    model = Text
    template_name = "word_analizer/text_detail.html"


class TextCreateView(CreateView):
    """Create View for raw text."""

    model = Text
    form_class = TextForm
    template_name = "word_analizer/text_create.html"

