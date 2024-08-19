from django.db import models




class Advisor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.URLField(max_length=9000,null=True)
    contact_info = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['id']
        indexes=[
            models.Index(fields=['id']),
        ]



class StatusChoices(models.TextChoices):
    DRAFT = 'df','Draft'
    PUBLISH='pb','Publish'


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=10000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    reviews_count=models.PositiveIntegerField(default=0)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=StatusChoices.choices, default=StatusChoices.PUBLISH)
    slug = models.SlugField(null=True,blank=True)

    def df_to_pb(self):
        if self.status == "df":
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == "pb":
            self.status = 'df'
            self.save()

    def __str__(self):
        return self.name






    class Meta:
        ordering = ['reviews_count']
        indexes = [
            models.Index(fields=['reviews_count']),
        ]



class Review(models.Model):
    SERVICE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    service = models.ForeignKey(Service,  on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=SERVICE_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True,blank=True)


    class Meta:
        ordering = ['-rating']
        indexes = [
            models.Index(fields=['-rating']),
        ]





class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.URLField(max_length=3000, null=True)
    profile_views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.nickname



    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id']),
        ]

class StatusChoices(models.TextChoices):
    DRAFT = 'df','Draft'
    PUBLISH='pb','Publish'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.URLField(max_length=4000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=5, choices=StatusChoices.choices, default=StatusChoices.PUBLISH)
    slug = models.SlugField(null=True,blank=True)

    def df_to_pb(self):
        if self.status == "df":
            self.status = 'pb'
            self.save()

    def pb_to_df(self):
        if self.status == "pb":
            self.status = 'df'
            self.save()



    def __str__(self):
        return self.title




    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]






