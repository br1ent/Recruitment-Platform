from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    class Role(models.TextChoices):
        JOB_SEEKER = 'job_seeker', '求职者'
        HR_ADMIN = 'hr_admin', 'HR管理员'

    class Status(models.TextChoices):
        ACTIVE = 'active', '正常'
        DISABLED = 'disabled', '禁用'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='关联用户')

    phone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    avatar = models.URLField(blank=True, verbose_name='头像')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True, verbose_name='简历')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER,
        verbose_name='角色',
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
        verbose_name='状态',
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return f'{self.user.username}'
