from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=255, default="",unique=True)
    
    def __str__(self):
        return self.name
    
class Intent(models.Model):
    name = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.name

class Category(models.Model):
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    intent = models.ForeignKey(Intent,default="",on_delete=models.CASCADE)
    category = models.CharField(max_length = 255, blank=True, unique = True)
    
    def __str__(self):
        return self.category
    
class Question(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    intent = models.ForeignKey(Intent,default="",on_delete=models.CASCADE)
    question = models.CharField(max_length = 255, default="",blank=True)
    
    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    intent = models.ForeignKey(Intent,default = "",on_delete=models.CASCADE)
    answer = models.CharField(max_length = 1024, blank=True)
    
    def __str__(self):
        return self.answer
    
class ChatTracker(models.Model):
    chatid = models.CharField(max_length = 255, default="")
    language = models.ForeignKey(Language,default=1,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,default="service")
    
    def __str__(self):
        return self.chatid