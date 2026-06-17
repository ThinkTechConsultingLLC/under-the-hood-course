# Capstone starter — package the tiny model so it runs the SAME everywhere (M10).
# Build:  docker build -t tiny-model .
# Run:    docker run --rm tiny-model
FROM python:3.12-slim
WORKDIR /app
COPY . .
# No external packages to install — this toy uses only the standard library.
CMD ["python", "app.py"]
