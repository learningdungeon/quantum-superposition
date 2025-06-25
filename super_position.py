from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np

# Create quantum circuit with 1 qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to create superposition (|+> state)
qc.h(0)

# Get the statevector
state = Statevector.from_instruction(qc)

# Print basic information
print("="*50)
print("Quantum Superposition Circuit: |+⟩ State")
print("="*50)
print("\nCircuit diagram:")
print(qc.draw(output='text'))

# Statevector information
print("\nStatevector:")
print(state)
print(f"\nVector form: {np.round(state.data, 4)}")

# Measurement probabilities
probabilities = state.probabilities_dict()
print("\nMeasurement probabilities:")
print(f"P(|0⟩) = {probabilities.get('0', 0):.4f}")
print(f"P(|1⟩) = {probabilities.get('1', 0):.4f}")

# Bloch sphere visualization
print("\nBloch sphere visualization:")
plot_bloch_multivector(state)
plt.savefig('superposition_bloch.png', bbox_inches='tight')
print("Saved as 'superposition_bloch.png'")

# Manual Bloch vector calculation
a = state.data[0]  # |0> coefficient
b = state.data[1]  # |1> coefficient

# Bloch vector components:
# x = 2*Re(a*conj(b))
# y = 2*Im(a*conj(b))
# z = |a|^2 - |b|^2
x = 2 * np.real(a * np.conj(b))
y = 2 * np.imag(a * np.conj(b))
z = np.abs(a)**2 - np.abs(b)**2

print("\nBloch vector components:")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")
print(f"z = {z:.4f}")
print("→ Should be approximately (1, 0, 0) for |+⟩ state")

# Mathematical explanation
print("\nMathematical form:")
print(r"   1        1")
print(r"   ― |0⟩ + ― |1⟩")
print(r"  √2       √2")
