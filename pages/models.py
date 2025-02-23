from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class File(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name if self.file else "No File"

class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

# # Move AboutUs class outside ContactInfo
# class AboutUs(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     logo = models.ImageField(upload_to='uploads/')
#     image = models.ImageField(upload_to="about_images/", null=True, blank=True)

#     def __str__(self):
#         return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="logos/", default="logos/default_logo.png")  # Set default logo
    image = models.ImageField(upload_to="about_images/", null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255, default="Terms & Conditions")
    content = models.TextField()
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)  # Optional logo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255, default="Privacy Policy")
    content = models.TextField()
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)  # Optional logo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title