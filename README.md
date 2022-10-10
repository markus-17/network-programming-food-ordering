# Network Programming - Laboratory Work Nr.2 - Food Ordering

## How to run the project using Docker?

You may build each image separately and run the containers in the same Docker network, but I recommend using `docker compose`.

```yaml
version: '3'
services:
  kitchen_1:
    container_name: kitchen_1
    build: network-programming-kitchen/
    ports:
      - 3001:3001
    environment:
      - USING_DOCKER_COMPOSE=1
      - RESTAURANT_ID=1
    depends_on:
      food_ordering:
        condition: service_started

  kitchen_2:
    container_name: kitchen_2
    build: network-programming-kitchen/
    ports:
      - 3002:3002
    environment:
      - USING_DOCKER_COMPOSE=1
      - RESTAURANT_ID=2
    depends_on:
      food_ordering:
        condition: service_started

  food_ordering:
    container_name: food_ordering
    build: network-programming-food-ordering/
    ports:
      - 8000:8000

  client_service:
    container_name: client_service
    build: network-programming-client-service/
    depends_on:
      kitchen_1:
        condition: service_started
      kitchen_2:
        condition: service_started
```