from django.db import models

class Item(models.Model):
    item_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BigIntegerField()

    def __str__(self):
        return f"{self.name} Item_ID:{self.item_id}"


def create_item(item_id:str, name:str, price:float, in_stock:int) -> object:
    return Item.objects.create(
        item_id=item_id, name=name, price=price, in_stock=in_stock
    )


def view_all_items() -> list:
    return Item.objects.all()


def search_item_by_name(name:str) -> None:
    return Item.objects.filter(name=name)


def get_item(item_id:str) -> list:
    return Item.objects.get(item_id=item_id)


def update_item(add:bool, quantity:int, item_id:str) -> None:
    item = Item.objects.get(item_id=item_id)
    item.in_stock += quantity if add else -(quantity)
    item.save()


def delete_item(item_id:str) -> None:
    Item.objects.get(item_id=item_id).delete()
