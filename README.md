# Module3 Project Gamma

## About our Project

Our project is aimed towards small to medium sized restaurant owners looking for a software solution to manage essential portions of their business. Our app provides features that would be of interest to business owners who want to create an online presence.

## Running the project locally

1. Fork this project (https://gitlab.com/backofthehouse/gastronomical-gems).

2. Clone the repository to your local machine.

3. Change directory to the new project directory.

4. Install [Docker](https://www.docker.com/products/docker-desktop/).

5. Start Docker Desktop.

6. In terminal, run these commands:

```
docker volume create gastroids2

docker compose build

docker compose up
```
If you have a computer with [Apple silicon](https://support.apple.com/en-us/HT211814), use these commands:
```
docker volume create gastroids2

DOCKER_DEFAULT_PLATFORM=linux/amd64 docker compose build

docker compose up
```

7. Visit [http://localhost:3000](http://localhost:3000) in your browser.

Wire-Frames: https://excalidraw.com/#room=ae01c103655b963a3799,6v_wKfT6C2fzkKNNqbYXkQ
FastAPI: https://mar-2-pt-fastrapi.mod3projects.com/docs

## Deliverables

- [Wire-Frame](docs/wireframe_design.md)

- [Deployed Project](https://backofthehouse.gitlab.io/gastronomical-gems)

- [OpenAPI Endpoints](https://mar-2-pt-fastrapi.mod3projects.com/docs#/)

- [Gitlab Issue Board](https://gitlab.com/backofthehouse/gastronomical-gems/-/issues)

- Team Journals:
  - [Alec](journals/alec_weinstein.MD)
  - [Ben](journals/Benjamin_Ostler.MD)
  - [Ray](journals/Raymond_quach.md)
  - [Kenny](journals/kenny_phung.md)
  - [Ed](journals/ed_lee.md)
