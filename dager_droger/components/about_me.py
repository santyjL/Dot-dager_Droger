import reflex as rx

from dager_droger.styles import Colores, Tamaños


def about_me_image() -> rx.Component:
    return rx.box(
                rx.image(src="/droger.png" , border_radius=Tamaños.BORDER_RADIUS_GRANDE.value),
                min_width="35%",
                min_height = "50%",
                max_width = "75px",
                max_height = "550px",
                padding=Tamaños.PADDING.value,
                margin=Tamaños.MARGIN_MEDIANO.value,
                bg =Colores.PRINCIPAL.value,
                box_shadow = Colores.NEON_PRINCIPAL.value,
                border_radius = Tamaños.BORDER_RADIUS_GRANDE.value
    )

def about_me() -> rx.Component:
    return rx.box(
        rx.text(
            "Dot-Dager o Droger, me dicen de muchas formas cuando consumo Falopa",
            color = Colores.TITULO.value,
            font_family = "Permanent Marker",
            font_size = "2.5em",
            font_weight="bold",
            max_width="95%",
            margin=Tamaños.MARGIN_MEDIANO.value
        ),

        rx.center(
            rx.text(
                    "Droger es un personaje que siempre está al borde, como un 'código' que se compila pero nunca se ejecuta. Es como el amigo que solo aparece cuando hay falopa, ¿no te parece? ¿O tenés algún amigo más pelotudo?",
                color= Colores.TEXTO.value,
                font_family = "MerriWeather",
                font_size = "1.5em",
                max_width= "95%",
                align="left",
                margin_x=Tamaños.MARGIN_MEDIANO.value
            ),
        )
    )
