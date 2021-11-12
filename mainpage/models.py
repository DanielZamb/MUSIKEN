from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    user_name = models.CharField(max_length=150)
    artist = models.BooleanField()
    biography = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Publication(models.Model):
    publication_id = models.BigIntegerField(primary_key=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="publications")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Review(models.Model):
    review_id = models.BigIntegerField(primary_key=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="reviews")
    publications = models.ManyToManyField(Publication,
                                          related_name="reviews")
    opinion = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "review-" + str(self.review_id)


class Rating(models.Model):
    rating_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=150,
                            blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name="own_ratings")
    users = models.ManyToManyField(User,
                                   related_name="ratings_used")
    review = models.ForeignKey(Review,
                               on_delete=models.DO_NOTHING,
                               related_name="ratings")

    def __str__(self):
        return self.name


class Content(models.Model):
    content_id = models.BigIntegerField(primary_key=True)
    publication = models.OneToOneField(Publication,
                                       on_delete=models.CASCADE,
                                       related_name="content")
    content_text = models.TextField()
    links = models.URLField(max_length=200)

    def __str__(self):
        return "cont-" + self.publication.name


class ContentImage(models.Model):
    image_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50,
                            blank=True)
    image = models.ImageField()
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE,
                                related_name="images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProfileImage(models.Model):
    image_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50,
                            blank=True)
    image = models.ImageField()
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile_image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TextMeasure(models.Model):
    text_id = models.BigIntegerField(primary_key=True)
    rating = models.OneToOneField(Rating,
                                  on_delete=models.CASCADE,
                                  related_name="text_measure")
    good_text = models.TextField()
    neutral_text = models.TextField()
    bad_text = models.TextField()

    def __str__(self):
        return "text-" + str(self.text_id)


class ScaleMeasure(models.Model):
    scale_id = models.BigIntegerField(primary_key=True)
    rating = models.OneToOneField(Rating,
                                  on_delete=models.CASCADE,
                                  related_name="scale_measure")
    lower_bound = models.FloatField()
    upper_bound = models.FloatField()
    unit = models.FloatField()

    def __str__(self):
        return "scale-" + str(self.scale_id)


class PercentageMeasure(models.Model):
    percentage_id = models.BigIntegerField(primary_key=True)
    rating = models.OneToOneField(Rating,
                                  on_delete=models.CASCADE,
                                  related_name="percentage_measure")
    upper_bound = models.FloatField()
    unit = models.FloatField()

    def __str__(self):
        return "percentage-" + str(self.percentage_id)


class Test(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    text = models.FloatField()

    def __str__(self):
        return self.first_name

# Create your models here.
