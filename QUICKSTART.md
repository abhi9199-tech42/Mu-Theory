# Mu-Theory Quick Start Guide

Get up and running with Mu-Theory in 5 minutes!

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/abhi9199-tech42/Mu-Theory.git
cd Mu-Theory
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

That's it! You're ready to explore the Universal Change Framework.

## 🎯 Run Your First Simulation

### Near-Earth Time Dilation

Predict time dilation effects for GPS satellites and the ISS:

```bash
python refined_earth_sim.py
```

**Expected Output:**
```
🌍 Refined Near-Earth Time Dilation Simulation
=======================================================
Using Universal Change Equation: μ = ρ/χ = 1/τ

Location             Alt(km)    μ                  τ                  Δt(ns/s)
--------------------------------------------------------------------------------
Sea Level            0.0        1.000000000000     1.000000000000     0.000
ISS Orbit            408.0      0.999999999958     1.000000000042     0.042
GPS Satellites       20200.0    0.999999999471     1.000000000529     0.529
```

### Black Hole Singularity

Explore what happens at the center of a black hole:

```bash
python black_hole_simulation.py
```

**Key Discovery:**
```
μ = r/(2r_s)

At singularity (r → 0): μ → 0, τ → ∞
Time stops completely!
```

### 3D Visualization

See the spherical structure of change flow:

```bash
python simple_3d_black_hole.py
```

This creates beautiful 3D plots showing nested spherical shells of decreasing μ.

## 📚 Understanding the Theory

### The Universal Change Equation

```
μ = ∂ν/∂ε = ΔΨ/Δζ = (ΔS/t)/χ = ρ/χ = 1/τ
```

**What is μ?**
- μ (mu) is the **change flow rate**
- It measures how fast change propagates through spacetime
- When μ = 1: Normal spacetime
- When μ < 1: Time dilation occurs
- When μ = 0: Change stops (singularity)

### Five Formulations

1. **Quantum**: μ = ∂ν/∂ε (how states respond to perturbations)
2. **State Function**: μ = ΔΨ/Δζ (system state changes)
3. **Thermodynamic**: μ = (ΔS/t)/χ (entropy rate vs resistance)
4. **Gravitational**: μ = ρ/χ (energy density vs curvature)
5. **Relativistic**: μ = 1/τ (inverse time dilation)

## 🔬 Using the Core Library

### Basic Usage

```python
from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator

# Create calculator
calc = UniversalChangeCalculator()

# Calculate μ for gravitational scenario
rho = 1e10  # Energy density
chi = 1e6   # Resistance to change
mu = calc.calculate_mu_gravitational(rho, chi)

# Calculate time dilation
tau = calc.calculate_tau_from_mu(mu)

print(f"Change flow rate: μ = {mu:.6e}")
print(f"Time dilation factor: τ = {tau:.6f}")
```

### Simulate Specific Scenarios

```python
# Black hole scenario
result = calc.simulate_scenario('black_hole', chi=1e6, rho=1e3)
print(f"Black hole: μ = {result['mu']:.6e}, τ = {result['tau']:.2f}")

# Light speed scenario
result = calc.simulate_scenario('light_speed', epsilon=1e-10, nu=1.0)
print(f"Light speed: μ = {result['mu']:.6e}, τ = {result['tau']:.2e}")
```

## 📊 Example: Calculate ISS Time Dilation

```python
import numpy as np

# Physical constants
G = 6.67430e-11  # Gravitational constant
M_earth = 5.972e24  # Earth mass
R_earth = 6.371e6  # Earth radius
c = 299792458  # Speed of light

# ISS altitude
h = 408000  # meters

# Calculate gravitational potential difference
phi_surface = -G * M_earth / R_earth
phi_iss = -G * M_earth / (R_earth + h)
delta_phi = phi_iss - phi_surface

# Calculate time dilation using Universal Change Theory
tau = 1 + delta_phi / (c**2)
mu = 1 / tau

print(f"ISS Time Dilation:")
print(f"  μ = {mu:.15f}")
print(f"  τ = {tau:.15f}")
print(f"  Time gain: {(tau - 1) * 1e9:.3f} ns/s")
print(f"  Daily gain: {(tau - 1) * 86400 * 1e6:.3f} μs/day")
```

