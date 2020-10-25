from datetime import date
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()

"""
Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).
Ресурс GENRES: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
Ресурс REVIEWS: отзывы на произведения. Отзыв привязан к определённому произведению.
Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
"""


class Categories(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=100, blank=False)
    year = models.PositiveIntegerField(
        default=date.today().year,
        validators=[MaxValueValidator(date.today().year)]
    )
    description = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True,
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    #genre = models.ManyToManyField(Genres, related_name='genres', related_query_name='query_genres')
        #, default=None, blank=True)
 #       Genres,
 #       related_name='genres',
 #       blank=True,
  #  )
    genre = models.ManyToManyField(Genres) #, verbose_name='genre',blank=True)
    #genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, related_name="genre", blank=True, null=True)
#    )

    #category = models.ManyToManyField(Categories)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name='titles', blank=True, null=True,)
 #   )

    def __str__(self):
        return self.name

  #  def get_genres(self):
  #      return "\n".join([i.name for i in self.genre.all()])
    
 #   def get_category(self):
  #      pass
 #       return "\n".join([i.name for i in self.category.all()])

class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name="review"
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review"
    )
    pub_date = models.DateTimeField("review date", auto_now_add=True)
    score = models.IntegerField(null=True, blank=True,
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ['author', 'title']
        ordering = ['-pub_date']


class Comments(models.Model):
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE,
                                related_name='comments', blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField("comment date", auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
