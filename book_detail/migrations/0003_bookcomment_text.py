# Generated by Django 4.0.2 on 2022-02-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_detail', '0002_bookcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomment',
            name='text',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_detail', '0002_bookcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomment',
            name='text',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
