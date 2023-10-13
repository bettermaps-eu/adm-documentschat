def get_authenticated_user_details(request_headers):
    user_object = {}

    ## check the headers for the Principal-Id (the guid of the signed in user)
    if "X-Ms-Client-Principal-Id" not in request_headers.keys():
        ## if it's not, assume we're in development mode and return a default user
        from . import sample_user
        raw_user_object = sample_user.sample_user
    else:
        ## if it is, get the user details from the EasyAuth headers
        raw_user_object = {k:v for k,v in request_headers.items()}

    user_object['user_principal_id'] = raw_user_object['X-Ms-Client-Principal-Id']
    user_object['user_name'] = raw_user_object['X-Ms-Client-Principal-Name']
    user_object['auth_provider'] = raw_user_object['X-Ms-Client-Principal-Idp']
    user_object['auth_token'] = 'tokenauth' #para q funcione con cualquier proveedor de identidad  #raw_user_object['X-Ms-Token-Google-Access-Token'] #google auth
    user_object['client_principal_b64'] = raw_user_object['X-Ms-Client-Principal']
    user_object['aad_id_token'] = 'aad_id_token' #para q funcione con cualquier proveedor de identidad  #raw_user_object["X-Ms-Token-Google-Id-Token"] #google auth

    return user_object

"""
def get_authenticated_user_details(request_headers):
    user_object = {}

    user_object['user_principal_id'] = '1a'
    user_object['user_name'] = 'username'
    user_object['auth_provider'] = 'googleProvider'
    user_object['auth_token'] = 123
    user_object['client_principal_b64'] = 'dXN1YXJpb2RlcHJldWJh'
    user_object['aad_id_token'] = 123

    return user_object
"""