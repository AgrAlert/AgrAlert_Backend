import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def sql_2_json():
	retLst = []
	db = sqlite3.connect('agralert.db')
	db.row_factory = dict_factory
	c = db.cursor()
	c.execute("SELECT * FROM agr")
	data = c.fetchall()
	result = json.dumps(data)
	for e in json.loads(result):
		e['options']={}
#		e['options'].append({"animation":2, "disableAutoPan": True})
		e['options'].update({'animation':2})
		e['options'].update({'disableAutoPan':True})
		retLst.append(e)
		
	return json.dumps(retLst)

