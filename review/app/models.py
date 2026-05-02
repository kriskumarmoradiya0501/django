from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    release_date = models.DateField()

    duration = models.IntegerField()

    category = models.CharField(max_length=50)

    language = models.CharField(max_length=50)

    director_name = models.CharField(max_length=100)

    budget = models.BigIntegerField()

    imdb_rating = models.FloatField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    user_name = models.CharField(max_length=100)

    user_email = models.EmailField()

    rating = models.IntegerField()

    review_text = models.TextField()

    watched_on = models.DateField()

    recommend = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name