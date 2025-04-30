from django.contrib import admin

# Register your models here.
from .models import Idea, Document, Content, Schedule

# Admin pour la classe Idea
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "urgent",
        "text",
        "audio_file",
        "created_at",
    )
    # Remplacer les champs vides qui n'est pas possible ManyToManyField
    empty_value_display = " "
    
    # Champs éditables
    list_display_links = ("title",)
    list_editable = ("urgent", "slug",)
    list_per_page = 10 # Permet de limiter le nombres d'articles par page permet de fluidifier l'administration

# Admin pour la classe Idea
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "uploaded_at",
        "summarized_text",
    )
    # Remplacer les champs vides qui n'est pas possible ManyToManyField
    empty_value_display = " "
    
    # Champs cliquables
    list_display_links = ("file",)
    list_per_page = 10 # Permet de limiter le nombres d'articles par page permet de fluidifier l'administration

# Admin pour la classe Idea
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        "idea",
        "content_type",
        "generated_text",
        "created_at",
        "is_published",
    )
    # Remplacer les champs vides qui n'est pas possible ManyToManyField
    empty_value_display = " "
    
    # Champs éditables
    list_display_links = ("idea", )
    list_editable = ("content_type", )
    list_per_page = 10 # Permet de limiter le nombres d'articles par page permet de fluidifier l'administration

# Admin pour la classe Idea
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "scheduled_time",
        "platform",
        "is_executed",
    )
    # Remplacer les champs vides qui n'est pas possible ManyToManyField
    empty_value_display = " "
    
    # Champs éditables
    list_display_links = ("content",)
    list_editable = ("platform",)
    list_per_page = 10 # Permet de limiter le nombres d'articles par page permet de fluidifier l'administration

