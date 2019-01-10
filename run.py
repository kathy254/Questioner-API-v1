from app import create_app

app = create_app('development')

@app.route('/')
def index():
    return "<p>Find documentation at <a href="https://documenter.getpostman.com/view/5582682/RznFpxuQ">here</a><p>"

if __name__ == "__main__":
    app.run(debug=True)