from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    site_title = models.CharField(max_length=200, default="MarketPlace")
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to="photos/logos/", blank=True, null=True)
    favicon = models.ImageField(upload_to="photos/favicons/", blank=True, null=True)
    site_copy = models.CharField(max_length=200, default="Copyright") 

    def __str__(self):
        return "Site Setting"
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

class Banner(models.Model):
    site_setting = models.ForeignKey(SiteSetting, on_delete=models.CASCADE, related_name="banners")
    image = models.ImageField(upload_to="photos/banners/")
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Banner for {self.site_setting.site_title}"