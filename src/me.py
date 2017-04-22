print "One"

print "Two"

import os
import sys
import django
import time
from django.http import JsonResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts.settings')
django.setup()

x = 10
while True:
    time.sleep(2)
    data = {
        "sales":100,
        "customers":x,
    }
    x = x+1

    JsonResponse(data) #http request





print "Three"
print "Four"
