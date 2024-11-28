import reflex as rx

from dager_droger.styles import Colores, Tamaños


def iconos(nombre : str, redirección: str) -> rx.Component:
    return rx.link(
            rx.icon(
            tag = nombre,
            margin_y=Tamaños.MARGIN_PEQUEÑO.value,
            color=Colores.TERCIARIO.value,
            height="35px",
        ),
        href=redirección,
        is_external=True
    )

def navbar() -> rx.Component:
    return rx.box(
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    margin= Tamaños.MARGIN_PEQUEÑO.value,
                    height="35px",
                    width = "150px",

                ),
                rx.separator(),
                rx.box(
                    rx.hstack(
                        iconos("mail" , "https://es.wikipedia.org/wiki/Pepinillo"),
                        rx.text(
                            "Guacho_paja_96@hotmail.com",
                            margin_y = Tamaños.MARGIN_PEQUEÑO.value,
                            font_family = "Permanent Marker",
                            align="center",
                            color=Colores.TERCIARIO.value
                        ),
                        iconos("youtube" , "https://www.youtube.com/@DotDager"),
                        iconos("github" , "https://github.com/MarianoVilla"),
                        iconos("instagram" ,"https://instagram.com/dager.32"),
                        iconos("twitch" , "https://twitch.tv/dagerxiv")
                    ),
                    margin_x=Tamaños.MARGIN_PEQUEÑO.value
                )
            ),
        width= "100%",
        height = "50px",
        bg= Colores.PRINCIPAL.value,
        z_indez = 5
    )