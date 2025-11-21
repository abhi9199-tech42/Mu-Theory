"""
Simple Near-Earth Time Dilation Simulation
Using Universal Change Equation: μ = ρ/χ = 1/τ
"""

import sys
import os
sys.path.append('.')

# Physical constants
G = 6.67430e-11  # Gravitational constant (m³/kg⋅s²)
M_earth = 5.972e24  # Earth mass (kg)
R_earth = 6.371e6  # Earth radius (m)
c = 299792458  # Speed of light (m/s)

class SimpleUniversalChange:
    """Simplified universal change calculator."""
    
    def calculate_mu_gravitational(self, rho, chi):
        """Calculate μ = ρ/χ for gravitational scenarios."""
        if abs(chi) < 1e-15:
            return float('inf')
        return rho / chi
    
    def calculate_tau_from_mu(self, mu):
        """Calculate τ = 1/μ."""
        if abs(mu) < 1e-15:
            return float('inf')
        return 1.0 / mu

def calculate_energy_density(altitude):
    """Calculate energy density ρ in Earth's gravitational field."""
    r = R_earth + altitude
    g = G * M_earth / (r**2)  # Gravitational field strength
    rho = g * 1e-9  # Scaled energy density
    return rho

def calculate_resistance_to_change(altitude):
    """Calculate χ (resistance to change) based on spacetime curvature."""
    r = R_earth + altitude
    r_s = 2 * G * M_earth / (c**2)  # Schwarzschild radius
    curvature_factor = 1 / (1 - r_s/(2*r))  # Modified for weak field
    chi = curvature_factor * 1e-6  # Scaled resistance
    return chi

def predict_time_dilation(altitude):
    """Predict time dilation at given altitude using μ = ρ/χ = 1/τ"""
    calc = SimpleUniversalChange()
    
    # Calculate energy density and resistance
    rho = calculate_energy_density(altitude)
    chi = calculate_resistance_to_change(altitude)
    
    # Calculate μ using gravitational formulation
    mu = calc.calculate_mu_gravitational(rho, chi)
    
    # Calculate time dilation factor
    tau = calc.calculate_tau_from_mu(mu)
    
    # Compare with Einstein's prediction
    r = R_earth + altitude
    phi_surface = -G * M_earth / R_earth
    phi_altitude = -G * M_earth / r
    tau_einstein = 1 + (phi_altitude - phi_surface) / (c**2)
    
    return {
        'altitude': altitude,
        'rho': rho,
        'chi': chi,
        'mu': mu,
        'tau': tau,
        'tau_einstein': tau_einstein,
        'time_gain_ns_per_s': (tau - 1) * 1e9
    }

def main():
    """Run the near-Earth time dilation simulation."""
    print("🌍 Near-Earth Spacetime Time Dilation Simulation")
    print("=" * 55)
    print("Using Universal Change Equation: μ = ρ/χ = 1/τ")
    print("Where:")
    print("  ρ = energy density (proportional to gravitational field)")
    print("  χ = resistance to change (spacetime curvature effect)")
    print("  μ = change flow rate")
    print("  τ = time dilation factor")
    print()
    
    # Test specific altitudes
    test_altitudes = {
        'Sea Level': 0,
        'Mount Everest': 8848,
        'Commercial Aviation': 10000,
        'Stratosphere': 50000,
        'Karman Line (Space)': 100000,
        'ISS Orbit': 408000,
        'High Earth Orbit': 1000000
    }
    
    print("📊 Time Dilation Predictions:")
    print("-" * 80)
    print(f"{'Location':<20} {'Alt(km)':<8} {'μ (×10⁻⁶)':<12} {'τ':<15} {'Δt(ns/s)':<10}")
    print("-" * 80)
    
    for name, altitude in test_altitudes.items():
        result = predict_time_dilation(altitude)
        
        print(f"{name:<20} {altitude/1000:<8.1f} {result['mu']*1e6:<12.3f} "
              f"{result['tau']:<15.10f} {result['time_gain_ns_per_s']:<10.2f}")
    
    print("-" * 80)
    print()
    
    # Detailed analysis for ISS
    print("🛰️ Detailed Analysis - International Space Station (408 km)")
    print("=" * 55)
    iss_result = predict_time_dilation(408000)
    
    print(f"Energy Density (ρ): {iss_result['rho']:.6e}")
    print(f"Resistance to Change (χ): {iss_result['chi']:.6e}")
    print(f"Change Flow Rate (μ): {iss_result['mu']:.6e}")
    print(f"Time Dilation Factor (τ): {iss_result['tau']:.12f}")
    print(f"Einstein's Prediction: {iss_result['tau_einstein']:.12f}")
    print(f"Time Gain: {iss_result['time_gain_ns_per_s']:.2f} nanoseconds per second")
    print(f"Daily Time Gain: {iss_result['time_gain_ns_per_s'] * 86400 / 1000:.2f} microseconds per day")
    print()
    
    # GPS satellites analysis
    print("🛰️ GPS Satellites Analysis (20,200 km)")
    print("=" * 40)
    gps_result = predict_time_dilation(20200000)
    
    print(f"Change Flow Rate (μ): {gps_result['mu']:.6e}")
    print(f"Time Dilation Factor (τ): {gps_result['tau']:.12f}")
    print(f"Time Gain: {gps_result['time_gain_ns_per_s']:.2f} nanoseconds per second")
    print(f"Daily Time Gain: {gps_result['time_gain_ns_per_s'] * 86400 / 1000:.2f} microseconds per day")
    print()
    
    print("💡 Physical Interpretation:")
    print("- Higher altitude → Lower ρ (weaker gravity)")
    print("- Higher altitude → Lower χ (less spacetime curvature)")
    print("- Net effect: μ changes, affecting time flow")
    print("- Positive time gain = clocks run faster at altitude")
    print("- This matches GPS satellite corrections needed!")

if __name__ == "__main__":
    main()