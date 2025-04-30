from django.db import models

# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField() # Afficher le titre dans l'URL "x-x-x..."
    urgent = models.BooleanField()
    text = models.TextField(blank = True)
    audio_file = models.FileField(upload_to='ideas/audio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title or f"Idée #{self.id}"

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summarized_text = models.TextField(blank=True)

    def __str__(self):
        return self.file.name


class Content(models.Model):
    CONTENT_TYPES = [
        ('post', 'Post LinkedIn'),
        ('tweet', 'Tweet'),
        ('email', 'Email'),
        ('script', 'Script vidéo'),
    ]
    
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
            return f"{self.content_type.capitalize()} lié à {self.idea}"


class Schedule(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    platform = models.CharField(max_length=100)  # Ex : LinkedIn, Twitter
    is_executed = models.BooleanField(default=False)

    def __str__(self):
        return f"📅 {self.platform} @ {self.scheduled_time}"