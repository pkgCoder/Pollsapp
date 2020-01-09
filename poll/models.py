from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default = timezone.now)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    question  = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.choice_text
