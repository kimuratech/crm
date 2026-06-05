from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='leads', null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Deal(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    stage = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    subject = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
