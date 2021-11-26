from xmlrpc import client

url = 'https://kelsinglobal-technical-dev-3684264.dev.odoo.com'
db = 'kelsinglobal-technical-dev-3684264'
username = 'cmunoz@kelsinglobal.com'
password = 'Camuz$2018'


common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())


uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'academy.session','check_access_rights',
                                ['write'], {'raise_exception' : False})
print(model_access)

courses = models.execute_kw(db, uid, password,
                            'academy.course','search_read',
                            [[['level', 'in', ['intermediate','begginer']]]])
print(courses)


course = models.execute_kw(db, uid, password,
                           'academy.course','search',
                           [[['name', '=', 'Website 500']]])
print(course)


session_fields = models.execute_kw(db, uid, password,
                                   'academy.session','fields_get',
                                   [],{'attributes': ['string', 'type', 'required']})
print(session_fields)


new_session = models.execute_kw(db, uid, password,
                                'academy.session','create',
                                [
                                    {
                                        'course_id' : course[0],
                                        'duration' : 5,
                                    }
                                ]
                               )
print(new_session)  
