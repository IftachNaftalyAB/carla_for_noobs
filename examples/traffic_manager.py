# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time

sys.path.append("/workspaces/carla/carla/PythonAPI/carla")
from agents.navigation.basic_agent import BasicAgent
from agents.navigation.behavior_agent import BehaviorAgent


def main():
    actor_list = []


    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        world = client.get_world()

        blueprint_library = world.get_blueprint_library()
        bp = random.choice(blueprint_library.filter('vehicle.dodge.charger_2020'))

        transform = world.get_map().get_spawn_points()[10]
        
        # Set the spectator behind the vehicleewwww
        spectator = world.get_spectator()
        spec_transform = carla.Transform(
            location = carla.Location(x = transform.location.x - 10, y = transform.location.y, z = transform.location.z + 5),
            rotation = transform.rotation
        )
        
        spectator.set_transform(spec_transform)

        # So let's tell the world to spawn the vehicle.
        vehicle = world.spawn_actor(bp, transform)
        
        actor_list.append(vehicle)
        print('created %s' % vehicle.type_id)

        # Let's put the vehicle to drive around.

        agent = BehaviorAgent(vehicle, behavior='aggressive')

        destination = random.choice(world.get_map().get_spawn_points()).location
        agent.set_destination(destination)

        while True:
            if agent.done():
                print("The target has been reached, stopping the simulation")
                break

            vehicle.apply_control(agent.run_step())

    finally:

        print('destroying actors')
        client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])
        print('done.')


if __name__ == '__main__':

    main()