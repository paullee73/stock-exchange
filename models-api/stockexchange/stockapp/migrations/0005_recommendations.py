# Generated by Django 2.1 on 2019-05-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0004_stock_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=1)),
                ('recommended_items', models.CharField(max_length=5)),
            ],
        ),
    ]
