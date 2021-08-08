from django.contrib import admin

from . import models

# admin.site.register(models.Question)
# admin.site.register(models.Choice)

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Dashboard'
admin.site.index_title = 'Pollster Admin Dashboard'


class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {
        'fields': ['question_text']
    }), ('Date Information', {
        'fields': ['pub_date'],
        'classes': ['collapse']
    })]

    inlines = [ChoiceInline]


admin.site.register(models.Question, QuestionAdmin)
