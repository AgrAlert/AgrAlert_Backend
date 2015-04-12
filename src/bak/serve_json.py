from bottle import route, run
import time

@route('/api/agralert') 
def get_status():
	return {'status': 'online', 'servertime': time.time()}
@route('/api/agralert/alerts')
def get_alerts():
	return {'empty':'True'}


if __name__ == '__main__':
	run(host='0.0.0.0', port=8080)
	

