from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction
import threading

def trigger_signals(request):
    # Signal 1 & 2 (Synchronous + Thread)

    print(f"Main code running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')
    print("User created, signal should have been processed. This proved signal executed synchronously")

    # Signal 3 (Transaction)
    try:
        with transaction.atomic():
            user2 = User.objects.create(username='testuser2')
            raise Exception("Rolling back the transaction")
    except Exception as e:
        print(f"Exception: {e}")
    
    user_exists = User.objects.filter(username='testuser2').exists()
    print(f"User exists after transaction? : {user_exists}")

    return HttpResponse("Signals triggered")
