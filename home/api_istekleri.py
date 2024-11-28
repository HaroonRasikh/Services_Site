import httpx
import json

SIGN_IN_API_ENPOINT = 'https://api.uimconsulting.com/az/v2/auths'
def try_signing_in(email, password, request):
    status = {'message': ''}

    response = httpx.post(SIGN_IN_API_ENPOINT, data= {
        'username': email,
        'password': password
    })
    
    if response.status_code == 200:
        json_response = response.json()
        
        if 'message' in json_response:
            status['message'] = json_response['message']
        if 'data' in json_response:
            status['access_token'] = json_response['data']['token']
            request.session['access_token'] = json_response['data']['token']
        
    return status
 
SIGN_UP_API_ENPOINT = 'https://api.uimconsulting.com/az/v2/users'
def try_signing_up(email, phone, password,fullname,idcard):
    status = {'message': ''}

    response = httpx.post(SIGN_UP_API_ENPOINT, data= {
        'fullname':fullname,
        'email': email,
        'phone':phone,
        'password': password,
        'idcard':idcard,
        'speciality':6,
        'type':4,
        'workplace':7
    })

    
    # if response.status_code == 200:
    json_response = response.json()
    print(json_response)
    if 'message' in json_response:
        if type(json_response['message']) == list:
            status['message'] = json_response['message'][0]
        else:
            status['message'] = json_response['message']
    if 'success' in json_response and json_response['success'] == 'success':
        status['success'] = True
        
    #if 'data' in json_response:
     #   status['access_token'] = json_response['data']['token']
  #  print('Not 200: ', response.json())
    return status

def getUserDetails(request):  
    username = request.session['username']
    password = request.session['password']
    sign_in_response = try_signing_in(username, password, request)

    profildetail_API = 'https://api.uimconsulting.com/en/v2/users/profile?token={}'.format(sign_in_response['access_token'])
    status = {'message': ''}
    response = httpx.get(profildetail_API)
    if response.status_code == 200:
        json_response = json.load(response)
        if json_response['status'] == 'success':
            status['success'] = True
            status['currentUser'] = json_response['payload']
    return status

def update_request(formData, request):
    username = request.session['username']
    password = request.session['password']
    sign_in_response = try_signing_in(username, password, request)

    profildetail_API = 'https://api.uimconsulting.com/en/v2/users/updateprofile?token={}'.format(sign_in_response['access_token'])
    status = {'message': ''}
    response = httpx.post(profildetail_API,data=formData)
    
    
    if response.status_code == 200:
        json_response = json.load(response)
        if 'success' in json_response:
            status['success'] = True
        else:
            status['message'] = json_response['message']
    

    return status

def change_password_request(current_password, new_password, request):
    status = {'message' : ''}
    username = request.session['username']
    password = request.session['password']
    sign_in_response = try_signing_in(username, password, request)
    if 'access_token' not in sign_in_response:
        status['message'] = 'Retry later'
        return status

    data = {
        'oldpassword': current_password,
        'password': new_password,
    }   
    res = httpx.post('https://api.uimconsulting.com/en/v2/users/passwordchange?token={}'.format(sign_in_response['access_token']), data=data)
    response = json.load(res)
    
    if 'status' in response:
        if response['status'] == 'success':
            status['success'] = True
        else:
            status['message'] = 'Failed to change your password, retry later!'
    else:
        status['message'] = 'Retry later, please'
    return status

   
# import httpx
# import json

# def update_profile(access_token, profile_data):
#     url = 'https://api.uimconsulting.com/en/v2/users/updateprofile?token={}'.format(access_token)
#     response = httpx.post(url, data=json.dumps(profile_data), headers={'Content-Type': 'application/json'})
#     response_data = response.json()
#     if response_data.get('success'):
#         return True
#     else:
#         return False