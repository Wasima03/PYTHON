#EJERCICIO 1
import mysql.connector

# 1️⃣ Conectamos a la base de datos
try:
    conexion = mysql.connector.connect(
        host="localhost",      # Cambia si tu servidor es otro
        user="tu_usuario",     # Tu usuario de MySQL
        password="tu_contraseña", # Tu contraseña de MySQL
        database="pokedex"     # Nombre de la base de datos
    )

    cursor = conexion.cursor()

    # 2️⃣ Consulta SQL: nombres de Pokémon con altura > 1.5
    consulta = "SELECT nombre FROM pokemon WHERE altura > 1.5"
    cursor.execute(consulta)

    # 3️⃣ Mostrar resultados
    resultados = cursor.fetchall()
    print("Pokemons con altura mayor a 1.5 metros:")
    for fila in resultados:
        print(fila[0])  # fila[0] es el nombre

except mysql.connector.Error as err:
    print(f"Error al conectar o consultar: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
#EJERCICIO 2
import mysql.connector

try:
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",          # Cambiar por tu usuario
        password="tu_contraseña",   # Cambiar por tu contraseña
        database="pokedex"
    )

    cursor = conexion.cursor()

    # Consulta UPDATE: poner en mayúsculas los nombres de Pokémon con peso > 200
    update_sql = "UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200"
    cursor.execute(update_sql)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Número de registros modificados
    print(f"Número de registros modificados: {cursor.rowcount}")

except mysql.connector.Error as err:
    print(f"Error al conectar o actualizar: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
#EJERCICIO 3
import mysql.connector

try:
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",       # Cambiar por tu usuario
        password="tu_contraseña", # Cambiar por tu contraseña
        database="pokedex"
    )

    cursor = conexion.cursor()

    # 1️⃣ Pedir datos al usuario
    nombre = input("Introduce el nombre del Pokémon: ").strip()
    peso = float(input("Introduce el peso del Pokémon (kg): "))
    altura = float(input("Introduce la altura del Pokémon (m): "))

    # 2️⃣ Obtener el número máximo de la Pokédex
    cursor.execute("SELECT MAX(numero) FROM pokemon")
    max_numero = cursor.fetchone()[0]
    if max_numero is None:
        max_numero = 0  # Si la tabla está vacía
    nuevo_numero = max_numero + 1

    # 3️⃣ Insertar el nuevo Pokémon
    sql_insert = "INSERT INTO pokemon (numero, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_insert, (nuevo_numero, nombre, peso, altura))

    # Confirmar cambios
    conexion.commit()

    print(f"Pokémon '{nombre}' añadido con número {nuevo_numero}.")

except mysql.connector.Error as err:
    print(f"Error al conectar o insertar: {err}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
#EJERCICIO 4
import mysql.connector

try:
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",          # Cambiar por tu usuario
        password="tu_contraseña",   # Cambiar por tu contraseña
        database="pokedex"
    )

    cursor = conexion.cursor()

    # 1️⃣ Pedir código al usuario
    codigo = int(input("Introduce el código del Pokémon a eliminar: "))

    # 2️⃣ Comprobar si existe
    cursor.execute("SELECT nombre FROM pokemon WHERE numero = %s", (codigo,))
    resultado = cursor.fetchone()

    if resultado:
        nombre_pokemon = resultado[0]

        # 3️⃣ Eliminar Pokémon
        cursor.execute("DELETE FROM pokemon WHERE numero = %s", (codigo,))
        conexion.commit()
        print(f"Pokémon '{nombre_pokemon}' con código {codigo} eliminado correctamente.")
    else:
        print(f"No existe ningún Pokémon con código {codigo}.")

except mysql.connector.Error as err:
    print(f"Error al conectar o eliminar: {err}")

except ValueError:
    print("El código debe ser un número entero.")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
