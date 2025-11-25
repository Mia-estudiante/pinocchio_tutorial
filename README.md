# 📘 Pinocchio Tutorial Repository

This repository provides a structured set of tutorials for learning and applying the **Pinocchio** rigid-body dynamics library.  
It includes lecture slides, example codes and YouTube links covering robot dynamics, collision detection, and simulation.

---

## 🎥 Lecture Videos (YouTube)


- **Lecture 1:** Introduction  
- **Lecture 2:** Pinocchio examples Walkthrough  
- **Lecture 3:** Supaero2025 Walkthrough  

[Playlist of 1.1, 2.3, 2.4, 3.3, 3.4, 3.5](https://youtube.com/playlist?list=PL5i0ThRFrlDXmFiudX2GwZLCyZ3KLb6uL&si=Ne1lANIXQkPWy95v)  
[Playlist of 1.2, 2.1, 2.2, 3.1, 3.2](https://www.youtube.com/playlist?list=PLjhswBSqp70Fyc8-ZRRJP7SNtRlcAInCa)  

---

## 📚 Overview

This tutorial series is designed to help learners understand:

- How robot configurations and velocities are represented in Pinocchio  
- How collision detection works using geometry models  
- How to visualize robots using Meshcat/Gepetto  
- How to compute robot dynamics (RNEA, ABA)  
- How to run simulations and apply simple control laws
- How to optimize the trajectory using Crocoddyl  
<p align="left">
  <img src="https://github.com/user-attachments/assets/03b812a7-7134-40d9-bee5-cd066b6a229e" width="45%"> 
  <img src="https://github.com/user-attachments/assets/52b4892e-9a43-4053-97c9-23d873b4eff7" width="45%">
</p>


## 📂 Repository Structure
```
├── slides/
│   ├── Lecture1. Pinocchio Introduction.pdf
│   ├── Lecture2. Pinocchio Examples.pdf
│   └── Lecture3. Pinocchio Tutorials.pdf
├── double_pendulum/urdf/
│   └── double_pendulum_point_mass.urdf
├── examples/
│   ├── meshcat-viewer.py (go2)
│   ├── build-reduced-model.py
│   ├── geometry-models.py
│   ├── overview-simple.py
│   ├── overview-urdf.py
│   └── kinematics-derivatives.py
├── 2_Pinocchio_examples/
│   ├── check_collision.ipynb
│   └── model_and_data.ipynb
├── 3_Pinocchio_tutorials/
│   ├── 1_geometry/
│   │   └── geo.ipynb
│   ├── 2_kinematics/
│   │   ├── ik.ipynb
│   │   └── tiago_loader.py
│   ├── 3_dynamics/
│   │   ├── inverse_dynamics_pm.py
│   │   └── forward_dynamics_aba.py 
│   ├── 4_optcontrol/
│   │   └── panda_reaching_sequence_of_targets.ipynb
└── README.md  
```


---
## 🧠 Tutorial Content

### Lecture 1 — Introduction & Motivation
- What the Pinocchio library is  
- How to install and set up the environment  
- Main features of Pinocchio  

---

### Lecture 2 — Pinocchio Examples
- Loading a robot model  
- Simulating a robot model  
- Computing analytical derivatives of rigid-body dynamics algorithms  
- Displaying models using Meshcat/Gepetto  
- Collision checking  

---

### Lecture 3 — Pinocchio Tutorials (Supaero2025)
- Forward geometry  
- Inverse geometry  
- Inverse kinematics (including Jacobians)  
- Dynamics
- Optimal control  
  
## 🔧 Installation

Highly recommended to use virtual environment  
Follow the setup of [Gepetto/supaero2025](https://github.com/Gepetto/supaero2025?tab=readme-ov-file#set-up)  

## ⚙️ Execution

Once you placed the codes into the folders belong, (or export the model dir path correctly,)  
you can execute the example code by:
```
home:~/pinocchio/examples$ python inverse_dynamics_pm.py
nq = 2 nv = 2
Joint torques: [-24.85364489  -8.61740833]
  
home:~/pinocchio/examples$ python forward_dynamics_aba.py
Joint accelerations: [-3.76557097e-09  1.00000001e+00]
```
---

## 🔗 External References
### 📌 Pinocchio

GitHub: https://github.com/stack-of-tasks/pinocchio

Docs: https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/devel/doxygen-html

### 📌 Supaero 2025 Robotics Course

GitHub: https://github.com/Gepetto/supaero2025
