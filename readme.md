![OS](https://img.shields.io/badge/OS-Linux-red?style=flat&logo=linux)
[![Python Version](https://img.shields.io/badge/Made%20with-Python%203.10-1f425f.svg?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-available-green.svg?style=flat&logo=docker)](https://github.com/emalderson/ThePhish/tree/master/docker)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/IftachNaftalyAB/carla_for_noobs)

# General Information

This repository aims to help setting up CARLA simulator, and show simple example of the Python API usage.

## CI

![example workflow](https://github.com/IftachNaftalyAB/carla_for_noobs/actions/workflows/semantic_release.yml/badge.svg)

# Prerequisites

1. [Install Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
2. Follow [Linux Post-Install Steps](https://docs.docker.com/engine/install/linux-postinstall/) for Docker Engine.
3. Install [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

# Install

1. Clone the repo:

        git clone git@github.com:IftachNaftalyAB/carla_for_noobs.git

2. Open the repository with VSCode and then [`reopen in container`](https://code.visualstudio.com/docs/devcontainers/containers).

**Note**: The [Dockerfile](./.devcontainer/Dockerfile) and the [devcontainer.json](./.devcontainer/devcontainer.json) will account for all the necessary installation and further setup.


# Run CARLA server

## Running the server (NOT FROM THE DEVCONTAINER):

Run the CARLA server with the [run_server.sh](./run_server.sh) script. 

**IMPORTANT**: It won't run from inside the container, run it from PC-terminal.

