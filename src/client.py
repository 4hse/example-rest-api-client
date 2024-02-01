import requests
import uuid 

#current user access token
authentication = {'access-token': 'replace_with_yours'}

#retrieve the list of offices that current user is able to access
params = {'limit': 10, 'sort': '-name'}
params.update(authentication)
r = requests.get('https://service.4hse.com/office/index', params=params)
print('#### INDEX ####')
print(r.text)
print(r)

#create a new office
#to create a new office we need to specify the project_id of the office
#in this example we retrieve it from the first office of the previous call
project_id = r.json().get('data')[0].get('project_id')

#also wee need a unique id for new office
office_id = uuid.uuid1()

payload = {'office_id': office_id, 'name': 'My new office', 'project_id': project_id}
r = requests.post('https://service.4hse.com/office/create', data=payload, params=authentication)
print('#### CREATE ####')
print(r.text)
print(r)

#retrieve the newly created office
params = {'id': office_id}
params.update(authentication)
r = requests.get('https://service.4hse.com/office/view', params=params)
print('#### VIEW ####')
print(r.text)
print(r)
new_office = r.json().get('data')

#updated office with new name
params = {'id': office_id}
params.update(authentication)
payload = new_office
payload.update({'name': 'new name for my office'})
r = requests.put('https://service.4hse.com/office/update', data=payload, params=params)
print('#### UPDATE ####')
print(r.text)
print(r)

#delete office
params = {'id': office_id, 'force': 'true'}
params.update(authentication)
r = requests.delete('https://service.4hse.com/office/delete', params=params)
print('#### DELETE ####')
print(r)