# ShopEase Product Service

An independent Product Management microservice built using FastAPI and Docker.

## Technology Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Docker
- In-memory data storage

## Features
- Create, retrieve, update and delete products.
- Retrieve all products.
- Filter products by category.
- Pagination using skip and limit.
- Pydantic request validation.
- HTTP exception handling.
- Automatic product ID generation.

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | /api/products/ | Create product |
| GET | /api/products/ | List products |
| GET | /api/products/{product_id} | Get product |
| PUT | /api/products/{product_id} | Update product |
| DELETE | /api/products/{product_id} | Delete product |

## Run Locally
Install dependencies:
```bash
pip install -r requirements.txt
```

Start the application:
```bash
uvicorn app.main:app --reload --port 8003
```

## Docker Deployment
Build image:
```bash
docker build -t shopease-product-service .
```

Run container:
```bash
docker run -d --name shopease-product-container -p 8003:8003 shopease-product-service
```

Check container:
```bash
docker ps
```

View logs:
```bash
docker logs shopease-product-container
```

## Documentation
Swagger UI: http://localhost:8003/docs

## Data Storage
This service uses temporary in-memory storage. Product data is cleared when the application restarts.

## Author
ShopEase Product Service Project
