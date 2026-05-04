from django.db import models

# Create your models here.
class currentBalance(models.Model):
    current_balance=models.FloatField(default=0)


class trackHistory(models.Model):
    current_balance=models.ForeignKey(currentBalance, on_delete=models.CASCADE)
    amount=models.FloatField(default=0)
    expense_type= models.CharField(choices=(
        ('CREDIT','CREDIT'),
        ('DEBIT','DEBIT')
    ))
    description= models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    