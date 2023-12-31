# Generated by Django 4.0.5 on 2022-07-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, default='/gallery/default.jpg', null=True, upload_to='gallery')),
                ('caption', models.TextField(blank=True, default='', max_length=300, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pp',
            field=models.ImageField(blank=True, default='/profiles/default.jpg', null=True, upload_to='profiles'),
        ),
    ]
