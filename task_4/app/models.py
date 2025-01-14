from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_attendee(self):
        return ", ".join([attendee.name for attendee in Order_Item.objects.filter(order_id=self.id)])


class Order_Item(models.Model):
    name = models.CharField(max_length=256)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
