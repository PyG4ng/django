from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                main_tag += 1

        if main_tag > 1:
            raise ValidationError('Может быть только один основной тег!')
        elif main_tag == 0:
            raise ValidationError('Должен быть хотя бы один основной тег!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


class ScopeTagInline(admin.TabularInline):
    model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at',]
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeTagInline,]
