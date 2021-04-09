from django.db import models
from django.utils import timezone


class Person(models.Model):
    plannames = (
        ("1", "premium"),
        ("2", "gold"),
        ("3", "diamond")
    )

    # not null fields
    name = models.CharField(max_length=50)
    plan = models.CharField(max_length=50, choices=plannames, default="1")
    created = models.DateTimeField(auto_now_add=True)  # timestamp of creation
    signalString = models.CharField(max_length=50)
    # depending upton the plan time(10sec)
    status = models.BooleanField(default=True)
    count = models.IntegerField(default=0)  # no. of times api clicked

    manualbooleanfield = models.BooleanField(default=False)

    time_when_boolean_field_changes = models.DateTimeField(default=None, null=True)

    total_ratings = models.IntegerField(default=0)
    no_of_ratings = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    rating = models.IntegerField(default=0)





    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.original_name = self.name
        self.old_count = self.count
        self.old_total_ratings = self.total_ratings
        self.old_no_of__ratings = self.no_of_ratings

        self.old_manualbooleanfield = self.manualbooleanfield
        # self.old_average_ratings = self.total_ratings



    def save(self, *args, **kwargs):

        # no. of times api clicked
        self.count = self.old_count+1

        # calculate and update rating
        if self.rating:
            self.total_ratings = self.old_total_ratings + self.rating
            self.no_of_ratings = self.old_no_of__ratings + 1
            self.average_rating = self.total_ratings / self.no_of_ratings

        # set new time changes when boolean field changes
        if self.old_manualbooleanfield != self.manualbooleanfield:
            self.time_when_boolean_field_changes = timezone.now()


        # save the data
        super().save(*args, **kwargs)



    def __str__(self):
        return str(self.id) + " " + self.name 
