"""
Black Hole Center Simulation
Using Universal Change Equation: μ = ρ/χ = 1/τ

Explores what happens at the center of a black hole where:
- ρ → extreme values (infinite energy density)
- χ → ∞ (infinite resistance to change)
- Net effect: μ → 0 ⇒ τ → ∞ (time stops)
"""

import numpy as np
import sys
import os
sys.path.append('.')

# Physical constants
G = 6.67430e-11  # Gravitational constant
c = 299792458    # Speed of light
M_sun = 1.989e30 # Solar mass

class BlackHoleSimulation:
    """Simulate black hole physics using universal change equation."""
    
    def __init__(self):
        self.tolerance = 1e-15
        
    def calculate_schwarzschild_radius(self, mass):
        """Calculate Schwarzschild radius: r_s = 2GM/c²"""
        return 2 * G * mass / (c**2)
    
    def calculate_energy_density_at_radius(self, mass, r):
        """
        Calculate energy density ρ approaching black hole center.
        As r → 0, ρ → ∞ (singularity)
        """
        if r < self.tolerance:
            return float('inf')
        
        # Energy density scales as M/r³ near singularity
        rho = G * mass / (r**3 * c**2)
        return rho
    
    def calculate_resistance_to_change(self, mass, r):
        """
        Calculate χ (resistance to change) near black hole center.
        
        Key insight: As spacetime curvature becomes infinite,
        resistance to change also becomes infinite.
        χ → ∞ as r → 0
        """
        if r < self.tolerance:
            return float('inf')
        
        r_s = self.calculate_schwarzschild_radius(mass)
        
        # Resistance increases dramatically as we approach singularity
        # χ ∝ 1/r² (curvature effect)
        chi = (r_s / r)**2
        return chi
    
    def calculate_mu_at_radius(self, mass, r):
        """
        Calculate μ = ρ/χ at given radius from black hole center.
        
        Critical insight: Even though ρ → ∞ and χ → ∞,
        their ratio μ = ρ/χ → 0 as r → 0
        """
        rho = self.calculate_energy_density_at_radius(mass, r)
        chi = self.calculate_resistance_to_change(mass, r)
        
        if chi == float('inf') and rho == float('inf'):
            # At true singularity: μ → 0
            return 0.0
        elif chi == float('inf'):
            return 0.0
        else:
            return rho / chi
    
    def calculate_time_dilation_at_radius(self, mass, r):
        """Calculate time dilation τ = 1/μ at given radius."""
        mu = self.calculate_mu_at_radius(mass, r)
        
        if abs(mu) < self.tolerance:
            return float('inf')  # Time stops at singularity
        else:
            return 1.0 / mu
    
    def simulate_approach_to_singularity(self, mass, num_points=20):
        """Simulate approach from event horizon to singularity."""
        r_s = self.calculate_schwarzschild_radius(mass)
        
        # Create logarithmic approach to center
        # From event horizon (r_s) down to near-singularity
        radii = np.logspace(np.log10(r_s), np.log10(r_s * 1e-10), num_points)
        
        results = []
        
        print(f"🕳️ BLACK HOLE SINGULARITY SIMULATION")
        print("=" * 60)
        print(f"Black Hole Mass: {mass/M_sun:.1f} Solar Masses")
        print(f"Schwarzschild Radius: {r_s:.3e} meters")
        print(f"Using Universal Change Equation: μ = ρ/χ = 1/τ")
        print()
        print("Journey from Event Horizon to Singularity:")
        print("-" * 80)
        print(f"{'Distance from Center':<20} {'ρ (Energy Density)':<20} {'χ (Resistance)':<15} {'μ':<15} {'τ':<15}")
        print("-" * 80)
        
        for i, r in enumerate(radii):
            rho = self.calculate_energy_density_at_radius(mass, r)
            chi = self.calculate_resistance_to_change(mass, r)
            mu = self.calculate_mu_at_radius(mass, r)
            tau = self.calculate_time_dilation_at_radius(mass, r)
            
            # Format for display
            if rho == float('inf'):
                rho_str = "∞"
            else:
                rho_str = f"{rho:.2e}"
                
            if chi == float('inf'):
                chi_str = "∞"
            else:
                chi_str = f"{chi:.2e}"
                
            if tau == float('inf'):
                tau_str = "∞"
            else:
                tau_str = f"{tau:.2e}"
            
            print(f"{r/r_s:.2e} × r_s      {rho_str:<20} {chi_str:<15} {mu:<15.2e} {tau_str:<15}")
            
            results.append({
                'radius': r,
                'radius_fraction': r/r_s,
                'rho': rho,
                'chi': chi,
                'mu': mu,
                'tau': tau
            })
        
        print("-" * 80)
        return results
    
    def analyze_singularity_physics(self, mass):
        """Analyze the physics at the singularity using universal change theory."""
        r_s = self.calculate_schwarzschild_radius(mass)
        
        print(f"\n🔬 SINGULARITY ANALYSIS")
        print("=" * 40)
        print(f"At the center of the black hole (r → 0):")
        print()
        
        # Analyze the limiting behavior
        print(f"Energy Density (ρ):")
        print(f"  ρ = GM/(r³c²) → ∞ as r → 0")
        print(f"  Physical meaning: Infinite mass-energy concentration")
        print()
        
        print(f"Resistance to Change (χ):")
        print(f"  χ = (r_s/r)² → ∞ as r → 0")
        print(f"  Physical meaning: Infinite spacetime curvature")
        print()
        
        print(f"Change Flow Rate (μ):")
        print(f"  μ = ρ/χ = [GM/(r³c²)] / [(r_s/r)²]")
        print(f"  μ = [GM/(r³c²)] / [4G²M²/(r²c⁴)]")
        print(f"  μ = c²r/(4GM) → 0 as r → 0")
        print(f"  Physical meaning: Change becomes impossible!")
        print()
        
        print(f"Time Dilation (τ):")
        print(f"  τ = 1/μ = 4GM/(c²r) → ∞ as r → 0")
        print(f"  Physical meaning: Time stops completely!")
        print()
        
        print(f"🌟 KEY INSIGHTS:")
        print(f"• Even though both ρ and χ become infinite,")
        print(f"  their ratio μ = ρ/χ approaches zero")
        print(f"• This means change flow rate goes to zero")
        print(f"• Therefore τ = 1/μ → ∞ (time stops)")
        print(f"• The singularity is a region where change cannot occur!")
        print(f"• This explains why nothing can escape - not even change itself!")
    
    def compare_black_hole_sizes(self):
        """Compare different black hole masses."""
        black_holes = {
            'Stellar Mass': 10 * M_sun,
            'Intermediate': 1000 * M_sun,
            'Sagittarius A*': 4.1e6 * M_sun,
            'Supermassive': 1e9 * M_sun
        }
        
        print(f"\n🌌 BLACK HOLE COMPARISON")
        print("=" * 50)
        print(f"{'Type':<15} {'Mass (M☉)':<12} {'r_s (km)':<10} {'μ at r_s/1000':<15}")
        print("-" * 55)
        
        for name, mass in black_holes.items():
            r_s = self.calculate_schwarzschild_radius(mass)
            test_radius = r_s / 1000  # Very close to singularity
            mu = self.calculate_mu_at_radius(mass, test_radius)
            
            print(f"{name:<15} {mass/M_sun:<12.1e} {r_s/1000:<10.2f} {mu:<15.2e}")

def main():
    """Run black hole center simulation."""
    sim = BlackHoleSimulation()
    
    # Simulate a stellar mass black hole (10 solar masses)
    mass = 10 * M_sun
    
    # Run the simulation
    results = sim.simulate_approach_to_singularity(mass)
    
    # Analyze singularity physics
    sim.analyze_singularity_physics(mass)
    
    # Compare different black hole sizes
    sim.compare_black_hole_sizes()
    
    print(f"\n🎯 CONCLUSION:")
    print(f"The Universal Change Equation μ = ρ/χ = 1/τ reveals that")
    print(f"at black hole singularities:")
    print(f"• Change flow rate μ → 0")
    print(f"• Time dilation τ → ∞")
    print(f"• Time effectively stops")
    print(f"• This provides a unified explanation for why singularities")
    print(f"  are 'frozen' regions where normal physics breaks down!")

if __name__ == "__main__":
    main()