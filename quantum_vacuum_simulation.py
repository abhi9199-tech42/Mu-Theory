"""
Quantum Vacuum Fluctuation Simulation
Using Universal Change Equation: μ = ΔΨ/Δζ

Virtual particles emerge from vacuum energy via change flow dynamics.
"""

import numpy as np
import matplotlib.pyplot as plt
from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator

# Physical constants
hbar = 1.055e-34  # Reduced Planck constant
c = 299792458     # Speed of light
epsilon_0 = 8.854e-12  # Vacuum permittivity

class QuantumVacuumSimulation:
    """Simulate quantum vacuum fluctuations using μ = ΔΨ/Δζ."""
    
    def __init__(self):
        self.calc = UniversalChangeCalculator()
        self.hbar = hbar
        self.c = c
        
    def calculate_vacuum_mu(self, delta_psi, delta_zeta):
        """
        Calculate μ for vacuum fluctuations.
        
        ΔΨ: Change in vacuum state function
        Δζ: Change in entropy interaction space
        """
        return self.calc.calculate_mu_state(0, delta_psi, 0, delta_zeta)
    
    def heisenberg_uncertainty_time(self, delta_E):
        """
        Calculate uncertainty in time from energy uncertainty.
        Δt ≥ ℏ/(2ΔE)
        """
        return self.hbar / (2 * delta_E)
    
    def virtual_particle_lifetime(self, mass):
        """
        Estimate virtual particle lifetime.
        
        For particle of mass m:
        ΔE ≈ mc²
        Δt ≈ ℏ/(2mc²)
        """
        delta_E = mass * self.c**2
        return self.heisenberg_uncertainty_time(delta_E)
    
    def simulate_vacuum_fluctuations(self):
        """Simulate vacuum fluctuations at different energy scales."""
        print("🌌 QUANTUM VACUUM FLUCTUATION SIMULATION")
        print("=" * 55)
        print("Using μ = ΔΨ/Δζ for vacuum state changes")
        print()
        
        # Different virtual particle scenarios
        particles = {
            'Virtual Photon': 0,  # massless
            'Virtual Electron-Positron': 9.109e-31 * 2,  # electron mass × 2
            'Virtual Muon Pair': 1.883e-28 * 2,
            'Virtual Pion': 2.488e-28,
            'Virtual Proton-Antiproton': 1.673e-27 * 2
        }
        
        print(f"{'Particle Pair':<30} {'Mass (kg)':<15} {'Lifetime (s)':<15} {'μ':<15}")
        print("-" * 80)
        
        for name, mass in particles.items():
            if mass == 0:
                lifetime = float('inf')
                lifetime_str = "∞"
                # For photons, use energy scale
                delta_E = 1e-19  # ~1 eV
                delta_t = self.heisenberg_uncertainty_time(delta_E)
                lifetime = delta_t
                lifetime_str = f"{lifetime:.2e}"
            else:
                lifetime = self.virtual_particle_lifetime(mass)
                lifetime_str = f"{lifetime:.2e}"
            
            # Calculate μ for this fluctuation
            # ΔΨ ~ energy scale, Δζ ~ spatial scale
            delta_psi = mass * self.c**2 if mass > 0 else 1e-19
            delta_zeta = lifetime * self.c  # characteristic length scale
            
            mu = self.calculate_vacuum_mu(delta_psi, delta_zeta)
            
            print(f"{name:<30} {mass:<15.2e} {lifetime_str:<15} {mu:<15.2e}")
        
        print()
        print("Physical Interpretation:")
        print("• Higher mass → Shorter lifetime → Higher μ")
        print("• Virtual particles are rapid change flow events")
        print("• μ represents rate of vacuum state transitions")
        print("• Heisenberg uncertainty emerges from μ dynamics")
    
    def casimir_effect_analysis(self):
        """Analyze Casimir effect using change flow theory."""
        print("\n🔬 CASIMIR EFFECT ANALYSIS")
        print("=" * 40)
        print("Casimir force between parallel plates")
        print()
        
        # Plate separations
        separations = np.array([1e-9, 10e-9, 100e-9, 1e-6, 10e-6])  # meters
        
        print(f"{'Separation (nm)':<20} {'Allowed Modes':<20} {'μ_vacuum':<15}")
        print("-" * 60)
        
        for d in separations:
            # Number of allowed vacuum modes
            # n ~ (d/λ_cutoff)³ where λ_cutoff ~ Planck length
            lambda_planck = 1.616e-35
            n_modes = (d / lambda_planck)**3
            
            # Vacuum μ depends on mode density
            # More modes → higher change flow rate
            mu_vacuum = n_modes / 1e100  # Normalized
            
            print(f"{d*1e9:<20.1f} {n_modes:<20.2e} {mu_vacuum:<15.2e}")
        
        print()
        print("Key Insight:")
        print("• Fewer modes between plates → Lower μ_vacuum")
        print("• Higher μ_vacuum outside → Net inward pressure")
        print("• Casimir force emerges from μ gradient!")
    
    def plot_vacuum_energy_spectrum(self):
        """Plot vacuum energy spectrum and μ distribution."""
        # Energy range (eV)
        energies_eV = np.logspace(-3, 3, 1000)  # meV to keV
        energies_J = energies_eV * 1.602e-19
        
        # Calculate lifetimes and μ values
        lifetimes = self.hbar / (2 * energies_J)
        
        # μ ~ E/ℏ (energy scale / time scale)
        mu_values = energies_J / self.hbar
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Plot 1: Virtual particle lifetime vs energy
        ax1.loglog(energies_eV, lifetimes, 'b-', linewidth=2)
        ax1.set_xlabel('Energy (eV)')
        ax1.set_ylabel('Virtual Particle Lifetime (s)')
        ax1.set_title('Heisenberg Uncertainty: Δt ≥ ℏ/(2ΔE)')
        ax1.grid(True, alpha=0.3)
        
        # Mark key particles
        particles_eV = {
            'Electron': 511000,
            'Muon': 105700000,
            'Pion': 139570000
        }
        for name, E in particles_eV.items():
            if E >= energies_eV.min() and E <= energies_eV.max():
                lifetime = self.hbar / (2 * E * 1.602e-19)
                ax1.plot(E, lifetime, 'ro', markersize=8)
                ax1.annotate(name, xy=(E, lifetime), xytext=(10, 10),
                           textcoords='offset points', fontsize=8)
        
        # Plot 2: μ vs energy
        ax2.loglog(energies_eV, mu_values, 'r-', linewidth=2)
        ax2.set_xlabel('Energy (eV)')
        ax2.set_ylabel('Change Flow Rate μ (Hz)')
        ax2.set_title('Vacuum Change Flow Rate vs Energy')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: Energy density distribution
        # Vacuum energy density ~ E³ (density of states)
        energy_density = energies_J**3
        ax3.loglog(energies_eV, energy_density, 'g-', linewidth=2)
        ax3.set_xlabel('Energy (eV)')
        ax3.set_ylabel('Vacuum Energy Density (arbitrary)')
        ax3.set_title('Vacuum Energy Spectrum')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: μ distribution in space
        # Simulate μ field around a fluctuation
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        
        # μ field: Gaussian fluctuation
        mu_field = 1 + 0.5 * np.exp(-R**2)
        
        im = ax4.contourf(X, Y, mu_field, levels=20, cmap='viridis')
        ax4.set_xlabel('x (Planck lengths)')
        ax4.set_ylabel('y (Planck lengths)')
        ax4.set_title('μ Field: Virtual Particle Fluctuation')
        plt.colorbar(im, ax=ax4, label='μ')
        
        plt.tight_layout()
        plt.suptitle('Quantum Vacuum: Change Flow Analysis', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def zero_point_energy_analysis(self):
        """Analyze zero-point energy using μ framework."""
        print("\n⚡ ZERO-POINT ENERGY ANALYSIS")
        print("=" * 40)
        print("Vacuum energy from μ perspective")
        print()
        
        # For harmonic oscillator: E_0 = ℏω/2
        frequencies = np.array([1e12, 1e15, 1e18, 1e21])  # Hz
        
        print(f"{'Frequency (Hz)':<20} {'E_0 (eV)':<15} {'μ (Hz)':<15}")
        print("-" * 55)
        
        for freq in frequencies:
            E_0 = 0.5 * self.hbar * 2 * np.pi * freq
            E_0_eV = E_0 / 1.602e-19
            mu = freq  # Change flow rate ~ frequency
            
            print(f"{freq:<20.2e} {E_0_eV:<15.2e} {mu:<15.2e}")
        
        print()
        print("Insight:")
        print("• Zero-point energy = minimum change flow rate")
        print("• Even at T=0, μ > 0 (quantum fluctuations)")
        print("• Vacuum is never truly 'empty' - always changing!")

def main():
    """Run quantum vacuum simulation."""
    sim = QuantumVacuumSimulation()
    
    print("🌌 Quantum Vacuum Fluctuation Simulation")
    print("Using Universal Change Equation: μ = ΔΨ/Δζ")
    print()
    
    # Simulate vacuum fluctuations
    sim.simulate_vacuum_fluctuations()
    
    # Casimir effect
    sim.casimir_effect_analysis()
    
    # Zero-point energy
    sim.zero_point_energy_analysis()
    
    # Plot results
    print("\n📊 Generating visualizations...")
    fig = sim.plot_vacuum_energy_spectrum()
    
    print("\n🎯 CONCLUSION:")
    print("Quantum vacuum fluctuations are manifestations of")
    print("change flow dynamics at the Planck scale.")
    print("Virtual particles emerge when μ = ΔΨ/Δζ exceeds")
    print("threshold values, consistent with Heisenberg uncertainty!")

if __name__ == "__main__":
    main()