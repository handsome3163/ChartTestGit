#export DJANGO_SETTINGS_MODULE=charts.settings

print "Populating Earth with Serial..."


import datetime

from django.db import models
from django.utils import timezone
import os
import sys
import django
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts.settings')
django.setup()

from charts.models import ECoG
from django.utils import timezone

i=0
word_count = 2
index = (word_count-1)*6
x =0


import serial

ser = serial.Serial('/dev/serial/by-id/usb-Texas_Instruments_XDS110__02.03.00.07__Embed_with_CMSIS-DAP_L1000912-if00', 115200, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)

ser.flushInput()
ser.flushOutput()

while True:
    data_raw = ser.readline()[0:-2];
    if (data_raw[0]=="[" and "[" not in data_raw[1:-1]):
        data_raw = data_raw[1:-1]
        print(data_raw[index :index +5])

        x = int(data_raw[index :index +5].replace(" ",""),16)
        print(x)
        q = ECoG(Value=x, Time=timezone.now())
        q.save()
        queryset = ECoG.objects.all()
