from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from users.context_processors import get_content_model
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserPasswordChangeForm, AddPostForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': _('Login'), 'page_header': _('Authorization')}


class UserRegistration(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    extra_context = {'title': _('Registration'), 'page_header': _('Registration')}
    success_url = reverse_lazy('users:login')


class UserProfile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': _('Profile'), 'page_header': _('User profile')}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:back_to_profile")
    template_name = "users/password_change_form.html"
    extra_context = {'title': _('Password change'), 'page_header': _('Password change')}


class UserPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'users/back_to_profile.html'
    extra_context = {'title': _('Password change'), 'page_header': _('Password change successfully done')}


class UserPasswordReset(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    extra_context = {'title': _('Password reset'), 'page_header': _('Password reset')}


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    extra_context = {'title': _('Password reset'), 'page_header': _('Password reset done')}


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy("users:password_reset_complete")
    extra_context = {'title': _('Password reset'), 'page_header': _('Password reset confirm')}


class UserPasswordResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    extra_context = {'title': _('Password reset'), 'page_header': _('Password reset complete')}


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'users/add_post.html'
    extra_context = {'title': _('Add an article'), 'page_header': _('Add an article')}


class UpdatePost(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = get_content_model()
    fields = ['header_ru', 'header_en', 'post_ru', 'post_en', 'category', 'author', 'photo', 'slug']
    template_name = 'users/add_post.html'
    permission_required = 'users.change_users'
    success_url = reverse_lazy('home')
    extra_context = {'title': _('Edit article'), 'page_header': _('Edit article')}


class DeletePost(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = get_content_model()
    template_name = 'users/delete.html'
    permission_required = 'users.delete_users'
    success_url = reverse_lazy('home')
    extra_context = {'title': _('Delete article'), 'page_header': _('Delete article')}
