from django.db import models

class PageVisit(models.Model):
    # Field to store the URL path as a string
    path = models.CharField(max_length=255, null=True, blank=True)  # URL path column
    
    # Field to store the timestamp of when the visit was created
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp when a visit is created
    
    def __str__(self):
        return f"Path: {self.path} | Timestamp: {self.timestamp}"

    class Meta:
        verbose_name = "Page Visit"
        verbose_name_plural = "Page Visits"
        ordering = ['-timestamp']  # Orders by latest visit first
