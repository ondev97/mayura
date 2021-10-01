import random
import string

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.timezone import now

# Create your models here.

class HomeSection(models.Model):
    class Meta:
        verbose_name_plural = 'Home Section'

    title_1 = models.CharField(max_length=250)
    title_2 = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    image = models.ImageField(upload_to='images/homepage')

    def __str__(self):
        return self.title_2

class ProductSection(models.Model):
    class Meta:
        verbose_name_plural = 'Product Section'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        verbose_name_plural = 'Product'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/homepage/products')
    url = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

class MaterialSection(models.Model):
    class Meta:
        verbose_name_plural = 'Material Section'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    sub_title = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='images/homepage/materials')
    name_1 = models.CharField(max_length=250)
    image_2 = models.ImageField(upload_to='images/homepage/materials')
    name_2 = models.CharField(max_length=250)
    image_3 = models.ImageField(upload_to='images/homepage/materials')
    name_3 = models.CharField(max_length=250)
    image_4 = models.ImageField(upload_to='images/homepage/materials')
    name_4 = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class TestimonialSection(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonial Section'

    title = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    image_1 = models.ImageField(upload_to='images/homepage/testimonials')
    name_1 = models.CharField(max_length=250)
    prof_1 = models.CharField(max_length=250)
    content_1 = RichTextField(blank=True)

    image_2 = models.ImageField(upload_to='images/homepage/testimonials')
    name_2 = models.CharField(max_length=250)
    prof_2 = models.CharField(max_length=250)
    content_2 = RichTextField(blank=True)

    image_3 = models.ImageField(upload_to='images/homepage/testimonials')
    name_3 = models.CharField(max_length=250)
    prof_3 = models.CharField(max_length=250)
    content_3 = RichTextField(blank=True)

    def __str__(self):
        return self.title

class VideoBlogSection(models.Model):
    class Meta:
        verbose_name_plural = 'Video & Blog Section'

    video_title = models.CharField(max_length=250)
    video_description = RichTextField(blank=True)
    video_url_1 = models.CharField(max_length=1000, null=True, blank=True)
    video_url_2 = models.CharField(max_length=1000, null=True, blank=True)

    blog_title = models.CharField(max_length=250)
    blog_description = RichTextField(blank=True)

    def __str__(self):
        return self.video_title+" "+self.blog_title

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class BlogPost(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Post'

    title = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=250, blank=True)
    excerpt = models.TextField(max_length=220, null=True, blank=True)
    content_1 = RichTextField(blank=True)
    is_content_2_in_quotation = models.BooleanField(default=False)
    content_2 = RichTextField(blank=True)
    content_3 = RichTextField(blank=True)
    image = models.ImageField(upload_to='images/blog')
    date = models.DateField(default=now)
    display_in_homepage = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250,unique=True,null=True,blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug()+"-"+self.title)
        super(BlogPost,self).save(*args,**kwargs)

class WhoAreWe(models.Model):
    class Meta:
        verbose_name_plural = 'Who Are We'

    title_1 = models.CharField(max_length=250)
    title_2 = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    image_1 = models.ImageField(upload_to='images/whoarewe')
    image_2 = models.ImageField(upload_to='images/whoarewe')

    def __str__(self):
        return self.title_1

class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = 'Map'

    title = models.CharField(max_length=250, default="")
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.url

class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'Comments'

    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = RichTextField(blank=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    website = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPage(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Page'

    title_1 = models.CharField(max_length=250)
    title_2 = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.title_1

