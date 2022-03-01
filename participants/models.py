from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

Year=[
    ('1','First'),
    ('2','Second'),
    ('3','Third'),
    ('4','Forth')
]

class PreEvent(models.Model):
    Team_name = models.CharField(max_length=100)
    Member1_name = models.CharField(max_length=50)
    Member1_email = models.EmailField(
        verbose_name='Email Address', unique=True)
    Member1_contact_no = PhoneNumberField(
        blank=False, null=False, help_text='Add country code before the contact no.')
    Member1_roll_no = models.CharField(max_length=100, verbose_name="Roll no/ College Name", null=False, blank=False,
                                       default="", help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name')
    Member1_are_you_a_thapar_student = models.BooleanField(
        default=True, verbose_name="Are you a thapar student?")
    Member1_year_of_study = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Member1_discordid=models.CharField(max_length=100,null=True,blank=True)    
    Member2_name = models.CharField(max_length=50, blank=True)
    Member2_email = models.EmailField(
        verbose_name='Email Address', blank=True)
    Member2_contact_no = PhoneNumberField(
        blank=True, help_text='Add country code before the contact no.')
    Member2_roll_no = models.CharField(max_length=100, verbose_name="Roll no/ College Name", blank=True,
                                       default=" ", help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name')
    Member2_are_you_a_thapar_student = models.BooleanField(
         verbose_name="Are you a thapar student?",blank=True)
    Member2_year_of_study = models.IntegerField(
         validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True,null=True)
    Member2_discordid=models.CharField(max_length=100,blank=True)  


    def __str__(self):
        return self.Team_name
 