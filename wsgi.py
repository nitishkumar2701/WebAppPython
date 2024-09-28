from app import create_app

# Create the app instance
app = create_app()

# If running directly, use the development server (optional)
if __name__ == "__main__":
    app.run(debug=True)
