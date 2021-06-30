from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class Category(models.Model):
    """
    this model saves story categories
    example: dessert, drinks, salad
    """
    title = models.CharField('Basliq', max_length=40)
    image = models.ImageField(upload_to='category_images')

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
    # CATEGORY_CHOICES = (
    #     (1, 'Dessert'),
    #     (2, 'Drink'),
    #     (3, 'Salad'),
    # )
    # relation's
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 db_index=True, related_name='stories')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               db_index=True, related_name='stories')
    tags = models.ManyToManyField(Tag, related_name='stories', db_index=True)

    # information's
    title = models.CharField(verbose_name='Basliq', max_length=120)
    description = models.TextField('Mezmun', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='story_images')

    # moderation's
    is_published = models.BooleanField('Ders olunsun?', default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ('category',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('stories:story_detail', kwargs={
            'pk': self.pk
        })


class Recipe(models.Model):
    """
    this model for save all stories example: Tasty & Delicious Foods,
    """
    # CATEGORY_CHOICES = (
    #     (1, 'Dessert'),
    #     (2, 'Drink'),
    #     (3, 'Salad'),
    # )
    # relation's
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 db_index=True, related_name='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               db_index=True, related_name='recipes')
    tags = models.ManyToManyField(Tag, related_name='recipes', db_index=True)

    # information's
    title = models.CharField(verbose_name='Basliq', max_length=120)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun', )
    image = models.ImageField('Sekil', upload_to='story_images')

    # moderation's
    is_published = models.BooleanField('Ders olunsun?', default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ('title',)

    def __str__(self):
        return self.title


class RecipeComment(models.Model):
    # relation's
    user = models.ForeignKey(User, db_index=True,
                             related_name='recipe_comments', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, db_index=True,
                               related_name='recipe_comments', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', db_index=True, null=True, blank=True,
                                       related_name='replies', on_delete=models.CASCADE)

    # information's
    content = models.TextField()

    # moderation's
    is_published = models.BooleanField('Ders olunsun?', default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. user: {self.user.username}"


class Contact(models.Model):
    name = models.CharField('Name', max_length=40)
    email = models.EmailField(max_length=40,)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class StoryComment(models.Model):
    # relation's
    user = models.ForeignKey(User, db_index=True,
                             related_name='story_comments', on_delete=models.CASCADE)
    story = models.ForeignKey(Story, db_index=True,
                              related_name='story_comments', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', db_index=True, null=True, blank=True,
                                       related_name='replies', on_delete=models.CASCADE)

    # information's
    content = models.TextField()

    # moderation's
    is_published = models.BooleanField('Ders olunsun?', default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)


class BookCategory(models.Model):
    title = models.CharField(max_length=255)


class Author(models.Model):
    full_name = models.CharField('ad soyad', max_length=255)
    image = models.ImageField('foto', upload_to='authors')
    nationality = models.CharField('milliyet', max_length=255)
    info = models.TextField('Bio')


class Book(models.Model):
    title = models.CharField('Basliq', max_length=255)
    description = models.TextField('Haqqinda')
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    price = models.DecimalField('qiymet', max_digits=4, decimal_places=2)
    page_count = models.IntegerField('sehife sayi')
    cover_image = models.ImageField('uz qabigi', upload_to='book_covers')
    categories = models.ManyToManyField(BookCategory, blank=True, related_name='books')
