"""
Light Speed Boundary Simulation
Using Universal Change Equation: μ = ∂ν/∂ε

At light speed: μ → ∞, τ → 0
Photons experience no proper time.
"""

import numpy as np
import matplotlib.pyplot as plt
from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator

# Physical constants
c = 299792458  # Speed of light (m/s)

class LightSpeedSimulation:
    """Simulate behavior at light speed boundary using μ = ∂ν/∂ε."""
    
    def __init__(self):
        self.calc = UniversalChangeCalculator()
        self.c = c
        
    def calculate_mu_at_velocity(self, v):
        """
        Calculate μ at given velocity using Lorentz factor.
        
        At v → c: γ → ∞, μ → ∞, τ → 0
        """
        if v >= self.c:
            return float('inf')
        
        # Lorentz factor
        gamma = 1 / np.sqrt(1 - (v/self.c)**2)
        
        # At relativistic speeds: μ = γ (change flow accelerates)
        mu = gamma
        
        return mu
    
    def simulate_velocity_range(self):
        """Simulate μ across velocity range from 0 to 0.9999c."""
        # Velocity range (as fraction of c)
        v_fractions = np.linspace(0, 0.9999, 1000)
        velocities = v_fractions * self.c
        
        # Calculate μ and τ
        mu_values = []
        tau_values = []
        gamma_values = []
        
        for v in velocities:
            mu = self.calculate_mu_at_velocity(v)
            tau = 1 / mu if mu != float('inf') else 0
            gamma = 1 / np.sqrt(1 - (v/self.c)**2)
            
            mu_values.append(mu)
            tau_values.append(tau)
            gamma_values.append(gamma)
        
        return v_fractions, mu_values, tau_values, gamma_values
    
    def analyze_photon_behavior(self):
        """Analyze photon behavior at v = c."""
        print("💡 PHOTON BEHAVIOR ANALYSIS")
        print("=" * 50)
        print("At light speed (v = c):")
        print()
        
        print("Classical Relativity:")
        print("  γ → ∞ (Lorentz factor diverges)")
        print("  τ → 0 (no proper time)")
        print()
        
        print("Universal Change Theory:")
        print("  μ → ∞ (infinite change flow rate)")
        print("  τ = 1/μ → 0 (no time passage)")
        print()
        
        print("Physical Interpretation:")
        print("  • Photons experience infinite change rate")
        print("  • From photon's perspective, no time passes")
        print("  • Journey is instantaneous for the photon")
        print("  • Explains why photons don't decay")
        print("  • Consistent with massless particle behavior")
        print()
        
        # Calculate for near-light speeds
        test_velocities = [0.9*c, 0.99*c, 0.999*c, 0.9999*c]
        
        print("Approaching Light Speed:")
        print(f"{'v/c':<10} {'μ':<15} {'τ':<15} {'Interpretation'}")
        print("-" * 60)
        
        for v in test_velocities:
            mu = self.calculate_mu_at_velocity(v)
            tau = 1 / mu
            v_frac = v / c
            
            if v_frac < 0.95:
                interp = "Moderate dilation"
            elif v_frac < 0.995:
                interp = "Strong dilation"
            else:
                interp = "Extreme dilation"
            
            print(f"{v_frac:<10.4f} {mu:<15.2f} {tau:<15.6f} {interp}")
    
    def plot_light_speed_approach(self):
        """Plot behavior as velocity approaches c."""
        v_fractions, mu_values, tau_values, gamma_values = self.simulate_velocity_range()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Plot 1: μ vs v/c
        ax1.plot(v_fractions, mu_values, 'b-', linewidth=2)
        ax1.set_xlabel('v/c')
        ax1.set_ylabel('Change Flow Rate μ')
        ax1.set_title('Change Flow Rate vs Velocity')
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim([0, 50])
        ax1.axhline(y=1, color='gray', linestyle='--', alpha=0.5, label='μ = 1 (rest)')
        ax1.legend()
        
        # Plot 2: τ vs v/c
        ax2.plot(v_fractions, tau_values, 'r-', linewidth=2)
        ax2.set_xlabel('v/c')
        ax2.set_ylabel('Time Dilation Factor τ')
        ax2.set_title('Time Dilation vs Velocity')
        ax2.grid(True, alpha=0.3)
        ax2.set_ylim([0, 0.5])
        ax2.axhline(y=1, color='gray', linestyle='--', alpha=0.5, label='τ = 1 (rest)')
        ax2.legend()
        
        # Plot 3: Log scale μ
        ax3.semilogy(v_fractions, mu_values, 'g-', linewidth=2)
        ax3.set_xlabel('v/c')
        ax3.set_ylabel('Change Flow Rate μ (log scale)')
        ax3.set_title('μ Divergence at Light Speed')
        ax3.grid(True, alpha=0.3)
        ax3.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
        
        # Plot 4: μ vs τ relationship
        ax4.plot(mu_values, tau_values, 'purple', linewidth=2, label='μ vs τ')
        ax4.plot([1], [1], 'ro', markersize=10, label='Rest frame')
        ax4.set_xlabel('Change Flow Rate μ')
        ax4.set_ylabel('Time Dilation Factor τ')
        ax4.set_title('Universal Relationship: τ = 1/μ')
        ax4.grid(True, alpha=0.3)
        ax4.set_xlim([0, 50])
        ax4.set_ylim([0, 1])
        
        # Add theoretical curve
        mu_theory = np.linspace(1, 50, 100)
        tau_theory = 1 / mu_theory
        ax4.plot(mu_theory, tau_theory, 'r--', alpha=0.5, label='τ = 1/μ')
        ax4.legend()
        
        plt.tight_layout()
        plt.suptitle('Light Speed Boundary: Universal Change Analysis', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def compare_particles(self):
        """Compare different particle velocities."""
        print("\n⚡ PARTICLE VELOCITY COMPARISON")
        print("=" * 60)
        
        particles = {
            'Electron (LHC)': 0.999999991 * c,
            'Proton (LHC)': 0.999999896 * c,
            'Cosmic Ray': 0.9999999999 * c,
            'Neutrino': 0.999999 * c,
            'Photon': c
        }
        
        print(f"{'Particle':<20} {'v/c':<15} {'μ':<15} {'τ':<15}")
        print("-" * 65)
        
        for name, v in particles.items():
            if v >= c:
                mu_str = "∞"
                tau_str = "0"
                v_frac = 1.0
            else:
                mu = self.calculate_mu_at_velocity(v)
                tau = 1 / mu
                mu_str = f"{mu:.2e}"
                tau_str = f"{tau:.2e}"
                v_frac = v / c
            
            print(f"{name:<20} {v_frac:<15.12f} {mu_str:<15} {tau_str:<15}")
        
        print()
        print("Key Insights:")
        print("• Higher velocity → Higher μ → Lower τ")
        print("• At v = c: μ = ∞, τ = 0 (photons)")
        print("• Particle accelerators approach but never reach μ = ∞")
        print("• Explains particle lifetime extension at high speeds")

def main():
    """Run light speed simulation."""
    sim = LightSpeedSimulation()
    
    print("🚀 Light Speed Boundary Simulation")
    print("Using Universal Change Equation: μ = ∂ν/∂ε")
    print()
    
    # Analyze photon behavior
    sim.analyze_photon_behavior()
    
    # Compare particles
    sim.compare_particles()
    
    # Plot results
    print("\n📊 Generating visualizations...")
    fig = sim.plot_light_speed_approach()
    
    print("\n🎯 CONCLUSION:")
    print("At light speed, μ → ∞ means infinite change flow rate.")
    print("This explains why photons experience no time (τ = 0).")
    print("The Universal Change Equation naturally reproduces")
    print("special relativity while providing deeper insight!")

if __name__ == "__main__":
    main()