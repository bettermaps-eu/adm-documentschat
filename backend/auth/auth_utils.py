def get_authenticated_user_details(request_headers):
    user_object = {}

    # Verificar si las cabeceras contienen la información de autenticación de Google
    if "X-Goog-Authenticated-User-Id" not in request_headers:
        # Si no se encuentra la información de Google, puedes manejar esto según tus necesidades.
        # Puedes lanzar una excepción, redirigir al usuario a la página de inicio de sesión de Google, etc.
        raise Exception("No se encontró la información de autenticación de Google en las cabeceras.")

    # Obtener los datos del usuario de Google a partir de las cabeceras
    user_object['user_principal_id'] = request_headers['X-Goog-Authenticated-User-Id']
    user_object['user_name'] = request_headers.get('X-Goog-Authenticated-User-Name', 'Nombre de usuario desconocido')
    user_object['auth_provider'] = 'Google'  # Puedes establecer el proveedor de autenticación como Google
    user_object['auth_token'] = request_headers.get('X-Goog-Id-Token', 'Token de autenticación desconocido')
    user_object['client_principal_b64'] = request_headers.get('X-Goog-Client-Principal', 'Cliente principal desconocido')
    user_object['google_id_token'] = request_headers.get('X-Goog-Id-Token', 'Token de ID de Google desconocido')

    return user_object
