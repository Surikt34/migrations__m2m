from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = sum(1 for form in self.forms if form.cleaned_data.get('is_main'))

        if main_tag_count == 0:
            raise ValidationError('Укажите основной раздел.')
        elif main_tag_count > 1:
            raise ValidationError('Основным может быть только один раздел.')

        return super().clean()

class RelationshipInlineFormset(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInlineFormset]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass