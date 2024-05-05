docker run \
    --privileged \
    --device=/dev/dri:/dev/dri \
    --network host \
    --gpus all \
    -e DISPLAY=${DISPLAY} \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -e SDL_VIDEODRIVER=x11 \
    -e QT_X11_NO_MITSHM=1 \
    -e NVIDIA_DRIVER_CAPABILITIES=all \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    carlasim/carla:0.9.15 \
    /bin/bash ./CarlaUE4.sh -prefernvidia
    
