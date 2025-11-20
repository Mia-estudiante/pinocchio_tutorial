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

print("nq =", model.nq, "nv =", model.nv)

q = np.array([0.5, -0.3])
v = np.array([0.1, 0.2])
a = np.array([0.0, 1.0])

tau = pin.rnea(model, data, q, v, a)


# Print out to the vector of joint torques (in N.m)
print("Joint torques: " + str(tau))
