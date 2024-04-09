# from django.views.decorators.cache import cache_page
# from .models import Category


# def get_function_context(self, request, slug):
#     page_objects = self.get_db_page(slug)
#     paginator = Paginator(self.get_db_content().all().select_related('category'), 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'title': page_objects.title,
#         'page_header': page_objects.page_header,
#         'page_post': page_objects.page_post,
#         'post': page_obj,
#         'page_obj': page_obj
#     }
#     return context


# @cache_page(60 * 15)
# def index(request):
#     return render(request, 'base/index.html', context=mixin.get_function_context(request, 'index'))


# @cache_page(60 * 15)
# def category(request, cat_slug):
#     category_objects = get_object_or_404(Category.objects.all(), cat_slug=cat_slug)
#     content_objects = mixin.get_db_content().filter(category_id=category_objects.pk).select_related('category')
#     extra_context = {
#         'title': category_objects.cat_name,
#         'page_header': category_objects.cat_name,
#         'post': content_objects
#     }
#     return render(request, 'base/index.html', context=extra_context)


# @cache_page(60 * 15)
# def content(request, slug):
#     content_objects = get_object_or_404(mixin.get_db_content().all(), slug=slug)
#     context = {
#         'title': content_objects.header,
#         'page_header': content_objects.header,
#         'post': content_objects.post,
#         'photo': content_objects.photo
#     }
#     return render(request, 'base/content.html', context=context)


# @cache_page(60 * 15)
# def about(request):
#     return render(request, 'base/about.html', context=mixin.get_function_context(request, 'about'))


# @cache_page(60 * 15)
# def contact(request):
#     page_objects = mixin.get_function_context(request, 'contact')
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             data = f"От: {email}\n{message}"
#             send_mail(name, data, '', [''])
#             return redirect('email_was_sent')
#     else:
#         form = ContactForm()
#     return render(request, "base/contact.html", context={**page_objects, **{'form': form}})


# @cache_page(60 * 15)
# def terms(request):
#     return render(request, 'base/terms_and_privacy.html', context=mixin.get_function_context(request, 'terms'))


# @cache_page(60 * 15)
# def privacy(request):
#     return render(request, 'base/terms_and_privacy.html', context=mixin.get_function_context(request, 'privacy'))


# def email_was_sent(request):
#     return render(request, 'base/email_was_sent.html')


# urlpatterns = [
#     path('', views.index, name="home"),
#     path('category/<slug:cat_slug>/', views.category, name='category'),
#     path('content/<slug:slug>/', views.content, name='content'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('terms/', views.terms, name='terms'),
#     path('privacy/', views.privacy, name='privacy'),
#     path('email_was_sent/', views.email_was_sent, name='email_was_sent'),
# ]
