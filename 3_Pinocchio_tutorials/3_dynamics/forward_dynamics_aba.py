# Copyright 2023 Inria
# SPDX-License-Identifier: BSD-2-Clause


"""
In this short script, we show how to compute inverse dynamics (RNEA), i.e. the
vector of joint torques corresponding to a given motion.
"""

from pathlib import Path

import numpy as np
import pinocchio as pin

# Load the model from a URDF file
# Change to your own URDF file here, or give a path as command-line argument
pinocchio_model_dir = Path(__file__).parent.parent / "models/"
model_path = pinocchio_model_dir / "example-robot-data/robots"
mesh_dir = pinocchio_model_dir
urdf_filename = "double_pendulum_point_mass.urdf"
urdf_model_path = model_path / "double_pendulum_description/urdf/" / urdf_filename
model, _, _ = pin.buildModelsFromUrdf(urdf_model_path, package_dirs=mesh_dir)

data = model.createData()

q = np.array([0.5, -0.3])
v = np.array([0.1, 0.2])
tau=np.array([-24.85364489,  -8.61740833])

ddotq = pin.aba(model, data, q, v, tau)

# Print out to the vector of joint torques (in N.m)
print("Joint accelerations: " + str(ddotq))
