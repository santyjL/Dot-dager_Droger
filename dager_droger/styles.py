from enum import Enum

fonts = {
    "https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap",
    "https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&display=swap"
}

style = {
    "font_family" : "Permanent Marker, MerriWeather"
}
class Tamaños (Enum):
    MARGIN_PEQUEÑO = "0.5em",
    MARGIN_MEDIANO = "1em",
    MARGIN_GRANDE = "1.5em"

    PADDING = "0.3em",

    BORDER_RADIUS = "1.5em"
    BORDER_RADIUS_GRANDE = "50em"
    BORDER = "solid #FFFFFF"

class Colores(Enum):
    PRINCIPAL = "#ff5500"
    TERCIARIO = "#FFFFFF"
    BG = "000000"

    NEON_PRINCIPAL = "#FFFFFF 5px 5px 5px"
    NEON_SECUNDARIO = "#3206e7 5px 5px 5px"
    NEON_TERCIARIO = "#FFFFFF 5px 5px 5px"

    TEXTO = "#FFFFFF"
    TEXTO2 = "#000000"
    TITULO = "#FFFFFF"
    TITULO2 = "#000000"

_hover_generico={
    "transform": "scale(1.05)",
    "transition": "all 0.5s ease-in-out",
    "filter": "drop-shadow(2 2 30px #ff5346)",
    },