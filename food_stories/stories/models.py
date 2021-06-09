from django.db import models


class Category(models.Model):
    """
    this model saves story categories
    example: dessert, drinks, salad
    """
    title = models.CharField('Basliq', max_length=40)
    image = models.ImageField(upload_to='media/category_images/')

    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    comment
    """
    # information's
    title = models.CharField('Basliq', max_length=40)

    # moderation's
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Story(models.Model):
    """
    this model for save all stories example: Tasty & Delicious Foods,
    """
    CATEGORY_CHOICES = (
        (1, 'Dessert'),
        (2, 'Drink'),
        (3, 'Salad'),
    )
    # information's
    title = models.CharField(verbose_name='Basliq', max_length=120)
    category = models.IntegerField('Kateqoriya', choices=CATEGORY_CHOICES)
    description = models.TextField('Mezmun', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='media/story_images/')

    # moderation's
    is_published = models.BooleanField('Ders olunsun?', default=False)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ('category', )

    def __str__(self):
        return self.title
