from typing import Dict

def get_endpoints(openapi_data: Dict) -> Dict:
    endpoints = []
    for path, methods in openapi_data.get('paths', {}).items():
        for method, details in methods.items():
            endpoints.append({
                "endpoint": path,
                "method": method.upper()
            })
    return endpoints


def get_endpoint_definition(openapi_data: Dict, method: str, endpoint: str) -> Dict:
    if endpoint not in openapi_data.get("paths", {}):
        raise ValueError(f"Endpoint '{endpoint}' not found in the OpenAPI file.")
    if method.lower() not in openapi_data["paths"][endpoint]:
        raise ValueError(f"Method '{method}' not found for endpoint '{endpoint}'.")

    endpoint_definition = openapi_data["paths"][endpoint][method.lower()]
    
    components = openapi_data.get("components", {}).get("schemas", {})
    collected_schemas = {}

    def collect_references(schema):
        """Recursively collect all schemas referenced by the given schema."""
        if not isinstance(schema, dict):
            return
        if "$ref" in schema:
            ref_path = schema["$ref"]
            if ref_path.startswith("#/components/schemas/"):
                schema_name = ref_path.split("/")[-1]
                if schema_name in components and schema_name not in collected_schemas:
                    collected_schemas[schema_name] = components[schema_name]
                    collect_references(components[schema_name])
        else:
            for value in schema.values():
                if isinstance(value, dict):
                    collect_references(value)
                elif isinstance(value, list):
                    for item in value:
                        collect_references(item)

    if "requestBody" in endpoint_definition:
        content = endpoint_definition["requestBody"].get("content", {})
        for media_type in content.values():
            schema = media_type.get("schema", {})
            collect_references(schema)

    if "responses" in endpoint_definition:
        for response in endpoint_definition["responses"].values():
            content = response.get("content", {})
            for media_type in content.values():
                schema = media_type.get("schema", {})
                collect_references(schema)

    result = {
        "endpoint": endpoint,
        "method": method.upper(),
        "definition": endpoint_definition,
        "schemas": collected_schemas
    }

    return result
