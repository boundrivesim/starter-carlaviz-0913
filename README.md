# Carla Starter Project for version 0.9.13

This project contains a multi-container Carla project template for educational purposes.


## Setup the environment

- Ubuntu 20.04 environment (Ubuntu on WSL may work, not recommended)
- Docker (first [install Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) and then follow [Docker post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/))
- Docker Compose ([install docker-compose](https://docs.docker.com/compose/install/))
- Python 3.8 (comes by default in Ubuntu 20.04)
- Install and upgrade `pip` to the latest version 
- Install `carla` package using `pip install carla==0.9.13`

## Quickstart

Once your environment set up, start Carla and Carlaviz server from the project directory using

```
docker-compose --profile carlaviz up -d 
```

Then visit the address `localhost:8080` in your browser to see a web-based visualization of the Carla simulation, which uses the default map. You can find an example client script in the project directory and run it using 

```
python client/run.py
```

and close servers once done using

```
docker-compose down
```

## Changing the map before the simulation

The `carlaviz` container does not support change of maps at runtime (See [the related issue](https://github.com/mjxu96/carlaviz/issues/19)). Follow the steps to change the map in your simulation.

```
docker-compose up -d
python utils/config.py --map <CARLA_MAPNAME>
docker-compose --profile carlaviz up -d 
python client/run.py
```
where `<CARLA_MAPNAME>` denotes a Carla map name `Town01`, ..., `Town07`, `Town10`.

Don't forget to visit `localhost:8080` to see the visualization.