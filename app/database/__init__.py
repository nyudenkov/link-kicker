from app import config

TORTOISE_ORM = {
    "connections": {"default": config.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
