from app import create_app

app = create_app()


@app.route('/')
def index():
    return 'Index Page!'


@app.route('/health')
def health():
    return 'Health Check OK!!'
