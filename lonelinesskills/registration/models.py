from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from datetime import datetime

class LonelyHumanProfile(models.Model):
    AGES = (
        ('under18', _("Under 18")),
        ('18to25', '18 - 25'),
        ('26to35', '26 - 35'),
        ('36to50', '36 - 50'),
        ('over50', _("Over 50"))
    )

    GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('S', _("I do not want to say"))
    )

    REQUIRED_GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('B', _("Doesn't matter"))
    )

    COMMUNICATION = (
        ('E', _("By E-Mail")),
        ('P', _("By Phone")),
        ('L', _("Live meet"))
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.CharField(_("age"), max_length = 7, choices = AGES)
    gender = models.CharField(_("gender"), max_length = 1, choices = GENDERS)
    description = models.TextField(_("description"), max_length = 1000)
    communication_style = models.CharField(_("communication style"), max_length=1, choices = COMMUNICATION)
    required_age_from = models.IntegerField(_("required age from"))
    required_age_to = models.IntegerField(_("required age to"))
    required_gender = models.CharField(_("required gender"), max_length=1, choices = REQUIRED_GENDERS)
    

    class Meta:
        verbose_name = _("lonelyhumanprofile")
        verbose_name_plural = _("lonelyhumanprofiles")
        ordering = ['id']

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("lonelyhumanprofile_detail", kwargs={"pk": self.pk})
    

class VolunteerProfile(models.Model):
    GENDER_FOR_VOLUNTEER = (
        ('M', _("Male")),
        ('F', _("Female")),
    )

    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)
    age = models.IntegerField(_("age"))
    gender = models.CharField(_("gender"), max_length = 1, choices = GENDER_FOR_VOLUNTEER)
    personal_no = models.CharField(_("personal_no"), max_length = 15)
    lonelyhuman = models.ForeignKey(
        LonelyHumanProfile,
        verbose_name=_("volunteer"),
        on_delete=models.CASCADE, 
        related_name='lonelyhuman',
        null=True  
    )

    
    class Meta:
        verbose_name = _("volunteerprofile")
        verbose_name_plural = _("volunteerprofiles")
        ordering = ['id']

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})    


#Sekmadienio antras variantas
# class UserProfile(AbstractUser):
#     phone = models.CharField(_("phone"), max_length=50, null=True, blank=True, unique=True)
#     is_volunteer = models.BooleanField(default=False)  
#     is_lonely_human = models.BooleanField(default=False)
#     class Meta:
#         verbose_name = _("userprofile")
#         verbose_name_plural = _("userprofiles")
#         ordering = ['username']

#     def __str__(self):
#         return self.username

#     def get_absolute_url(self):
#         return reverse("userprofile_detail", kwargs={"pk": self.pk})


# class LonelyHumanProfile(models.Model):
#     age = (
#         ('under18', _("Under 18")),
#         ('18to25', '18 - 25'),
#         ('26to35', '26 - 35'),
#         ('36to50', '36 - 50'),
#         ('over50', _("Over 50"))
#     )

#     gender = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('secret', _("I do not want to say"))
#     )

#     required_genders = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('both', _("Not important"))
#     )

#     communication = (
#         ('email', _("By E-Mail")),
#         ('phone', _("By Phone")),
#         ('live', _("Live meet"))
#     )

#     age = models.CharField(_("age"), max_length = 10, choices=age)
#     gender = models.CharField(_("gender"),max_length = 10, choices = gender)
#     description = models.TextField(_("description"), max_length=2000)
#     communication_style = models.CharField(_("communication style"), max_length=10, choices=communication)
#     required_age_from = models.IntegerField(_("required age from"))
#     required_age_to = models.IntegerField(_("required age to"))
#     required_gender = models.CharField(_("required gender"), max_length=10, choices=required_genders)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='lonely_human_profile')


