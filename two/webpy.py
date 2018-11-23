import web
import json
render = web.template.render('tpl/')

db = []

json_names_file = open('names.json')
json_names_str = json_names_file.read()
json_names_data = json.loads(json_names_str)[0]
for n in json_names_data['names']:

db[0] = [{'name': 'Dima'}, {'name': 'Vova'}]




urls = ('/(.*)', 'index')
app = web.application(urls, globals())

class index:        

    def POST(self, url):
        name = 'Dima'
        i = web.input()
        db.append({'name': i['name']})
        #import pdb; pdb.set_trace()
        return render.index({'name': name,'db': db})
            
   
        
    def GET(self, name):
        name = 'Dima'
        return render.index({'name': name,'db': db})
        '''
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'
        '''

    def write_to_json(names):
        with open('names.json','w') as jf:
            jf_file = json.load('names.json')
            jf_target = jf_file[0]['names']
            name_list = json.dumps(names)
            jf_target.append(name_list)
            json.dump(jf_file, jf)


if __name__ == "__main__":
    app.run()
    
    
