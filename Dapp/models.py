from django.db import models

# Create your models here.


class Contract(models.Model):
    name = models.CharField(max_length=50, editable=False)
    abi = models.TextField(null=True, editable=False)
    bytecode = models.TextField(null=True, editable=False)
    address = models.TextField(null=True, editable=False)
    contract = models.TextField(null=True)

    def __str__(self):
        return self.name