#     class Meta:
#         verbose_name = _("lonelyhumanprofile")
#         verbose_name_plural = _("lonelyhumanprofiles")
#         ordering = ['user_profile__username']

#     def __str__(self):
#         return self.user_profile.username

#     def get_absolute_url(self):
#         return reverse("lonelyhumanprofile_detail", kwargs={"pk": self.pk})


# class VolunteerProfile(models.Model):

#     gender_for_volunteer = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#     )

#     first_name = models.CharField(_("first name"), max_length=30)
#     last_name = models.CharField(_("last name"), max_length=30)
#     age = models.CharField(_("Age"), max_length = 10)
#     gender = models.CharField(_("gender"), max_length=10, choices=gender_for_volunteer)
#     identity_id = models.CharField(_("identity_id"), max_length=15)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='volunteer_profile')
#     lonelyhuman = models.ForeignKey(
#         LonelyHumanProfile, 
#         verbose_name=_("lonely human"),
#         on_delete=models.CASCADE, 
#         related_name='volunteers', 
#         null=True)

#     class Meta:

#         verbose_name = _("volunteerprofile")
#         verbose_name_plural = _("volunteerprofiles")
#         ordering = ['user_profile__username']

#     def __str__(self):

#         return self.user_profile.username

#     def get_absolute_url(self):
#         return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})



#Sekmadienio pirmas variantas
    
# class UserAccountManager(BaseUserManager): 
# 	def create_user(self, email, password = None): 
# 		if not email or len(email) <= 0 : 
# 			raise ValueError("Email field is required !") 
# 		if not password : 
# 			raise ValueError("Password is must !") 
		
# 		user = self.model( 
# 			email = self.normalize_email(email) , 
# 		) 
# 		user.set_password(password) 
# 		user.save(using = self._db) 
# 		return user 
	
# 	def create_superuser(self , email , password): 
# 		user = self.create_user( 
# 			email = self.normalize_email(email) , 
# 			password = password 
# 		) 
# 		user.is_admin = True
# 		user.is_staff = True
# 		user.is_superuser = True
# 		user.save(using = self._db) 
# 		return user 
	

# class UserAccount(AbstractBaseUser): 
# 	class Types(models.TextChoices): 
# 		lonely_human = 'LONELY_HUMAN' , _("lonely human")
# 		volunteer = "Volunteer" , _("Volunteer")
		
# 	type = models.CharField(max_length = 20 , choices = Types.choices , 
# 							default = Types.lonely_human) 
# 	email = models.EmailField(max_length = 50, unique = True) 
# 	is_active = models.BooleanField(default = True) 
# 	is_admin = models.BooleanField(default = False) 
# 	is_staff = models.BooleanField(default = False) 
# 	is_superuser = models.BooleanField(default = False) 
# 	is_lonely_human = models.BooleanField(default = False) 
# 	is_volunteer = models.BooleanField(default = False) 
	
# 	USERNAME_FIELD = "email"
	
# 	objects = UserAccountManager() 
	
# 	def __str__(self): 
# 		return str(self.email) 
	
# 	def has_perm(self , perm, obj = None): 
# 		return self.is_admin 
	
# 	def has_module_perms(self , app_label): 
# 		return True
	
# 	def save(self , *args , **kwargs): 
# 		if not self.type or self.type == None : 
# 			self.type = UserAccount.Types.lonely_human 
# 		return super().save(*args , **kwargs)


# class LonelyHumanManager(models.Manager): 
# 	def create_user(self , email , password = None): 
# 		if not email or len(email) <= 0 : 
# 			raise ValueError("Email field is required !") 
# 		if not password : 
# 			raise ValueError("Password is must !") 
# 		email = email.lower() 
# 		user = self.model( 
# 			email = email 
# 		) 
# 		user.set_password(password) 
# 		user.save(using = self._db) 
# 		return user 
	
