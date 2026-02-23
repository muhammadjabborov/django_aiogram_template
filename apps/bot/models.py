from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from apps.common.models import BaseModel


# ------------------------
# User
# ------------------------

class User(BaseModel):
    full_name = models.CharField(_("full_name"), max_length=255, blank=True, null=True)
    phone_number = models.CharField(_("phone_number"), max_length=255, blank=True, null=True)
    username = models.CharField(_("username"), max_length=255, blank=True, null=True)
    telegram_id = models.BigIntegerField(_("telegram_id"), unique=True, db_index=True)
    is_premium = models.BooleanField(default=False)
    premium_end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.full_name or ''} ({self.username})"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


# ------------------------
# Book
# ------------------------

class Book(BaseModel):
    title = models.CharField(_("title"), max_length=255, blank=True, null=True)
    subtitle = models.CharField(_("subtitle"), max_length=255, blank=True, null=True)
    photo = models.ImageField(_("photo"), upload_to="books/", blank=True, null=True)

    def __str__(self):
        return self.title or "Book"

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


# ------------------------
# Chapter
# ------------------------

class Chapter(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(_("title"), max_length=255, blank=True, null=True)
    order = models.IntegerField(_("order"), default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - {self.title}"

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")
        ordering = ["order"]


# ------------------------
# Test (Question)
# ------------------------

class Test(BaseModel):
    class TestType(models.TextChoices):
        REGULAR_TEST = "regular_test", "Regular Test"
        BOOLEAN_TEST = "boolean_test", "True / False"

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="tests")
    question = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)
    type = models.CharField(
        max_length=20,
        choices=TestType.choices,
        default=TestType.REGULAR_TEST
    )

    def __str__(self):
        return f"Q: {self.question[:50]}"

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
        ordering = ["order"]


# ------------------------
# Answer (Choices)
# ------------------------

class Answer(BaseModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="answers")
    text = HTMLField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text[:40]}"

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")


# ------------------------
# User Test Session
# ------------------------

class UserTest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tests")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.chapter.title} ({self.score})"

    class Meta:
        verbose_name = _("User Test")
        verbose_name_plural = _("User Tests")


# ------------------------
# User Answer (Selected Option)
# ------------------------

class UserAnswer(BaseModel):
    user_test = models.ForeignKey(UserTest, on_delete=models.CASCADE, related_name="answers")
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_test.user} - {self.test.id}"

    class Meta:
        unique_together = ("user_test", "test")
        verbose_name = _("User Answer")
        verbose_name_plural = _("User Answers")


# ------------------------
# Chapter Analyse Video
# ------------------------

class ChapterAnalyseVideo(BaseModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    video = models.FileField(upload_to="analysis/")
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.chapter.title

    class Meta:
        verbose_name = _("Chapter Analyse Video")
        verbose_name_plural = _("Chapter Analyse Videos")


# ------------------------
# Plan (Subscription)
# ------------------------

class Plan(BaseModel):
    class PlanType(models.TextChoices):
        YEARLY = "yearly", "Yillik"
        MONTHLY = "monthly", "Oylik"

    title = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    type = models.CharField(max_length=25, choices=PlanType.choices, default=PlanType.MONTHLY)
    included_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plans")
