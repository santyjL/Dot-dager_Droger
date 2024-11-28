"""
Hola X,

Estoy buscando una página de destino/portafolio limpio y simple creado
para mi marca personal, llamada "Dot Dager".

La página debe mostrar mi nombre, una foto de perfil (adjunta) y
dar a los visitantes una idea de mi personalidad; como un portafolio o una página de
presentación. Aquí hay un poco sobre mí: soy un creador de contenido que
ama la programación, los gatos, las guitarras, los pepinillos y la filosofía.

No tengo requisitos de diseño específicos más allá de mostrar mi nombre y
foto de perfil de manera destacada, pero me encantaría ver algo que se sienta
como "yo". Puedes ser creativo con la forma en que representas estos
intereses.

El sitio puede ser de una sola página, no requiere navegación ni funciones
complejas (como cargas de contenido).

Adjunto está mi foto de perfil, que uso en todas mis redes sociales. Aparte de esto, la marca y la paleta son de tu agrado.

Tengo un presupuesto alto y espero terminar esto en aproximadamente una semana.

¿Te interesaría ayudarme con esto?

Saludos, Mariano/Dot Dager.
"""
import reflex as rx

from dager_droger.components.about_me import about_me, about_me_image
from dager_droger.components.audio import un_programador_y_su_gato_pepino
from dager_droger.components.footer import footer
from dager_droger.components.grid import intereses
from dager_droger.components.navbar import navbar
from dager_droger.components.videos import videos_droger
from dager_droger.styles import Colores


def index() -> rx.Component:
    return rx.box(  # Usamos rx.box para aplicar estilos globales
        rx.vstack(
            navbar(),
            rx.center(
                rx.hstack(
                    about_me_image(),
                    about_me()
                ),
            ),
            rx.box(height="250px"),
            rx.center(
                rx.vstack(
                    rx.center(
                        rx.box(
                        rx.heading(
                                "Ven te voy a enseñar lo que me gusta",
                                font_family="Permanent Marker",
                                font_size="2em",
                                color=Colores.TITULO.value,
                                align="center",  # Aseguramos el centrado
                            ),
                        width="99vw"
                        )
                    )
                )
            ),
            rx.center(
                rx.vstack(
                    rx.center(
                        rx.box(
                            intereses(),
                            width="99vw"
                        )
                    )
                )
            ),
            rx.box(height="200px"),
             rx.center(
                rx.vstack(
                    rx.center(
                        rx.box(
                        rx.heading(
                                "Unos cuantos videos para que no te aburras",
                                font_family="Permanent Marker",
                                font_size="2em",
                                color=Colores.TITULO.value,
                                align="center",  # Aseguramos el centrado
                            ),
                        width="99vw"
                        )
                    )
                )
            ),
            rx.center(
                videos_droger(),
                margin_y="2em",
            ),
            rx.center(
                rx.vstack(
                    rx.center(
                        un_programador_y_su_gato_pepino(),
                    )
                ),
            ),
            rx.box(height="100px"),
            rx.divider(),

            footer(),
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_width="99vw",
        min_height="100vh",
    )


app = rx.App()
app.add_page(index)