# 	def get_queryset(self , *args, **kwargs): 
# 		queryset = super().get_queryset(*args , **kwargs) 
# 		queryset = queryset.filter(type = UserAccount.Types.lonely_human) 
# 		return queryset	 

# class LonelyHuman(UserAccount):
#     ages = (
#         ('under18', _("Under 18")),
#         ('18to25', '18 - 25'),
#         ('26to35', '26 - 35'),
#         ('36to50', '36 - 50'),
#         ('over50', _("Over 50"))
#     )

#     gender = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('secret', _("I do not want to say"))
#     )

#     required_genders = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('both', _("Not important"))
#     )

#     communication = (
#         ('email', _("By E-Mail")),
#         ('phone', _("By Phone")),
#         ('live', _("Live meet"))
#     )

#     age = models.CharField(_("age"), max_length=10, choices=ages)
#     gender = models.CharField(_("gender"), max_length=10, choices=gender)
#     description = models.TextField(_("description"), max_length=2000)
#     communication_style = models.CharField(_("communication style"), max_length=10, choices=communication)
#     required_age_from = models.IntegerField(_("required age from"))
#     required_age_to = models.IntegerField(_("required age to"))
#     required_gender = models.CharField(_("required gender"), max_length=10, choices=required_genders)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='lonely_human_profile')

#     class Meta:
#         proxy = True

#     objects = LonelyHumanManager()

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = UserAccount.Types.lonely_human
#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return f"LonelyHuman - {self.email}"

#     def get_absolute_url(self):
#         return reverse("lonelyhuman_detail", kwargs={"pk": self.pk})

	
# class VolunteerManager(models.Manager): 
# 	def create_user(self , email , password = None): 
# 		if not email or len(email) <= 0 : 
# 			raise ValueError("Email field is required !") 
# 		if not password : 
# 			raise ValueError("Password is must !") 
# 		email = email.lower() 
# 		user = self.model( 
# 			email = email 
# 		) 
# 		user.set_password(password) 
# 		user.save(using = self._db) 
# 		return user 
		
# 	def get_queryset(self , *args , **kwargs): 
# 		queryset = super().get_queryset(*args , **kwargs) 
# 		queryset = queryset.filter(type = UserAccount.Types.volunteer) 
# 		return queryset 
	
	
# class Volunteer(UserAccount):
#     gender_for_volunteer = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#     )

#     first_name = models.CharField(_("first name"), max_length=30)
#     last_name = models.CharField(_("last name"), max_length=30)
#     age = models.CharField(_("Age"), max_length=10)
#     gender = models.CharField(_("gender"), max_length=10, choices=gender_for_volunteer)
#     identity_id = models.CharField(_("identity_id"), max_length=15)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='volunteer_profile')
#     lonelyhuman = models.ForeignKey(
#         LonelyHuman, 
#         verbose_name=_("lonely human"),
#         on_delete=models.CASCADE, 
#         related_name='volunteers', 
#         null=True)

#     class Meta:
#         proxy = True
#         verbose_name = _("volunteerprofile")
#         verbose_name_plural = _("volunteerprofiles")
#         ordering = ['user_profile__username']

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = UserAccount.Types.volunteer
#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return self.user_profile.username

#     def get_absolute_url(self):
#         return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})


#Šeštadienio bandymas

# class UserProfile(models.Model):
#     user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
#     username = models.CharField(_("username"), max_length=20, db_index=True, unique=True)
#     email = models.EmailField(_("email"), max_length=50, null=True, blank=True)
#     phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)

#     class Meta:
#         verbose_name = _("userprofile")
#         verbose_name_plural = _("userprofiles")
#         ordering = ['username']

#     def __str__(self):
#         return self.username

#     def get_absolute_url(self):
#         return reverse("userprofile_detail", kwargs={"pk": self.pk})



# class LonelyHumanProfile(models.Model):
#     age = (
#         ('under18', _("Under 18")),
#         ('18to25', '18 - 25'),
#         ('26to35', '26 - 35'),
#         ('36to50', '36 - 50'),
#         ('over50', _("Over 50"))
#     )

