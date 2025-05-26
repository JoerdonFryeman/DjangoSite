from .models import Content
from base.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, FormView, DetailView


class HomePage(ListView):
    template_name = 'base/index.html'
    context_object_name = 'post'
    paginate_by = 4
    extra_context = {'title': _('Space'), 'page_header': _('Space')}

    def get_queryset(self):
        return Content.published.all().select_related('category')


class CategoryPage(ListView):
    template_name = 'base/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['post'][0].category
        context['title'] = cat.cat_name
        context['page_header'] = cat.cat_name
        context['selected'] = cat.pk
        return context

    def get_queryset(self):
        return Content.published.filter(category__cat_slug=self.kwargs['cat_slug']).select_related('category')


class ContentPage(DetailView):
    template_name = 'base/content.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['content'].header
        context['page_header'] = context['content'].header
        context['photo'] = context['content'].photo
        context['post'] = context['content'].post
        context['author'] = context['content'].author
        context['time_update'] = context['content'].time_update
        context['slug'] = context['content'].slug
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Content.published, slug=self.kwargs[self.slug_url_kwarg])


class AboutPage(TemplateView):
    template_name = 'base/about.html'
    extra_context = {
        'title': _('About'),
        'page_header': _('Site information'),
        'page_post': _('Website source code')
    }


class ContactPage(FormView):
    form_class = ContactForm
    template_name = 'base/contact.html'
    extra_context = {
        'title': _('Contact'),
        'page_header': _('Contact us'),
        'page_post': _('Support with Bitcoin: bc1qewfgtrrg2gqgtvzl5d2pr9pte685pp5n3g6scy')
    }

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        data = f"От: {email}\n{message}"
        send_mail(name, data, '', [''])
        return redirect('email_was_sent')


class TermsPage(TemplateView):
    template_name = 'base/terms.html'
    extra_context = {
        'title': _('Terms'),
        'page_header': _('Terms of Use'),
        'page_post': _('Your Terms of Use')
    }


class PrivacyPage(TemplateView):
    template_name = 'base/privacy.html'
    extra_context = {
        'title': _('Privacy'),
        'page_header': _('Privacy & Security'),
        'page_post': _('Your privacy policy')
    }


class EmailWasSent(TemplateView):
    template_name = 'base/email_was_sent.html'
    extra_context = {
        'title': _('Successfully sent!'),
        'page_header': _('Successfully sent!'),
        'page_post': _('Your message has been successfully sent!')
    }


def page_not_found(request, exception):
    return HttpResponseNotFound(render(request, 'base/error_404.html'))