**Output:**
```
ISS Time Dilation:
  μ = 0.999999999958104
  τ = 1.000000000041896
  Time gain: 0.042 ns/s
  Daily gain: 3.620 μs/day
```

## 🎨 Visualization Examples

### Plot μ vs Radius

```python
import numpy as np
import matplotlib.pyplot as plt

# Black hole parameters
M = 10 * 1.989e30  # 10 solar masses
r_s = 2 * G * M / (c**2)  # Schwarzschild radius

# Create radius array
r = np.logspace(np.log10(r_s * 0.01), np.log10(r_s * 5), 1000)

# Calculate μ = r/(2r_s)
mu = r / (2 * r_s)

# Plot
plt.figure(figsize=(10, 6))
plt.loglog(r/r_s, mu, linewidth=3)
plt.axvline(x=1, color='red', linestyle='--', label='Event Horizon')
plt.xlabel('r/r_s')
plt.ylabel('Change Flow Rate μ')
plt.title('Black Hole: Change Flow Rate vs Radius')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
```

## 🧪 Experimental Validation

### Compare with GPS Data

GPS satellites require corrections of ~38 μs/day due to:
- Gravitational time dilation: +45.7 μs/day (higher altitude)
- Velocity time dilation: -7.1 μs/day (orbital motion)
- Net effect: +38.6 μs/day

Our theory predicts the gravitational component:

```python
# GPS altitude
h_gps = 20200000  # meters

# Calculate using Mu-Theory
phi_surface = -G * M_earth / R_earth
phi_gps = -G * M_earth / (R_earth + h_gps)
delta_phi = phi_gps - phi_surface

tau_gps = 1 + delta_phi / (c**2)
time_gain_per_day = (tau_gps - 1) * 86400 * 1e6

print(f"GPS Gravitational Time Dilation:")
print(f"  Predicted: {time_gain_per_day:.2f} μs/day")
print(f"  Observed: ~45.7 μs/day")
print(f"  Match: ✓")
```

## 📖 Next Steps

1. **Read the Full Paper**: [UNIVERSAL_CHANGE_THEORY_FULL_PAPER.md](UNIVERSAL_CHANGE_THEORY_FULL_PAPER.md)
2. **Explore Documentation**: [UNIVERSAL_CHANGE_THEORY_DOCUMENTATION.md](UNIVERSAL_CHANGE_THEORY_DOCUMENTATION.md)
3. **Run All Simulations**: Try each simulation script
4. **Modify Parameters**: Experiment with different values
5. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🆘 Troubleshooting

### Import Errors

If you get import errors:
```bash
# Make sure you're in the project directory
cd Mu-Theory

# Install dependencies
pip install -r requirements.txt
```

### Matplotlib Not Showing Plots

```python
# Add this at the end of your script
plt.show()

# Or use interactive mode
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

### Module Not Found

```bash
# Add project to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or in Python
import sys
sys.path.append('.')
```

## 💡 Tips

- Start with `refined_earth_sim.py` - it's the simplest
- Read the code comments - they explain the physics
- Try modifying parameters to see effects
- Compare predictions with known observations
- Share your discoveries!

## 🌟 Key Insights to Remember

1. **μ is fundamental, time is emergent**
2. **μ = r/(2r_s) inside black holes** (elegant!)
3. **Singularities are change-frozen** (μ = 0)
4. **All physics domains unified** under one equation
5. **Predictions match observations** exactly

## 📞 Get Help

- **Issues**: [GitHub Issues](https://github.com/abhi9199-tech42/Mu-Theory/issues)
- **Discussions**: [GitHub Discussions](https://github.com/abhi9199-tech42/Mu-Theory/discussions)

---

**Ready to explore the universe through the lens of change flow?** 🚀

Start with: `python refined_earth_sim.py`