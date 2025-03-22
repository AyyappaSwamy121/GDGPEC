from django.contrib import admin
from .models import *

class Registration_adding(admin.ModelAdmin):
    list_display=["name","contact","email","password","kaggle_result","flutter_result","kotlin_result","android_development_result","firebase_result","gemini_result"]
admin.site.register(Registration,Registration_adding)


class kaggle(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(kaggle_questions, kaggle,)

class flutter(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(flutter_questions, flutter,)

class flutter(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(firebase_questions, flutter,)

class gemini(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(gemini_questions, gemini,)

class android_development(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(android_development_questions, android_development,)

class kotlin(admin.ModelAdmin):
    list_display = ("question", "option1","option2","option3","option4","answer",)
admin.site.register(kotlin_questions, kotlin,)