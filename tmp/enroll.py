from django.db import models

# Create your models here.
class Enroll(models.Model):
    # first_name = models.CharField(max_length=100)
    class Meta:
        db_table = "enrolls"

def getEnroll():
    return Enroll.objects.all()

# def create_user():
#     User.objects.filter(firstName="Snoopy",lastName="Lee").update(firstName="Emily")
#
# def create_articles(content):
#     Articles.objects.create(user= user, content=content)
#     return


# def get_articles():
#     return Enroll.objects.all()
    # return Articles.objects.filter(user = user).all().order_by("-last_update")


#def get_article_owner():
    #article = Articles.objects.get(id=2)
    #user = article.user

    #user = Articles.objects.get(id=2).select_related('user')

# multiple models
# https://www.jianshu.com/p/1fccbbf72204