from django.db import models


# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=100)
    MyClass = models.CharField(max_length=20)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class User(models.Model):
    # id = models.CharField(max_length=20)
    LIKES = (
        ('差評','bad'),
        ('中等','normal'),
        ('好','good'),
    )
    like = models.CharField(max_length=1,choices=LIKES)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

#搜尋 ID
def search_id(**kwargs):
    id = kwargs.get('id')
    try:
        if id:
            result = Item.objects.extra(where=['id = %s'],params = [id])
        else:
            result = Item.objects.all()
    except Exception as e:
        return e.args
    return result