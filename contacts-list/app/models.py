from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_favorite = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.name}"


def create_contact(name: str, email: str, phone: str, is_favorite: bool) -> object:
    return Contact.objects.create(
        name=name, email=email, phone=phone, is_favorite=is_favorite
    )


def all_contacts() -> list:
    return Contact.objects.all()


def find_contact_by_name(name: str) -> object:
    try:
        return Contact.objects.get(name=name)
    except:
        return None


def favorite_contacts() -> list:
    return Contact.objects.filter(is_favorite=True)


def update_contact_email(name: str, email: str) -> None:
    contact = Contact.objects.get(name=name)
    contact.email = email
    contact.save()


def delete_contact(name: str) -> None:
    Contact.objects.get(name=name).delete()
