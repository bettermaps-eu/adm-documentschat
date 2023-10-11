def get_authenticated_user_details(request_headers):
    user_object = {}

    ## Comprueba las cabeceras en busca de la clave específica de Google
    if "X-Google-Client-Principal-Id" not in request_headers:
        ## Si no se encuentra, puedes manejarlo como desees, por ejemplo, regresar un usuario predeterminado.
        # from . import sample_user
        # raw_user_object = sample_user.sample_user
        return None
    else:
        ## Si se encuentra, obtén los detalles del usuario desde las cabeceras de Google
        raw_user_object = {k: v for k, v in request_headers.items()}

    user_object['user_principal_id'] = raw_user_object['X-Google-Client-Principal-Id']
    user_object['user_name'] = raw_user_object['X-Google-Client-Principal-Name']
    user_object['auth_provider'] = 'Google'  # Puedes establecer el proveedor como "Google".
    user_object['auth_token'] = raw_user_object['X-Google-Token']  # Ajusta esto según las cabeceras de Google.
    user_object['client_principal_b64'] = raw_user_object['X-Google-Client-Principal']  # Ajusta esto según las cabeceras de Google.
    user_object['google_id_token'] = raw_user_object["X-Google-ID-Token"]  # Ajusta esto según las cabeceras de Google.

    return user_object
