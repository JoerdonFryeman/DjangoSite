# from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth import get_user_model, authenticate, login, logout
# from django.views.decorators.cache import cache_page


# @cache_page(60 * 15)
# def user_login(request):
#     page_objects = mixin.get_function_extra_context('login')
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = UserLoginForm()
#     return render(request, 'users/login.html', context={**page_objects, **{'form': form}})


# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('home'))


# def user_registration(request):
#     form = UserRegisterForm(request.POST)
#     page_objects = mixin.get_function_extra_context('registration')
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             return render(request, 'users/login.html')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/registration.html', context={**page_objects, **{'form': form}})

# def add_post(request):
#     page_objects = mixin.get_context('add_post')
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 get_content_model().objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Error')
#     else:
#         form = AddPostForm()
#     return render(request, 'users/add_post.html', context={**page_objects, **{'form': form}})


# urlpatterns = [
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('registration/', views.user_registration, name='registration'),
#     path('add_post/', views.add_post, name='add_post'),
# ]


# class UserRegisterForm(UserCreationForm):
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password1'] != cd['password2']:
#             raise forms.ValidationError(_('The passwords don\'t match!'))
#         return cd['password1']
