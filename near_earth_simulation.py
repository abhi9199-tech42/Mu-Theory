"""
Near-Earth Spacetime Time Dilation Simulation
Using Universal Change Equation: μ = ρ/χ = 1/τ

Predicts time dilation effects in Earth's gravitational field
at various altitudes using the universal change framework.
"""

import numpy as np
import matplotlib.pyplot as plt
from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator, PhysicsParameters

# Physical constants
G = 6.67430e-11  # Gravitational constant (m³/kg⋅s²)
M_earth = 5.972e24  # Earth mass (kg)
R_earth = 6.371e6  # Earth radius (m)
c = 299792458  # Speed of light (m/s)

class NearEarthSimulation:
    """Simulate time dilation in near-Earth spacetime using μ = ρ/χ = 1/τ"""
    
    def __init__(self):
        self.calculator = UniversalChangeCalculator()
        
    def calculate_gravitational_potential(self, altitude: float) -> float:
        """Calculate gravitational potential at given altitude."""
        r = R_earth + altitude
        return -G * M_earth / r
    
    def calculate_energy_density(self, altitude: float) -> float:
        """
        Calculate energy density ρ in Earth's gravitational field.
        Using ρ ∝ gravitational field strength.
        """
        r = R_earth + altitude
        # Gravitational field strength: g = GM/r²
        g = G * M_earth / (r**2)
        
        # Energy density proportional to field strength
        # Scale factor to get reasonable μ values
        rho = g * 1e-9  # Scaled energy density
        return rho
    
    def calculate_resistance_to_change(self, altitude: float) -> float:
        """
        Calculate χ (resistance to change) based on spacetime curvature.
        Higher curvature = higher resistance to change.
        """
        r = R_earth + altitude
        # Schwarzschild radius for reference
        r_s = 2 * G * M_earth / (c**2)
        
        # Resistance increases as we approach the surface (higher curvature)
        # χ ∝ 1/(1 - r_s/r) but scaled for near-Earth conditions
        curvature_factor = 1 / (1 - r_s/(2*r))  # Modified for weak field
        chi = curvature_factor * 1e-6  # Scaled resistance
        return chi
    
    def predict_time_dilation(self, altitude: float) -> dict:
        """
        Predict time dilation at given altitude using μ = ρ/χ = 1/τ
        
        Args:
            altitude: Height above Earth surface (meters)
            
        Returns:
            Dictionary with μ, τ, and analysis
        """
        # Calculate energy density and resistance
        rho = self.calculate_energy_density(altitude)
        chi = self.calculate_resistance_to_change(altitude)
        
        # Calculate μ using gravitational formulation
        mu = self.calculator.calculate_mu_gravitational(rho, chi)
        
        # Calculate time dilation factor
        tau = self.calculator.calculate_tau_from_mu(mu)
        
        # Compare with Einstein's prediction for validation
        r = R_earth + altitude
        phi_surface = -G * M_earth / R_earth
        phi_altitude = -G * M_earth / r
        
        # Einstein's time dilation: τ_einstein ≈ 1 + (φ_alt - φ_surf)/c²
        tau_einstein = 1 + (phi_altitude - phi_surface) / (c**2)
        
        return {
            'altitude': altitude,
            'rho': rho,
            'chi': chi,
            'mu': mu,
            'tau': tau,
            'tau_einstein': tau_einstein,
            'difference_percent': abs(tau - tau_einstein) / tau_einstein * 100
        }
    
    def run_altitude_sweep(self, max_altitude: float = 1000e3, num_points: int = 100):
        """Run simulation across range of altitudes."""
        altitudes = np.linspace(0, max_altitude, num_points)
        results = []
        
        print("🌍 Near-Earth Time Dilation Simulation")
        print("=" * 50)
        print(f"Using Universal Change Equation: μ = ρ/χ = 1/τ")
        print(f"Altitude range: 0 to {max_altitude/1000:.0f} km")
        print()
        
        for alt in altitudes:
            result = self.predict_time_dilation(alt)
            results.append(result)
            
            # Print some key altitudes
            if alt in [0, 100e3, 400e3, 1000e3] or alt == altitudes[-1]:
                print(f"Altitude: {alt/1000:6.0f} km")
                print(f"  μ (change flow): {result['mu']:.6e}")
                print(f"  τ (time dilation): {result['tau']:.10f}")
                print(f"  Einstein τ: {result['tau_einstein']:.10f}")
                print(f"  Difference: {result['difference_percent']:.3f}%")
                print()
        
        return results
    
    def plot_results(self, results):
        """Plot time dilation vs altitude."""
        altitudes = [r['altitude']/1000 for r in results]  # Convert to km
        tau_values = [r['tau'] for r in results]
        tau_einstein = [r['tau_einstein'] for r in results]
        mu_values = [r['mu'] for r in results]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Plot 1: Time dilation factor
        ax1.plot(altitudes, tau_values, 'b-', linewidth=2, label='Universal Change (μ = ρ/χ)')
        ax1.plot(altitudes, tau_einstein, 'r--', linewidth=2, label='Einstein GR')
        ax1.set_xlabel('Altitude (km)')
        ax1.set_ylabel('Time Dilation Factor (τ)')
        ax1.set_title('Time Dilation in Near-Earth Spacetime')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Add annotations for key altitudes
        key_alts = [0, 100, 400, 1000]  # km
        for alt_km in key_alts:
            if alt_km <= max(altitudes):
                idx = min(range(len(altitudes)), key=lambda i: abs(altitudes[i] - alt_km))
                ax1.annotate(f'{alt_km} km\nτ = {tau_values[idx]:.8f}', 
                           xy=(altitudes[idx], tau_values[idx]),
                           xytext=(10, 10), textcoords='offset points',
                           bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                           fontsize=8)
        
        # Plot 2: Change flow rate μ
        ax2.semilogy(altitudes, mu_values, 'g-', linewidth=2, label='μ = ρ/χ')
        ax2.set_xlabel('Altitude (km)')
        ax2.set_ylabel('Change Flow Rate μ (log scale)')
        ax2.set_title('Change Flow Rate vs Altitude')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        plt.tight_layout()
        plt.show()
        
        return fig

def main():
    """Run the near-Earth time dilation simulation."""
    sim = NearEarthSimulation()
    
    # Run simulation
    results = sim.run_altitude_sweep(max_altitude=1000e3, num_points=200)
    
    # Plot results
    fig = sim.plot_results(results)
    
    # Specific predictions for important altitudes
    print("\n🛰️ Specific Predictions:")
    print("=" * 30)
    
    important_altitudes = {
        'Sea Level': 0,
        'Commercial Aviation': 10e3,
        'Karman Line': 100e3,
        'ISS Orbit': 408e3,
        'GPS Satellites': 20200e3
    }
    
    for name, alt in important_altitudes.items():
        if alt <= 1000e3:  # Within our simulation range
            result = sim.predict_time_dilation(alt)
            print(f"{name} ({alt/1000:.0f} km):")
            print(f"  Time runs {(result['tau']-1)*1e9:.2f} ns/s faster than surface")
            print(f"  μ = {result['mu']:.3e}")
            print()

if __name__ == "__main__":
    main()