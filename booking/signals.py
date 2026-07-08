from django.db.models.signals import post_save
from django.dispatch import receiver
from booking.models import Bus,Seat

@receiver(post_save,sender=Bus)
def createSeatsForBus(sender,instance,created,**kwargs):
    if created:
        for     i in range(1,instance.number_of_seats+1):
            Seat.objects.create(bus=instance,seat_number=f"S{i}")
