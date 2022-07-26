from website import create_app #website becomes a package since it is in __init__.copy()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)