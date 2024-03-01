# conversor 
segundos_str = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos_str // 86400
horas = (segundos_str % 86400) // 3600
minutos = ((segundos_str % 86400) % 3600) // 60
segundos = ((segundos_str % 86400) % 3600) % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")