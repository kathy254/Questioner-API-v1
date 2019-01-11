from app import create_app

app = create_app('development')

@app.route('/')
def index():
    return "Welcome to Questioner."

if __name__ == "__main__":
    app.run(debug=True)