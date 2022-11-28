from django.contrib import admin
from .models import TbCssrespondents, TbQuestions, TbCmuoffices, TbCmuofficials, TbCoverage, \
    TbCssrespondentsDetails, TbEmployees


class CustomerFeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('responddate',)


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('datecreated',)


admin.site.register(TbCssrespondents, CustomerFeedbackAdmin)
admin.site.register(TbQuestions, QuestionAdmin)
admin.site.register(TbCmuoffices)
admin.site.register(TbCmuofficials)
admin.site.register(TbCoverage)
admin.site.register(TbCssrespondentsDetails)
admin.site.register(TbEmployees)
