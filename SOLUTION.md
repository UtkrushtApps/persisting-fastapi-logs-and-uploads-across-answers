# Solution Steps

1. Ensure the FastAPI app writes logs to `/app/logs` and saves uploaded files under `/app/uploads` (already set in `main.py`).

2. In the Dockerfile, use the `VOLUME ["/app/logs"]` instruction to declare `/app/logs` as a named Docker volume, ensuring that container restarts do not erase logs.

3. Leave `/app/uploads` as a normal directory in the image, so we can mount a host directory to it at container run time (as a bind mount).

4. Create a `requirements.txt` including `fastapi` and `uvicorn`.

5. Build the Docker image using `docker build -t fastapi-persistence .`.

6. Run the container with the following command to mount `/app/uploads` as a bind mount (host's `./host_uploads` directory) and let Docker handle `/app/logs` as a volume: 

  docker run -d --name fastapi-app -p 8000:8000 \
    -v fastapi_logs:/app/logs \
    -v $(pwd)/host_uploads:/app/uploads \
    fastapi-persistence

7. Upload files and write logs via the FastAPI endpoints to create persistent data.

8. Stop and remove the container: `docker stop fastapi-app && docker rm fastapi-app`.

9. Start a new container in the same way, reusing the host bind mount and named volume: you will find previously uploaded files under `./host_uploads` on your host, and logs remain intact.

10. Inspect the Docker named volume with `docker volume inspect fastapi_logs` to confirm it is attached to the new container.

11. Check the usage and data under `host_uploads` (on host) and logs (either in a new container or by attaching another temporary container to 'fastapi_logs').

12. The FastAPI app will continue working without changes, and persistent storage will be preserved across container lifecycles.

