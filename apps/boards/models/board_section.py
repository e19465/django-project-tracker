from django.db import models
from core.models import TimeStampedModel
from boards.models import Board


class BoardSection(TimeStampedModel):
    title = models.CharField(max_length=50)
    max_issues_limit = models.PositiveIntegerField(default=0)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="board_sections"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = "Board Section"
        verbose_name_plural = "Board Sections"

    def __str__(self):
        return f"Section {self.pk}: {self.title}"
