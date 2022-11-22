from datetime import datetime
data = datetime.now()

hora = data.hour
minutos = data.minute

if hora >= 19:
    print("Es hora de irse a casa")
else:
    print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))

