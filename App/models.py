from django.db import models

# Create your models here.
class Question(models.Model):
    Question_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.Question_text

class Choice(models.Model):
    Choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    Question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return self.Choice_text
