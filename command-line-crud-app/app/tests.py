from django.test import TestCase

from django.test import TestCase
from .models import (
    Item,
    create_item,
    view_all_items,
    search_item_by_name,
    get_item,
    update_item,
    delete_item,
)


class ItemModelTest(TestCase):
    # Model Test Cases begin
    def setUp(self):
        Item.objects.create(item_id="001", name="Item 1", price=10.99, in_stock=100)

    def test_item_creation(self):
        item = Item.objects.get(item_id="001")
        self.assertEqual(item.name, "Item 1")
        self.assertEqual(item.price, 10.99)
        self.assertEqual(item.in_stock, 100)

    def test_item_string_representation(self):
        item = Item.objects.get(item_id="001")
        self.assertEqual(str(item), "Item 1 Item_ID:001")

    def test_create_item(self):
        create_item("002", "Item 2", 15.99, 200)
        item = Item.objects.get(item_id="002")
        self.assertEqual(item.name, "Item 2")
        self.assertEqual(item.price, 15.99)
        self.assertEqual(item.in_stock, 200)

    # Model Test Cases End and Function test Cases Begin
    def test_view_all_items(self):
        items = view_all_items()
        self.assertEqual(items.count(), 1)

    def test_search_item_by_name(self):
        create_item("003", "Item 3", 12.99, 150)
        items = search_item_by_name("Item 3")
        self.assertEqual(items.count(), 1)

    def test_get_item(self):
        create_item("004", "Item 4", 9.99, 300)
        item = get_item("004")
        self.assertEqual(item.name, "Item 4")

    def test_update_item(self):
        create_item("005", "Item 5", 8.99, 250)
        update_item(True, 50, "005")
        item = Item.objects.get(item_id="005")
        self.assertEqual(item.in_stock, 300)

    def test_delete_item(self):
        create_item("006", "Item 6", 7.99, 180)
        items = Item.objects.filter(item_id = "006")
        self.assertEqual(items.count(), 1)
        delete_item("006")
        self.assertEqual(items.count(), 0)
