from django.db import models

# Create your models here.
class PictureAndData(models.Model):
    localisation=models.TextField()
    GPS=models.TextField()
    photo=models.ImageField(upload_to="photos/")
    photoPath=models.TextField()
    commentary=TextField()
    id=models.Integer.Field()
    idUser=TextField()

    def __str__(self,_localisation,_GPS,_photo,_commentary,_id,_idUser):
        self.localisation=_localisation
        self.GPS=_GPS
        self.photo=_photo
        self.commentary=_commentary
        self.id=_id
        self.idUser=_idUser
        self.photoPath=self.photo.path
        return self
    
