import reflex as rx

from dager_droger.styles import Colores, Tamaños


# Componente reutilizable para una caja con título y texto dinámico
def caja_interes(titulo: str, texto_hover: str, imagen: str, altura: str, ancho: str, columnas: str, filas: str) -> rx.Component:
    return rx.box(
        # Título siempre visible
        rx.box(
            rx.heading(
                titulo,
                font_family="MerriWeather",
                font_size="2.5em",
                color=Colores.PRINCIPAL.value,
                text_align="center",
                style={
                    "bg" : "#FFFFFF91",
                    "position": "absolute",
                    "top": "10%",  # Ajusta según diseño
                    "left": "50%",
                    "transform": "translateX(-50%)",
                    "transition": "opacity 0.3s ease",  # Animación para desaparecer
                },
                class_name="titulo-visible",
            ),
        ),
        # Texto que aparece en el hover
        rx.box(
            rx.heading(
                texto_hover,
                font_family="MerriWeather",
                font_size="1em",
                color="#FFFFFF",
                text_align="center",
                style={
                    "bg" : "#00000091",
                    "position": "absolute",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "opacity": "0",
                    "transition": "opacity 0.3s ease",  # Animación suave

                },
                class_name="texto-hover",
            ),
        ),
        height=altura,
        width=ancho,
        grid_column=columnas,
        grid_row=filas,
        background_image=f"url('{imagen}')",
        background_size="cover",
        background_position="center",
        border_radius=Tamaños.BORDER_RADIUS.value,
        border=Tamaños.BORDER.value,
        box_shadow=Colores.NEON_TERCIARIO.value,
        position="relative",
        _hover={
            ".texto-hover": {"opacity": "1"},  # Mostrar texto dinámico
            ".titulo-visible": {"opacity": "0"},  # Ocultar título
            "filter": "drop-shadow(2 2 30px #ff5346)",
            "transition": "all 0.5s ease-in-out",
            "transform": "scale(1.05)",
        },
    )


# Generar todas las cajas de intereses
def intereses() -> rx.Component:
    return rx.grid(
        caja_interes(
            titulo="¡Ah, los gatos!",
            texto_hover=(
                "Esos seres misteriosos que parecen más interesados en dormir que en la programación. "
                "Son como los comentarios en el código: no los entiendes, pero sabés que están ahí."
            ),
            imagen="/michulina.jpg",
            altura="60vh",
            ancho="30vw",
            columnas="3",
            filas="span 2",
        ),
        caja_interes(
            titulo="preguntas existenciales con Gatos",
            texto_hover=(
                "Te miran con desdén y te hacen cuestionar tu vida, mientras se sientan sobre tu teclado como "
                "si fueran los dueños del universo."
            ),
            imagen="/filosofo_incognito.png",
            altura="30vh",
            ancho="30vw",
            columnas="1",
            filas="1",
        ),
        caja_interes(
            titulo="El pepino",
            texto_hover=(
                "El pepino en la cama es como un algoritmo ineficiente: prometedor al principio, pero después de "
                "un rato solo te deja con ganas de más... ¡y un dolor de cabeza!"
            ),
            imagen="/pepinos.png",
            altura="30vh",
            ancho="60vw",
            columnas="span 2",
            filas="2",
        ),
        caja_interes(
            titulo="La falopa ",
            texto_hover=(
                "Bueno, si a vos te gusta, ¡está bien! Pero ojo, con la falopa hay que cuidar el 'garbage collection' "
                "o terminás haciendo un 'stack overflow' de otro nivel."
            ),
            imagen="/falopa.png",
            altura="30vh",
            ancho="60vw",
            columnas="span 2",
            filas="3",
        ),
        caja_interes(
            titulo="Programar en C#",
            texto_hover=(
                "Es como una buena relación: al principio todo parece sencillo y limpio, pero con el tiempo te "
                "encontrás con bugs inesperados y necesitas refactorizar constantemente."
            ),
            imagen="/la_buena.jpg",
            altura="30vh",
            ancho="60vw",
            columnas="span 2",
            filas="1",
        ),
        columns="3",
        spacing="3",
        width="98%",
        align="center",
        margin=Tamaños.MARGIN_MEDIANO.value,
        bg=Colores.PRINCIPAL.value,
        border_radius=Tamaños.BORDER_RADIUS.value,
        border=Tamaños.BORDER.value,
        padding=Tamaños.PADDING.value,
    )