#     gender = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('secret', _("I do not want to say"))
#     )

#     required_genders = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#         ('both', _("Not important"))
#     )

#     communication = (
#         ('email', _("By E-Mail")),
#         ('phone', _("By Phone")),
#         ('live', _("Live meet"))
#     )

#     age = models.CharField(_("Age"), max_length = 10, choices=age)
#     gender = models.CharField(_("gender"),max_length = 10, choices = gender)
#     description = models.TextField(_("description"), max_length=2000)
#     communication_style = models.CharField(_("communication Style"), max_length=10, choices=communication)
#     required_age_from = models.IntegerField(_("required Age From"))
#     required_age_to = models.IntegerField(_("required Age To"))
#     required_gender = models.CharField(_("required Gender"), max_length=10, choices=required_genders)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='lonely_human_profile')

#     class Meta:
#         verbose_name = _("lonelyhumanprofile")
#         verbose_name_plural = _("lonelyhumanprofiles")
#         ordering = ['user_profile__username']

#     def __str__(self):
#         return self.user_profile.username

#     def get_absolute_url(self):
#         return reverse("lonelyhumanprofile_detail", kwargs={"pk": self.pk})


# class VolunteerProfile(models.Model):
#     gender_for_volunteer = (
#         ('male', _("Male")),
#         ('female', _("Female")),
#     )

#     first_name = models.CharField(_("first name"), max_length=30)
#     last_name = models.CharField(_("last name"), max_length=30)
#     age = models.CharField(_("Age"), max_length = 10)
#     gender = models.CharField(_("gender"), max_length=10, choices=gender_for_volunteer)
#     identity_id = models.CharField(_("identity_id"), max_length=15)
#     user_profile = models.OneToOneField('UserProfile', verbose_name=_("user profile"), on_delete=models.CASCADE, related_name='volunteer_profile')
#     lonelyhuman = models.ForeignKey(
#         LonelyHumanProfile, 
#         verbose_name=_("lonely human"),
#         on_delete=models.CASCADE, 
#         related_name='volunteers', 
#         null=True)

#     class Meta:
#         verbose_name = _("volunteerprofile")
#         verbose_name_plural = _("volunteerprofiles")
#         ordering = ['user_profile__username']

#     def __str__(self):
#         return self.user_profile.username

#     def get_absolute_url(self):
#         return reverse("volunteerprofile_detail", kwargs={"pk": self.pk})




#Asmens kodo tikrinimas

# def save(self, *args, **kwargs):
#         if not self.validate_personal_no():
#             raise ValidationError('You are not real person!')
#         if self.age != self.calculate_age_from_personal_no():
#             raise ValidationError('You are not real person!') 
#         super().save(*args, **kwargs)

#     def validate_personal_no(self):
#         personal_no = self.personal_no
#         if len(personal_no) != 11:
#             return False
#         if not personal_no.isdigit():
#             return False
#         if (self.personal_no[0] == '3' or self.personal_no[0] == '5') and self.gender != 'M':
#             return False
#         if (self.personal_no[0] == '4' or self.personal_no[0] == '6') and self.gender != 'F':
#             return False
#         multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
#         checksum = sum(int(personal_no[i]) * multipliers[i] for i in range(10))

#         remainder = checksum % 11

#         if remainder == 10:
#             multipliers = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#             checksum = sum(int(personal_no[i]) * multipliers[i] for i in range(10))
#             remainder = checksum % 11

#         if remainder == int(personal_no[10]):
#             return True
#         else:
#             return False

#     def calculate_age_from_personal_no(self):
#         personal_no = self.personal_no
#         birth_year = int(personal_no[1:3])
#         today = datetime.now()
#         return today.year - birth_year - ((today.month, today.day) < (int(personal_no[3:5]), int(personal_no[5:7])))
