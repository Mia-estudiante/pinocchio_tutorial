import numpy as np
import pinocchio as pin

# Create model and data
model = pin.buildSampleModelHumanoidRandom()
data = model.createData()

# Set bounds
model.lowerPositionLimit = -np.ones((model.nq, 1))
model.upperPositionLimit = np.ones((model.nq, 1))

q = pin.randomConfiguration(model)
v = np.random.rand(model.nv, 1)
a = np.random.rand(model.nv, 1)

# Compute derivatives
pin.computeForwardKinematicsDerivatives(model, data, q, v, a)

joint_name = "rleg6_joint"
joint_id = model.getJointId(joint_name)

# Velocity derivatives
dv_dq, dv_dv = pin.getJointVelocityDerivatives(
    model, data, joint_id, pin.ReferenceFrame.WORLD
)

# Acceleration derivatives
dv_dq2, da_dq, da_dv, da_da = pin.getJointAccelerationDerivatives(
    model, data, joint_id, pin.ReferenceFrame.WORLD
)

print("=== JOINT:", joint_name, "===")
print("model.nq:", model.nq, "model.nv:", model.nv)

print("\n--- Velocity Derivatives (WORLD frame) ---")
print("dv/dq shape:", dv_dq.shape)
print("dv/dv shape:", dv_dv.shape)
print("dv/dq (first 3 rows):\n", dv_dq[:3, :5])
print("dv/dv (first 3 rows):\n", dv_dv[:3, :5])

print("\n--- Acceleration Derivatives (WORLD frame) ---")
print("da/dq shape:", da_dq.shape)
print("da/dv shape:", da_dv.shape)
print("da/da shape:", da_da.shape)
print("da/dq (first 3 rows):\n", da_dq[:3, :5])
print("da/dv (first 3 rows):\n", da_dv[:3, :5])
