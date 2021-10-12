# Generated by Django 3.2.8 on 2021-10-12 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210517_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=gag.helpers.UploadTo('comment')),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.post_comment'),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.post'),
        ),
        migrations.AlterField(
            model_name='post_comment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]