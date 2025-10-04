from jsonschema import validate

from typing import Dict, Any

# Esquema para un "post"
post_schema: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"]
}

# Esquema para un "user"
user_schema: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "email": {"type": "string"},
    },
    "required": ["id", "email"]
}

# Función que valida una instancia contra un esquema
def assert_schema(instance: Dict[str, Any], schema: Dict[str, Any]) -> None:
    validate(instance=instance, schema=schema)
