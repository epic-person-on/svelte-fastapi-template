FROM python:3.12
WORKDIR /usr/local/app

# Install uv & generate requirements.txt
RUN curl -LsSf https://astral.sh/uv/install.sh | shcurl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv export --no-hashes --format requirements-txt > requirements.txt

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . .
EXPOSE 8000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["fastapi", "run", "main.py"]