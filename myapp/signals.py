# myapp/signals.py
import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

# Question 1: Proving Django signals are synchronous
@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)
    print("Signal handler finished.")

# Question 2: Proving that Django signals run in the same thread
@receiver(post_save, sender=User)
def thread_check_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Question 3: Proving that Django signals run in the same transaction
@receiver(post_save, sender=User)
def transaction_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler: User created with username {instance.username}")
