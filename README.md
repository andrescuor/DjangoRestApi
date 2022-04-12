# DjangoRestApi
Interview project
CHECKLIST

1. Crear 3 modelos 
	Equipo:
		id = PK
		Nombre Equipo
		Imagen Bandera
		Escudo Equipo
	Jugadores:
		id = PK
		Foto Jugador (jpeg)
		Nombre (CHAR)
		Apellido (CHAR)
		Fecha de Nacimiento (DATE)
		Posicion en la que juega (INT)
		Numero de Camiseta (INT)
		Es Titular? (BOOLEAN)
		FK = EQUIPO
	Cuerpo Tecnico
		id = PK
		Nombre (CHAR)
		Apellido (CHAR)
		Fecha de Nacimiento (DATE)
		Nacionalidad (COLOMBIA)
		Rol(Tecnico|medico|preparador) (multiselect)
		FK = EQUIPO

2. Que debemos hacer
	**Crear Equipos (REGISTRO-VALIDACION)
	**Crear jugadores (REGISTRO-VALIDACION)
	**Crear Equipo tecnico (REGISTRO-VALIDACION)

3. Crear un servicio que contenga


	**Cual es la edad promedio de los jugadores (AVG-PLAYERS)
	
	**Quien es el mas Joven (MAX-PLAYERS)
	**Quien es el mas viejo (MIN-PLAYERS)
	**Cual equipo registro mas jugadoreS (COUNT-TEAMS OR PLAYERS)
	**Cual es el promedio de numero de jugadores en cada equipo (AVG-PLAYERS)
	**Total de Jugadores que participaran en el campeonato (SUM-PLAYERS
	**Cuantos suplentes hay (SUM-PLAYERS)
	**Cuantos equipos hay registrados (SUM-TEAMS)
	**Quien es el tecnico mas viejo (MIN-STAFF)


ENDPOINTS

PLAYERS:
# CRUD ENDPOINTS
	api/player/create/
	api/player/list/
	api/player/update/<pk>/
	api/player/delete/<pk>/

# OTHER ENDPOINTS PLAYERS
    # Total de jugadores
    api/player/get-total/
    # Total de suplentes
    api/player/get-total-sub/
    # Jugador mas Joven
    api/player/get-youngest/
    # Jugador mas viejo
    api/player/get-oldest/
    # Promedio Jugadores por equipo
    api/player/get-average/
    # Promedio Edad Jugadores
    api/player/age-avg/

TEAMS:
    # CRUD ENDPOINTS
    api/team/create/
    api/team/list/
    api/team/review/<pk>
    api/team/update/<pk>
    api/team/delete/<pk>


    # OTHER ENDPOINTS
    # Tecnico mas viejo
    path('get-oldest/', views.StaffOldestManager.as_view()),

STAFF:
    # CRUD ENDPOINTS
    api/staff/create/
    api/staff/list/
    api/staff/update/<pk>
    api/staff/delete/<pk>
    api/staff/review/<pk>

    # OTHER ENDPOINTS
    # Total de equipos registrados
    api/staff/get-total/
