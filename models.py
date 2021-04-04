from django.db import models

# Create your models here.

class VideoModel(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to="videos", null=True, verbose_name="")

    # class Meta:
    #     verbose_name = 'videofile'
    #     verbose_name_plural = 'videos'

    def __str__(self):
        return self.name
