from chalice import Chalice

app = Chalice(app_name='src')


@app.route('/')
def index():
    print("TESTE DEBUG! 123123123")
    return {'hello': 'world123'}