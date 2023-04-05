# Generated by Django 4.1.6 on 2023-04-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_labeling', '0003_news_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='sentiment',
            field=models.CharField(blank=True, choices=[('positive', 'positive'), ('neutral', 'neutral'), ('negative', 'negative'), ('mixed', 'mixed')], max_length=15, null=True),
        ),
    ]