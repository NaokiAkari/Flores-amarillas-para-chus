import turtle
import random
import math

# ============================================================
# CONFIGURACIÓN DE LA VENTANA
# ============================================================

pantalla = turtle.Screen()
pantalla.setup(width=1300, height=750)
pantalla.title("🌻 Feliz Día de las Flores Amarillas 🌻")
pantalla.bgcolor("black")
pantalla.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

random.seed(20)


# ============================================================
# FUNCIONES BÁSICAS
# ============================================================

def ir(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def punto(x, y, tamaño, color):
    ir(x, y)
    t.dot(tamaño, color)


def circulo(x, y, radio, color):
    ir(x, y - radio)
    t.color(color)
    t.begin_fill()
    t.circle(radio)
    t.end_fill()


# ============================================================
# ESTRELLAS
# ============================================================

def estrella_brillante(x, y, tamaño):

    t.color("#FFD700")
    t.pensize(2)

    # Línea vertical
    ir(x, y)
    t.goto(x, y + tamaño)
    ir(x, y)
    t.goto(x, y - tamaño)

    # Línea horizontal
    ir(x, y)
    t.goto(x + tamaño, y)
    ir(x, y)
    t.goto(x - tamaño, y)

    # Diagonal 1
    ir(x, y)
    t.goto(
        x + tamaño * 0.7,
        y + tamaño * 0.7
    )

    ir(x, y)
    t.goto(
        x - tamaño * 0.7,
        y - tamaño * 0.7
    )

    # Diagonal 2
    ir(x, y)
    t.goto(
        x - tamaño * 0.7,
        y + tamaño * 0.7
    )

    ir(x, y)
    t.goto(
        x + tamaño * 0.7,
        y - tamaño * 0.7
    )


# Estrellas pequeñas

for i in range(100):

    x = random.randint(-620, 620)
    y = random.randint(40, 350)

    tamaño = random.choice([2, 3, 4, 5])

    punto(
        x,
        y,
        tamaño,
        "#FFD92E"
    )


# Estrellas grandes

estrellas = [
    (-510, 270, 13),
    (-350, 315, 10),
    (-80, 300, 12),
    (80, 330, 10),
    (280, 300, 12),
    (470, 275, 14),
    (580, 160, 9),
    (-220, 170, 9),
    (350, 160, 8)
]

for x, y, tamaño in estrellas:
    estrella_brillante(x, y, tamaño)


# ============================================================
# LUNA
# ============================================================

# Halo de la luna

circulo(
    500,
    260,
    82,
    "#171300"
)

# Luna amarilla

circulo(
    500,
    260,
    65,
    "#FFE66D"
)

# Parte negra para crear la luna creciente

circulo(
    470,
    280,
    60,
    "black"
)

# Detalles de la luna

punto(525, 285, 7, "#F5D84A")
punto(515, 240, 5, "#F5D84A")
punto(545, 265, 4, "#F5D84A")


# ============================================================
# CORAZONES
# ============================================================

def corazon(x, y, tamaño):

    t.color("#FFD21C")
    t.pensize(3)

    ir(x, y)

    t.setheading(140)

    t.forward(tamaño)

    t.circle(-tamaño / 2, 200)

    t.left(120)

    t.circle(-tamaño / 2, 200)

    t.forward(tamaño)


corazon(-470, 210, 25)
corazon(360, 190, 25)
corazon(180, -120, 20)
corazon(-180, -90, 20)
corazon(520, 50, 18)


# ============================================================
# MARIPOSA
# ============================================================

def mariposa(x, y, tamaño):

    # Alas superiores
    circulo(
        x - tamaño,
        y + tamaño // 2,
        tamaño // 2,
        "#FFD21C"
    )

    circulo(
        x + tamaño,
        y + tamaño // 2,
        tamaño // 2,
        "#FFD21C"
    )

    # Alas inferiores
    circulo(
        x - tamaño,
        y - tamaño // 2,
        tamaño // 2,
        "#F5C400"
    )

    circulo(
        x + tamaño,
        y - tamaño // 2,
        tamaño // 2,
        "#F5C400"
    )

    # Cuerpo
    ir(x, y - tamaño)

    t.color("#8A5000")
    t.pensize(5)

    t.goto(x, y + tamaño)

    # Antenas
    t.pensize(2)

    ir(x, y + tamaño)
    t.goto(
        x - 10,
        y + tamaño + 15
    )

    ir(x, y + tamaño)
    t.goto(
        x + 10,
        y + tamaño + 15
    )


mariposa(-480, 170, 10)


# ============================================================
# TÍTULO
# ============================================================

ir(0, 125)

t.color("#FFD21C")

t.write(
    "Feliz día de las",
    align="center",
    font=("Comic Sans MS", 42, "bold")
)

ir(0, 65)

t.write(
    "Flores Amarillas CHUS :3",
    align="center",
    font=("Comic Sans MS", 42, "bold")
)


# ============================================================
# DECORACIÓN DEL TÍTULO
# ============================================================

t.color("#FFD21C")
t.pensize(5)

# Decoración izquierda

ir(-390, 95)
t.setheading(160)
t.forward(30)

ir(-385, 70)
t.setheading(170)
t.forward(25)

# Decoración derecha

ir(390, 95)
t.setheading(20)
t.forward(30)

ir(385, 70)
t.setheading(10)
t.forward(25)


# ============================================================
# MENSAJE
# ============================================================

t.color("#FFD92E")

ir(0, 5)

t.write(
    "recuerda que eres una persona increible ^^",
    align="center",
    font=("Comic Sans MS", 20, "normal")
)

ir(0, -30)

t.write(
    "espero no ser el unico ",
    align="center",
    font=("Comic Sans MS", 20, "normal")
)

ir(0, -65)

t.write(
    "que te haga un detalle asi nwn",
    align="center",
    font=("Comic Sans MS", 20, "normal")
)

ir(0, -100)

t.write(
    "abrazos amifita OwO",
    align="center",
    font=("Comic Sans MS", 20, "normal")
)


# ============================================================
# TALLOS
# ============================================================

def tallo(x, y, altura, grosor):

    ir(x, y)

    t.color("#218B21")
    t.pensize(grosor)

    t.setheading(90)
    t.forward(altura)


# ============================================================
# HOJAS
# ============================================================

def hoja(x, y, tamaño, angulo):

    ir(x, y)

    t.setheading(angulo)

    t.color("#2E8B22")

    t.begin_fill()

    t.circle(tamaño, 70)

    t.left(110)

    t.circle(tamaño, 70)

    t.end_fill()

    # Nervadura de la hoja

    ir(x, y)

    t.setheading(angulo)

    t.color("#66A833")
    t.pensize(2)

    t.forward(tamaño * 1.2)


# ============================================================
# PÉTALOS DEL GIRASOL
# ============================================================

def petalo_girasol(x, y, tamaño, angulo):

    # --------------------------------------------------------
    # El pétalo se construye alrededor del punto central.
    # Esto evita que los pétalos queden separados del centro.
    # --------------------------------------------------------

    rad = math.radians(angulo)

    # Dirección del pétalo
    dx = math.cos(rad)
    dy = math.sin(rad)

    # Dirección perpendicular
    px = -dy
    py = dx

    # Dimensiones
    largo = tamaño * 1.35
    ancho = tamaño * 0.38

    # Centro del pétalo
    centro_x = x + dx * tamaño * 0.60
    centro_y = y + dy * tamaño * 0.60

    puntos = []

    # --------------------------------------------------------
    # PARTE SUPERIOR DEL PÉTALO
    # --------------------------------------------------------

    for i in range(21):

        angulo_curva = math.pi * i / 20

        local_x = math.cos(angulo_curva) * largo * 0.50
        local_y = math.sin(angulo_curva) * ancho

        nuevo_x = (
            centro_x
            + dx * local_x
            + px * local_y
        )

        nuevo_y = (
            centro_y
            + dy * local_x
            + py * local_y
        )

        puntos.append(
            (nuevo_x, nuevo_y)
        )

    # --------------------------------------------------------
    # PARTE INFERIOR DEL PÉTALO
    # --------------------------------------------------------

    for i in range(20, -1, -1):

        angulo_curva = math.pi * i / 20

        local_x = math.cos(angulo_curva) * largo * 0.50
        local_y = -math.sin(angulo_curva) * ancho

        nuevo_x = (
            centro_x
            + dx * local_x
            + px * local_y
        )

        nuevo_y = (
            centro_y
            + dy * local_x
            + py * local_y
        )

        puntos.append(
            (nuevo_x, nuevo_y)
        )

    # --------------------------------------------------------
    # DIBUJAR EL PÉTALO
    # --------------------------------------------------------

    t.color("#FFD21C")
    t.begin_fill()

    ir(
        puntos[0][0],
        puntos[0][1]
    )

    for px_actual, py_actual in puntos[1:]:

        t.goto(
            px_actual,
            py_actual
        )

    t.goto(
        puntos[0][0],
        puntos[0][1]
    )

    t.end_fill()


# ============================================================
# GIRASOL
# ============================================================

def girasol(x, y, tamaño):

    # ========================================================
    # 1. TALLO
    # ========================================================

    tallo(
        x,
        y - tamaño * 3.8,
        tamaño * 4.8,
        max(4, int(tamaño / 5))
    )

    # ========================================================
    # 2. HOJAS
    # ========================================================

    hoja(
        x,
        y - tamaño * 2.2,
        tamaño * 1.1,
        145
    )

    hoja(
        x,
        y - tamaño * 3.2,
        tamaño * 1.0,
        35
    )

    # ========================================================
    # 3. PÉTALOS AMARILLOS
    # ========================================================

    # Primera fila de pétalos

    for angulo in range(0, 360, 30):

        petalo_girasol(
            x,
            y,
            tamaño,
            angulo
        )

    # Segunda fila de pétalos

    for angulo in range(15, 360, 30):

        petalo_girasol(
            x,
            y,
            tamaño * 0.82,
            angulo
        )

    # ========================================================
    # 4. CENTRO MARRÓN
    # ========================================================
    #
    # IMPORTANTE:
    #
    # Los pétalos se dibujan primero.
    # El centro se dibuja DESPUÉS.
    #
    # x,y es exactamente el centro de la flor.
    #
    # De esta manera el marrón queda ENCIMA de los pétalos
    # y exactamente en el medio.
    # ========================================================

    circulo(
        x,
        y,
        tamaño * 0.52,
        "#7A3B00"
    )

    circulo(
        x,
        y,
        tamaño * 0.37,
        "#3B1800"
    )

    # ========================================================
    # 5. SEMILLAS DEL CENTRO
    # ========================================================

    for i in range(20):

        angulo = random.uniform(
            0,
            math.pi * 2
        )

        radio = random.uniform(
            tamaño * 0.10,
            tamaño * 0.40
        )

        semilla_x = (
            x
            + math.cos(angulo) * radio
        )

        semilla_y = (
            y
            + math.sin(angulo) * radio
        )

        punto(
            semilla_x,
            semilla_y,
            3,
            "#D99A20"
        )


# ============================================================
# GIRASOLES GRANDES
# ============================================================

girasol(
    -500,
    -135,
    48
)

girasol(
    -260,
    -230,
    38
)

girasol(
    245,
    -225,
    38
)

girasol(
    500,
    -130,
    48
)


# ============================================================
# GIRASOLES PEQUEÑOS
# ============================================================

girasol(
    -60,
    -270,
    25
)

girasol(
    100,
    -275,
    23
)

girasol(
    370,
    -260,
    27
)


# ============================================================
# PASTO
# ============================================================

def pasto(x, y, altura):

    t.color(
        random.choice([
            "#0D5018",
            "#146B1E",
            "#208522",
            "#2A9525"
        ])
    )

    t.pensize(
        random.choice([2, 3, 4])
    )

    ir(x, y)

    t.setheading(
        random.randint(65, 115)
    )

    t.forward(altura)


# Dibujar mucho pasto

for x in range(-640, 641, 8):

    altura = random.randint(20, 80)

    pasto(
        x,
        -360,
        altura
    )


# ============================================================
# HOJAS EXTRA
# ============================================================

hojas_extra = [

    (-570, -310, 35, 60),
    (-540, -335, 30, 120),

    (-430, -330, 32, 50),
    (-350, -340, 30, 130),

    (-150, -330, 35, 60),
    (-100, -340, 28, 120),

    (150, -335, 35, 50),
    (200, -340, 28, 130),

    (300, -330, 35, 60),
    (420, -330, 32, 120),

    (550, -310, 38, 60)
]

for x, y, tamaño, angulo in hojas_extra:

    hoja(
        x,
        y,
        tamaño,
        angulo
    )


# ============================================================
# FLORES PEQUEÑAS
# ============================================================

def flor_pequena(x, y, tamaño):

    # Pétalos

    for angulo in range(0, 360, 72):

        px = (
            x
            + math.cos(math.radians(angulo))
            * tamaño
        )

        py = (
            y
            + math.sin(math.radians(angulo))
            * tamaño
        )

        punto(
            px,
            py,
            tamaño * 1.2,
            "#FFD21C"
        )

    # Centro

    punto(
        x,
        y,
        tamaño * 0.9,
        "#8A4800"
    )


# Crear muchas flores pequeñas

for i in range(35):

    x = random.randint(-600, 600)
    y = random.randint(-350, -270)

    tamaño = random.randint(5, 9)

    flor_pequena(
        x,
        y,
        tamaño
    )


# ============================================================
# HOJAS PEQUEÑAS EXTRA
# ============================================================

for i in range(25):

    x = random.randint(-620, 620)
    y = random.randint(-350, -280)

    tamaño = random.randint(10, 18)

    hoja(
        x,
        y,
        tamaño,
        random.randint(20, 160)
    )


# ============================================================
# LUCES DORADAS
# ============================================================

for i in range(20):

    x = random.randint(-600, 600)
    y = random.randint(-220, 100)

    punto(
        x,
        y,
        random.randint(3, 7),
        "#FFD21C"
    )


# ============================================================
# MOSTRAR EL DIBUJO
# ============================================================

pantalla.update()

turtle.done()