# 3D Rotation Matrix Visualization

A simple Python project that demonstrates how a 3D rotation matrix can rotate multiple points in 3D space.

## What this project does

The project:

1. Generates 100 random 3D points.
2. Generates three random rotation angles.
3. Creates three rotation matrices:
   - Rotation around X-axis
   - Rotation around Y-axis
   - Rotation around Z-axis
4. Combines them into one rotation matrix.
5. Rotates all 100 points.
6. Visualizes the points before and after rotation.
7. Verifies that rotation preserves the distance of each point from the origin.

## Main Formula

The combined rotation matrix is:

R = Rz @ Ry @ Rx

The rotated points are calculated using:

B = (R @ A.T).T

## Technologies

- Python
- NumPy
- Matplotlib

## Installation

```bash
pip install -r requirements.txt