# Recommender

Post recommendation service for Danbooru.

# Quickstart

    # Install dependency manager (https://poetry.eustace.io)
    python3 -m pip install --user poetry

    # Install dependencies
    python3 -m poetry install

    # Edit config file
    cp env.sample .env
    vim .env

    # Train model
    python3 -m poetry run bin/train

    # Run webserver (development)
    python3 -m poetry run flask run
    python3 -m poetry run gunicorn wsgi

    # Get recommendations for user #1
    curl http://localhost:5000/recommend/1

    # Get recommendations for post #1
    curl http://localhost:5000/similar/1
