import reflex as rx

from dager_droger.styles import Colores, Tamaños


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="4",font_family="MerriWeather" , color= Colores.TEXTO.value), href=href, is_external=True)


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            floating_text("Falopa"),
            size="7", weight="bold", as_="h3"
        ),
        footer_item("Psicopata en potencia", "https://es.wikihow.com/correr-como-Naruto"),
        footer_item("Las 3 virtudes de un programador", "https://pablasso.com/articles/las-3-grandes-virtudes-de-un-programador-pereza-impaciencia-y-arrogancia"),
        footer_item("Pepinos de 30cm o más", "https://www.amazon.com/-/es/mburring-Pepino-Ingl%C3%A9s/dp/B001PLET96/ref=zg_bs_g_6507077011_d_sccl_3/130-2599093-9110444?psc=1"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading(
            floating_text("C# God "),
            size="4", weight="bold", as_="h3"
        ),
        footer_item("Mi musica", "https://open.spotify.com/intl-es/artist/6bkClBMJd4qKxJp0J5vHsz?si=UqjJfsoeRnmwZBSM-9edhg&nd=1&dlsi=d76c3a7159424316"),
        footer_item("Que llegue hasta el fondo ", "https://es.wikipedia.org/wiki/Javier_Milei"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon , color=Colores.PRINCIPAL.value , margin_y=Tamaños.MARGIN_PEQUEÑO.value), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "https://instagram.com/dager.32"),
        social_link("music-4", "https://open.spotify.com/intl-es/artist/6bkClBMJd4qKxJp0J5vHsz?si=mbfNHqvBT9SKSQ-ZNhXHJg&nd=1"),
        social_link("youtube", "https://www.youtube.com/@DotDager"),
        social_link("github","https://github.com/MarianoVilla"),
        social_link("twitch" , "https://twitch.tv/dagerxiv"),
        spacing="3",
        justify="end",
        width="100%",
    )


def floating_text(content: str) -> rx.Component:
    """Creates floating text with a perpetual vertical movement."""
    return rx.text(
        content,
        size="5",
        weight="bold",
        font_family="Permanent Marker",
        animation="float 3s ease-in-out infinite",
        style={
            "@keyframes float": {
                "0%": {"transform": "translateY(0)"},
                "50%": {"transform": "translateY(-10px)"},
                "100%": {"transform": "translateY(0)"},
            }
        },
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="/logo.png",
                            width="7em",
                            height="auto",
                            border_radius="10%",
                        ),
                        align_items="center",
                    ),
                    floating_text("© 2024 Dot-Dager - Droger, Inc"),
                    spacing="2",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    spacing="3",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        justify="center",
        width="99%",
        margin_x=Tamaños.MARGIN_PEQUEÑO.value
    )
