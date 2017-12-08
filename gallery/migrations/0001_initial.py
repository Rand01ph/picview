# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 01:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='分类名称')),
                ('order_by', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=60, verbose_name='密码')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('salt', models.CharField(max_length=29, verbose_name='salt值')),
                ('is_active', models.BooleanField(default=False, verbose_name='激活标志')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Client', verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='相册标题')),
                ('order_by', models.IntegerField(default=0, verbose_name='排序')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('category', models.ManyToManyField(to='gallery.Category', verbose_name='分类')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name_plural': '相册',
                'verbose_name': '相册',
            },
        ),
        migrations.CreateModel(
            name='HighCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='大类名称')),
                ('order_by', models.IntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name_plural': '大类',
                'verbose_name': '大类',
            },
        ),
        migrations.CreateModel(
            name='UploadImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True, verbose_name='图片标题')),
                ('ext', models.CharField(blank=True, max_length=32, null=True, verbose_name='文件类型')),
                ('md5', models.CharField(blank=True, max_length=32, null=True, verbose_name='MD5')),
                ('size', models.BigIntegerField(blank=True, null=True, verbose_name='文件大小')),
                ('file', models.ImageField(upload_to=gallery.models.UploadImg.get_file_path, verbose_name='图片文件')),
                ('order_by', models.IntegerField(default=0, verbose_name='排序')),
                ('is_cover', models.BooleanField(default=False, verbose_name='是否相册封面')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery', verbose_name='所属相册')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
            ],
            options={
                'verbose_name_plural': '图片',
                'verbose_name': '图片',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery', verbose_name='评论相册'),
        ),
        migrations.AddField(
            model_name='category',
            name='high_cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.HighCategory', verbose_name='大类'),
        ),
    ]
