import reflex as rx

from dager_droger.styles import Colores, Tamaños


def videos_droger():
    return rx.hstack(
        rx.center(
                rx.video(url="https://www.youtube.com/watch?v=BTDI9Je1UWY" ,
                         height="250px" , width="auto",
                         margin=Tamaños.MARGIN_PEQUEÑO.value,
                         align="center"
                         ),
                rx.video(url="https://www.youtube.com/watch?v=YQfRVo5UwOM" ,
                         height="250px" , width="auto",
                         margin=Tamaños.MARGIN_PEQUEÑO.value,
                         align="center",
                         ),
                rx.video(url="https://www.youtube.com/watch?v=o_s6Q-teA6U&t=405s" ,
                         height="250px" , width="auto",
                         margin=Tamaños.MARGIN_PEQUEÑO.value,
                         align="center"
                         ),
        ),
        justify="center",
        bg = Colores.PRINCIPAL.value,
        min_width = "99vw",
        padding_y= Tamaños.PADDING.value
    )