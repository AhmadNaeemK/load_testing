from django.db import models

# Create your models here.


class Organization(models.Model):
    title = models.CharField(max_length=20)
    ceo_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phn = models.CharField(max_length=15)


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    organization = models.ForeignKey(to='Organization', on_delete=models.CASCADE)
    salary = models.IntegerField(default=1000)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    title = models.CharField(max_length=20)
    organization = models.ForeignKey(to='Organization',
                                     related_name='project_organization',
                                     on_delete=models.CASCADE)
    manager = models.ForeignKey(to='Employee',
                                related_name='manager',
                                on_delete=models.CASCADE)
    employees = models.ManyToManyField(to='Employee',
                                       related_name='project_employee_set'
                                       )
    budget = models.IntegerField(default=0)
