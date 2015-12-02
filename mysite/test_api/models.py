from django.db import models

# Create your models hqreq
class AipuAccount(models.Model):
    aipu_id = models.CharField(max_length = 6)
    password = models.CharField(max_length = 6)
    wallet_user = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.aipu_id
