# Generated by Django 2.0 on 2018-01-18 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Link')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Comment')),
            ],
        ),
    ]
