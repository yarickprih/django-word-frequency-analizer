from django.db import models
from django.urls import reverse_lazy

from word_analizer import services

# Create your models here.


class Text(models.Model):
    """Model definition for raw text and it's word frequncies."""

    text = models.TextField(
        verbose_name="Text",
        blank=False,
        null=False,
        default="",
        help_text="Enter text in English to let us analize it.",
    )

    most_frequent = models.JSONField(
        blank=True, null=True, verbose_name="Most Frequent Words"
    )

    average_frequency = models.JSONField(
        blank=True, null=True, verbose_name="Average Frequency Words"
    )

    least_frequent = models.JSONField(
        blank=True, null=True, verbose_name="Least Frequent Words"
    )

    class Meta:
        """Meta definition."""

        verbose_name = "Text"
        verbose_name_plural = "Texts"

    def __str__(self):
        return self.text[:15]

    def get_absolute_url(self):
        return reverse_lazy("text_detail_view", args=[self.pk])

    def save(self, *args, **kwargs):
        self.most_frequent = services.calc_most_freq(self.text)
        self.average_frequency = services.avg_freq(self.text)
        self.least_frequent = services.calc_least_freq(self.text)
        super().save(*args, **kwargs)
