from io import BytesIO

from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User
from django.db import models


# Category of post


class Category(models.Model):
    name = models.CharField("Category Name", max_length=255)
    slug = models.SlugField("Category Slug", unique=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


# Sub Category


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField("Sub Category Name", max_length=255)
    slug = models.SlugField("Sub Category Slug", unique=True)
    image = models.ImageField("Sub Category Image", null=True)

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Sub Category'

    def __str__(self):
        return f'{self.category.name} => {self.name}'

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Post(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name='post', on_delete=models.CASCADE)
    post_title = models.CharField("Post Title", max_length=255)
    slug = models.SlugField("Post Slug", unique=True)
    post_description = models.TextField("Post Description", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    date_added = models.DateTimeField("Post Added Date", auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return f'{self.id}  {self.post_title}'

    def get_absolute_url(self):
        return f'/{self.sub_category.category.slug}/{self.sub_category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Comments(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="postComment", on_delete=models.CASCADE)
    comment = models.TextField("Comment On Post", max_length=500)
    date = models.DateField("Comment Date", auto_now_add=True)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Comment'

    def __str__(self):
        return f' Post Title ==>  {self.post.post_title}'

    def get_absolute_url(self):
        return f'/{self.post.slug}/'


class ContactUs(models.Model):
    first_name = models.CharField("First Name", max_length=30, blank=False, null=False)
    last_name = models.CharField("Last Name", max_length=30, blank=False, null=False)
    email = models.EmailField("Email", max_length=50, blank=False, null=False)
    phone = models.IntegerField("Contact No.", null=False, blank=False)
    subject = models.CharField("Subject", max_length=60)
    message = models.TextField("Message", max_length=500)
    date = models.DateField("Contact Date", auto_now_add=True)

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Contact Us'

    def __str__(self):
        return self.subject