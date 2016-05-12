from django.db import models

# ********** Start Models **********

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="CompanyLogos/", default="CompanyLogos/none/default_logo.jpg" )

    @property
    def votes_objects(self):
        return Vote.objects.filter(company=self)

    @property
    def yes_objects(self):
        return self.votes_objects.filter(does_test=True)

    @property
    def no_objects(self):
        return self.votes_objects.filter(does_test=False)

    @property
    def num_votes(self):
        return self.votes_objects.count()

    @property
    def num_yes_votes(self):
        return self.yes_objects.count()

    @property
    def num_no_votes(self):
        return self.no_objects.count()

    @property
    def percent_yes(self):
        return format(self.num_yes_votes/self.num_votes * 100, '.2f')

    @property
    def percent_no(self):
        return format(self.num_no_votes/self.num_votes * 100, '.2f')

    def __str__(self):
        return self.name

class Vote(models.Model):
    does_test = models.BooleanField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=80)
    comment = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return '%s on %s' % (self.does_test, self.date)

class Suggestion(models.Model):
    logo = models.FileField()
    company_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)

# ********** End Models **********