from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question

from django.contrib import admin

from .models import Choice, Question

from django.contrib import admin

from .models import Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
inlines=[ChoiceInLine]
list_display=('question_text','pub_date','was_published_recently')
list_filter=['pub_date']
search_fields=['question_text']

admin.site.register(QuestionAdmin)

admin.site.register(Question, QuestionAdmin)


from django.contrib import admin

from .models import Choice, Question
# ...
admin.site.register(Choice)