# Generated by Django 4.1.3 on 2022-11-12 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_document_markdown_voicemessage_delete_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='voicemessage',
            name='dialogId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]