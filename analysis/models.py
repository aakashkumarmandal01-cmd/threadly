from django.db import models
class AdminAction(models.Model): user=models.ForeignKey('accounts.User',on_delete=models.SET_NULL,null=True); action=models.CharField(max_length=200); target=models.CharField(max_length=200,blank=True); metadata=models.JSONField(default=dict,blank=True); created_at=models.DateTimeField(auto_now_add=True)
