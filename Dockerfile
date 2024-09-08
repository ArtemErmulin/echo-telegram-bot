FROM python:3.11-slim

WORKDIR /app
COPY . ./

# curl for healthcheck
RUN apt update && apt install -y curl
RUN pip install --no-cache-dir uv
RUN uv sync

EXPOSE 8443

CMD ["uv", "run", "run.py"]
