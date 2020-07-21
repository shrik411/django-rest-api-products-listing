from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=False)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True , related_name='children', on_delete=models.SET_NULL)

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of
        
        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])