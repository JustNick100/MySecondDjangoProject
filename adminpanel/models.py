from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.


class UserProfile(models.Model): 

    full_name = models.CharField(max_length=255)

    email = models.EmailField(max_length=254)

    password=models.CharField(max_length=255)

    level = models.CharField(max_length=20)

    def __str__(self):

    	return self.user.username



class Agent(models.Model):

	full_name = models.CharField(max_length=255)

	email = models.EmailField()

	user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)



class Service(models.Model):

	title = models.CharField(max_length=255)

	description = models.TextField(blank=True)

	procedure = models.TextField(blank=True)

	def __str__(self):

		return self.title



class Service_faq(models.Model):

	question = models.TextField(blank=True)

	answer = models.TextField(blank=True)

	service = models.ForeignKey(Service,on_delete=models.CASCADE)

	def __str__(self):

		return self.question



class Service_faq_docs(models.Model):

	title = models.CharField(max_length=100)

	doc_type = models.CharField(max_length=50)

	path = models.TextField(blank=True)

	faq = models.ForeignKey(Service_faq, on_delete=models.CASCADE)

	def __str__(self):

		return self.title



class Service_faq_link(models.Model):

	target_type = models.CharField(max_length=50)

	target_id = models.IntegerField()

	faq_id = models.ForeignKey(Service_faq,on_delete=models.CASCADE)



class Transcript(models.Model):

	datetime = models.DateTimeField()

	client_id = models.IntegerField()

	agent_id = models.IntegerField()



class Transcript_message(models.Model):

	datetime = models.DateTimeField()

	content = models.TextField(blank=True)

	sender_id = models.IntegerField()
	
	sender_type = models.CharField(max_length=10)

	transcript = models.ForeignKey(Transcript,on_delete = models.CASCADE)

	def __str__(self):

		return self.content



class Category(models.Model):

	title = models.CharField(max_length=200)

	description = models.TextField(blank=True)

	master = models.IntegerField()#replace this into Foreignkey with master model

	service = models.ForeignKey(Service, on_delete=models.CASCADE)




class Categories_suggestion(models.Model):

	target_type = models.CharField(max_length=100)

	target_id = models.IntegerField()

	category = models.ForeignKey(Category, on_delete=models.CASCADE)




class Language(models.Model):

	name = models.CharField(max_length=100)

	direction = models.CharField(max_length=5)

	def __str__(self):

		return self.name



class Client(models.Model):

	full_name = models.CharField(max_length=100)

	email = models.EmailField()

	phone = PhoneField(blank=True)

	language = models.ForeignKey(Language, on_delete=models.CASCADE)



class Language_translations(models.Model):

	target = models.IntegerField()

	target_type = models.CharField(max_length=50)

	content = models.TextField()

	language = models.ForeignKey(Language, on_delete=models.CASCADE)







