version: '3'
services:
  laradock:
    image: laradock
    build: 
      context: {location}
      dockerfile: {location}/docker/Dockerfile
    container_name: laradock
    ports:
      {ports}
    volumes:
      {volumes}
    privileged: true

