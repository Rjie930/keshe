from django.db import models

# Create your models here.
class Status(models.TextChoices):
    UNSTARTED = 'u', "还未开始的活动"
    ONGOING = 'o', "正在进行的活动"
    FINISHED = 'f', "已经完成的活动"


class Task(models.Model):
    name = models.CharField(verbose_name="活动名称", max_length=65, unique=True)
    status = models.CharField(verbose_name="活动类型", max_length=1, choices=Status.choices)
    class Meta:
        verbose_name = "任务信息"
        verbose_name_plural = "任务内容"

    def __str__(self):
        return self.name