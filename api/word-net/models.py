from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from django.utils.text import slugify


class WordNet(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    short_description = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    hypernyms = models.ManyToManyField('self', related_name='word_hypernymns', null=True, blank=True)
    hyponyms = models.ManyToManyField('self', related_name='word_hyponyms', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(WordNet, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
