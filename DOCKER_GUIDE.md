# Docker Development Guide

## Quick Start

### Using Docker Compose (Recommended)

**Run the analysis in Docker:**
```bash
docker-compose up
```

This will:
1. Build the image (first time only)
2. Start a container with live code volume mounts
3. Execute `python main.py`
4. Keep the container available for interactive use

**Run with interactive shell:**
```bash
docker-compose run --rm housing-analysis /bin/bash
```

Then you can run Python commands inside:
```bash
python main.py          # Run analysis
python -c "import pandas; print('OK')"  # Test imports
```

**Stop the container:**
```bash
docker-compose down
```

---

## Volume Mounts (Hot Reload)

Your `docker-compose.yml` has these volume configurations:

```yaml
volumes:
  - .:/app                    # Project folder synced live
  - ./outputs:/app/outputs    # Outputs folder accessible from host
  - /app/__pycache__          # Keep cache inside container
```

### How Live Code Updates Work:

1. **Edit a file in VSCode** (e.g., `src/visualization.py`)
2. **Save the file** (Ctrl+S)
3. **Changes instantly appear inside the running container** ✅
4. **Restart the container** to run with new code changes

Example:
```bash
# Terminal 1: Container running
$ docker-compose up

# Terminal 2: Edit your code in VSCode
# Then restart the container:
$ docker-compose down
$ docker-compose up

# Container now runs with your code changes!
```

---

## Common Commands

### Build only (without running)
```bash
docker-compose build
```

### Run and see live logs
```bash
docker-compose up --build
```

### Run in background
```bash
docker-compose up -d
```

### View logs (if running in background)
```bash
docker-compose logs -f housing-analysis
```

### Stop background container
```bash
docker-compose down
```

### Remove images and containers
```bash
docker-compose down -v
```

---

## Troubleshooting

### "Cannot connect to Docker daemon"
- Ensure Docker Desktop is running
- On Windows/Mac: Start Docker app
- On Linux: `sudo systemctl start docker`

### Volume mount not working
- Ensure paths are correct in `docker-compose.yml`
- Windows: File sharing must be enabled in Docker Desktop settings
  - Settings → Resources → File Sharing
  - Add your project folder path

### Changes not reflecting in container
- Save your file in VSCode
- Restart the container: `docker-compose restart housing-analysis`

### Permission denied errors
- On Linux: Add user to docker group
  ```bash
  sudo usermod -aG docker $USER
  ```

---

## Docker vs Local Development

| Aspect | Local | Docker |
|--------|-------|--------|
| **Setup** | Manual venv | Automated |
| **Python version** | System-dependent | Consistent |
| **Dependencies** | Local install | Isolated |
| **Team sharing** | Version mismatches | Same environment |
| **Production parity** | May differ | Same as production |
| **Learning curve** | None | Minimal |

---

## Environment Variables

Set in `docker-compose.yml`:

```yaml
environment:
  - PYTHONUNBUFFERED=1          # Real-time console output
  - PYTHONDONTWRITEBYTECODE=1    # Don't create .pyc files
```

To add more:
```yaml
environment:
  - MY_VAR=value
  - ANOTHER_VAR=another_value
```

---

## For CI/CD Integration

This Dockerfile is production-ready. Use in GitHub Actions, GitLab CI, etc:

```dockerfile
# Build
docker build -t uk-housing-price:latest .

# Run
docker run -v $(pwd)/outputs:/app/outputs uk-housing-price:latest
```

---

## Questions?

- Docker docs: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Python in Docker: https://docs.docker.com/language/python/
