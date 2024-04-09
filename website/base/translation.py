from modeltranslation.translator import register, TranslationOptions
from .models import Content, Category


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ('header', 'post',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('cat_name',)
