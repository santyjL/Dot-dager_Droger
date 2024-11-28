import reflex as rx

config = rx.Config(
    app_name="dager_droger",
    frontend_port=3000,
    # Sobrescribir estilos globales
    template={
        "head": """
        <style>
            body {
                cursor: pointer;
            }
        </style>
        """
    }
)
