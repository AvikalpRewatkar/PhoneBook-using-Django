from django.db import models

# Create your models here.
class createcontact(models.Model):
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nickName = models.CharField(max_length=100)
    phoneno = models.CharField(max_length = 11)
    workno = models.CharField(max_length = 11)
    email = models.EmailField(max_length=100)
    birthday = models.CharField(max_length=100)
    anniversary = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=4)
    hstreet = models.CharField(max_length=100)
    hcity = models.CharField(max_length=100)
    hstate = models.CharField(max_length=100)
    hcountry = models.CharField(max_length=100)
    hpostcode = models.CharField(max_length=100)
    wstreet = models.CharField(max_length=100)
    wcity = models.CharField(max_length=100)
    wstate = models.CharField(max_length=100)
    wcountry = models.CharField(max_length=100)
    wpostcode = models.CharField(max_length=100)

    # name = str(firstName) + str(middleName) + str(lastName)

    def __str__(self):
        self.name = str(self.firstName) + " " +  str(self.middleName) + " " + str(self.lastName)
        return self.name
    