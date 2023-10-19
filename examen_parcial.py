def f(x):"gestion de tareas diarias"
dia=input("ingrese el dia de la semana: lunes,martes,miercoles,jueves,viernes,sabado,domingo.  ")
hora=float(input("ingrese la hora actual en formato de 24 hrs.  "))
tarea=input("ingrese el tipo de tarea: estudio,deportes,descanso,trabajo.  ")

if hora<= 5:
  print("debes estar dormido")
elif 5<hora<14:
  print("debes estar en clase")
elif 14<hora<22:
  print("puedes hacer tareas")
if tarea=="descanso" and 18<hora<22:
  print("ademas de tomar una siesta puedes comenzar a hacer tus tareas")
