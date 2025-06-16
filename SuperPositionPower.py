#Import Qiskit 

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
#Create Quantum Circuit  for Super Position using Hadamard

qc = QuantumCircuit (1,1) #Register Qubit and Classical Bit

qc.h(0) #Applied Hadamard Gate on qubit 0 for the superposition

qc.measure (0,0) #collapse of superposition by measure to attain final result

print("Circuit Created")
print(qc.draw(output='text'))

# Simulation

simulator = AerSimulator() #New simulator object

job = simulator.run(qc, shots=1000) #Direct execution

result = job.result() #get results

counts = result.get_counts() #Extract counts
print ("\n Measurment Result") 
print (counts)


#plot_histogram(counts).savefig('SuperPositionGraph.png') #Visualization saved in png

#plt.savefig('SuperPositionGraph.png',bbox_inches ='tight)

#print ('SuperPositionGraph.png')


#cat << 'EOF' > quantum_ascii.py
#!/usr/bin/env python3

# Quantum ASCII Visualizer - Single Qubit Superposition
import sys

# Your measurement results
counts = {'0': 496, '1': 504}  # Your actual results
total_shots = sum(counts.values())

# Calculate percentages
percentages = {state: (count / total_shots * 100) for state, count in counts.items()}

# Visualization parameters
MAX_BAR_WIDTH = 60  # Maximum bar width in characters
MAX_BAR_HEIGHT = 20  # Maximum bar height

# Calculate scaling
max_count = max(counts.values())
scale_factor = MAX_BAR_WIDTH / max_count
bar_widths = {state: int(count * scale_factor) for state, count in counts.items()}

# Generate visualization
print("\n\033[1;36mQUANTUM SUPERPOSITION RESULTS\033[0m")
print(f"Total measurements: {total_shots} shots")
print(f"Expected ~50/50 distribution | Actual: {percentages['0']:.1f}% |0› vs {percentages['1']:.1f}% |1›\n")

# Draw bars with labels
for state in sorted(counts.keys()):
    count = counts[state]
    pct = percentages[state]
    width = bar_widths[state]
    
    # Create ASCII bar
    bar = '\033[1;32m█\033[0m' * width
    
    # Print state with Dirac notation
    print(f"\033[1;35m|{state}›\033[0m: {bar} {count} ({pct:.1f}%)")

# Draw reference lines
print("\n\033[1;34mProbability Scale:\033[0m")
print("0% " + " " * (MAX_BAR_WIDTH//2 - 3) + "50% " + " " * (MAX_BAR_WIDTH//2 - 4) + "100%")
print("└" + "─" * (MAX_BAR_WIDTH//2 - 1) + "┴" + "─" * (MAX_BAR_WIDTH//2 - 1) + "┘")

# Quantum state explanation
print("\n\033[1;33mInterpretation:\033[0m")
print("- Hadamard gate created superposition: |0› → (|0› + |1›)/√2")
print(f"- Measurement collapsed state to |0› {counts['0']} times and |1› {counts['1']} times")
print(f"- Observed slight bias: \033[1;31m{abs(50 - percentages['1']):.1f}% deviation\033[0m from ideal 50/50 distribution")
print("- Typical in quantum systems due to probabilistic nature")

# Make executable and run
#chmod +x quantum_ascii.py
#./quantum_ascii.py
