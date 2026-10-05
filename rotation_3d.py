import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 3D Rotation Matrix Visualization
# ============================================================
# This project demonstrates how a 3D rotation matrix can be
# used to rotate 100 points in 3D space.
#
# The process:
# 1. Generate 100 random 3D points.
# 2. Generate 3 random rotation angles.
# 3. Build Rx, Ry, and Rz rotation matrices.
# 4. Combine them into one rotation matrix R.
# 5. Rotate all points using R.
# 6. Visualize the points before and after rotation.
# ============================================================


def gen_R_3d(p):
    """
    Generate a 3D rotation matrix from three angles.

    Parameters
    ----------
    p : numpy.ndarray
        A 1D array containing three rotation angles:
        [px, py, pz] in radians.

    Returns
    -------
    R : numpy.ndarray
        Combined 3D rotation matrix of shape (3, 3).
    """

    # Extract the three rotation angles
    px, py, pz = p

    # --------------------------------------------------------
    # Rotation around X-axis
    # --------------------------------------------------------
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(px), np.sin(px)],
        [0, -np.sin(px), np.cos(px)]
    ])

    # --------------------------------------------------------
    # Rotation around Y-axis
    # --------------------------------------------------------
    Ry = np.array([
        [np.cos(py), 0, -np.sin(py)],
        [0, 1, 0],
        [np.sin(py), 0, np.cos(py)]
    ])

    # --------------------------------------------------------
    # Rotation around Z-axis
    # --------------------------------------------------------
    Rz = np.array([
        [np.cos(pz), np.sin(pz), 0],
        [-np.sin(pz), np.cos(pz), 0],
        [0, 0, 1]
    ])

    # Combine the three rotations into one matrix
    # The rightmost matrix is applied first.
    R = Rz @ Ry @ Rx

    return R


def rotate_points(A, R):
    """
    Rotate a set of 3D points using a rotation matrix.

    Parameters
    ----------
    A : numpy.ndarray
        Matrix of points with shape (N, 3).

    R : numpy.ndarray
        Rotation matrix with shape (3, 3).

    Returns
    -------
    B : numpy.ndarray
        Rotated points with shape (N, 3).
    """

    # A has shape (N, 3)
    # Transpose -> (3, N)
    #
    # R has shape (3, 3)
    #
    # R @ A.T -> (3, N)
    #
    # Transpose again -> (N, 3)
    return (R @ A.T).T


def plot_points(ax, points, title):
    """
    Plot 3D points on a given axis.
    """

    ax.scatter(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        s=35
    )

    ax.set_title(title)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)


# ============================================================
# 1. Generate 100 random 3D points
# ============================================================

np.random.seed(42)

N_POINTS = 100

A = np.random.uniform(
    low=-1,
    high=1,
    size=(N_POINTS, 3)
)

print("Original points shape:")
print(A.shape)


# ============================================================
# 2. Generate three random rotation angles
# ============================================================

# random.rand(3) generates 3 random values between 0 and 1
#
# Multiplying by 2*pi converts them into angles between
# 0 and 2*pi radians (0 to 360 degrees).

p = 2 * np.pi * np.random.rand(3)

px, py, pz = p


print("\nRotation angles:")
print(f"px = {px:.4f} radians = {np.degrees(px):.2f} degrees")
print(f"py = {py:.4f} radians = {np.degrees(py):.2f} degrees")
print(f"pz = {pz:.4f} radians = {np.degrees(pz):.2f} degrees")


# ============================================================
# 3. Generate the combined 3D rotation matrix
# ============================================================

R = gen_R_3d(p)


print("\nCombined rotation matrix R:")
print(R)

print("\nRotation matrix shape:")
print(R.shape)


# ============================================================
# 4. Rotate all 100 points
# ============================================================

B = rotate_points(A, R)


print("\nRotated points shape:")
print(B.shape)


# Print a few points to compare
print("\nFirst 5 original points:")
print(A[:5])

print("\nFirst 5 rotated points:")
print(B[:5])


# ============================================================
# 5. Check that rotation preserves the distance from origin
# ============================================================
# A correct rotation changes direction but keeps the vector length.

original_lengths = np.linalg.norm(A, axis=1)
rotated_lengths = np.linalg.norm(B, axis=1)

max_difference = np.max(
    np.abs(original_lengths - rotated_lengths)
)

print("\nMaximum difference in point lengths:")
print(max_difference)

if max_difference < 1e-10:
    print("Rotation preserved the lengths successfully.")
else:
    print("There is a numerical difference.")


# ============================================================
# 6. Plot original and rotated points
# ============================================================

fig = plt.figure(figsize=(14, 6))

# ------------------------------------------------------------
# Original points
# ------------------------------------------------------------
ax1 = fig.add_subplot(1, 2, 1, projection="3d")

plot_points(
    ax1,
    A,
    "Original 3D Points"
)


# ------------------------------------------------------------
# Rotated points
# ------------------------------------------------------------
ax2 = fig.add_subplot(1, 2, 2, projection="3d")

plot_points(
    ax2,
    B,
    "Rotated 3D Points"
)


fig.suptitle(
    "3D Rotation Matrix Visualization",
    fontsize=16
)

plt.tight_layout()

plt.show()