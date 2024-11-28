import reflex as rx

from dager_droger.styles import Colores, Tamaños


def un_programador_y_su_gato_pepino() -> rx.Component:
    return rx.center(
            rx.audio(
                url="/temardo.mp3",
                playing=True ,
                width="350px" , height="64px",
                bg = Colores.PRINCIPAL.value,
                border_radius=Tamaños.BORDER_RADIUS.value,
                border=Tamaños.BORDER.value,
                box_shadow = Colores.NEON_TERCIARIO.value,
                padding=Tamaños.PADDING.value,
                margin_x= Tamaños.MARGIN_GRANDE.value,
            ),
            width="99vw",
    )