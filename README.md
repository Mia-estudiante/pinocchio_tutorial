# 📘 Pinocchio Tutorial Repository

This repository provides a structured set of tutorials for learning and applying the **Pinocchio** rigid-body dynamics library.  
It includes lecture slides, example codes and YouTube links covering robot dynamics, collision detection, and simulation.

---

## 🎥 Lecture Videos (YouTube)

*https://youtube.com/playlist?list=PL5i0ThRFrlDXmFiudX2GwZLCyZ3KLb6uL&si=Ne1lANIXQkPWy95v*

- **Lecture 1:** Introduction  
- **Lecture 2:** Pinocchio examples Walkthrough  
- **Lecture 3:** Supaero2025 Walkthrough  

---

## 📚 Overview

This tutorial series is designed to help learners understand:

- How robot configurations and velocities are represented in Pinocchio  
- How to compute robot dynamics (RNEA, ABA)  
- How collision detection works using geometry models  
- How to visualize robots using Meshcat/Gepetto  
- How to run simulations and apply simple control laws  

---

# 📂 Repository Structure
.  
├── slides/  
│ ├── 01_Pinocchio_Introduction.pdf  
│ ├── 02_Pinocchio_Examples.pdf  
│ ├── 03_Supaero_Examples.pdf  
│  
├── urdf/  
│ ├── double_pendulum/  
│  
└── README.md  


---
# 🧠 Tutorial Content

## Lecture 1 — Introduction & Motivation
- What the Pinocchio library is  
- How to install and set up the environment  
- Main features of Pinocchio  

---

## Lecture 2 — Pinocchio Examples
- Loading a robot model  
- Simulating a robot model  
- Computing analytical derivatives of rigid-body dynamics algorithms  
- Displaying models using Meshcat/Gepetto  
- Collision checking  

---

## Lecture 3 — Pinocchio Tutorials (Supaero2025)
- Forward geometry  
- Inverse geometry  
- Inverse kinematics (including Jacobians)  
- Dynamics  
  
🔧 Installation

Install dependencies:
```
pip install pin
pip install meshcat
pip install numpy scipy
pip install jupyterlab
```

---

## 🔗 External References
### 📌 Pinocchio

GitHub: https://github.com/stack-of-tasks/pinocchio

Docs: https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/

### 📌 Supaero 2025 Robotics Course

GitHub: https://github.com/machines-in-motion/supaero2025
