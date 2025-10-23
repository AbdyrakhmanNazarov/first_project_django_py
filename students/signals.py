from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Student, StudentContract


@receiver(post_save, sender=Student)
def student_contract_create_signal(sender, instance: Student, created, **kwargs):

    if created:
        StudentContract.objects.get_or_create(student=instance)


@receiver(post_delete, sender=Student)
def student_contract_delete_signal(sender, instance: Student, **kwargs):

    try:
        instance.contract.delete()
    except StudentContract.DoesNotExist:
        pass