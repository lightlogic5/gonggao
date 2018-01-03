from django.db import models

# Create your models here.
# 共创建了3个模型，分别是项目名、标签名、文章
class project(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

class tags(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

class articale(models.Model):
    name = models.CharField(max_length=255)
    a_project = models.ForeignKey(project)
    a_tag = models.ManyToManyField(tags, null=True, blank=True, verbose_name="选择文章标签")

    def __str__ (self):
        return self.name
    
