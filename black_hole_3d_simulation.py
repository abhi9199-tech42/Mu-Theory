"""
3D Black Hole Center Simulation
Using Universal Change Equation: μ = ρ/χ = 1/τ

Creates 3D visualizations of:
- Change flow rate μ in 3D space
- Energy density ρ distribution
- Resistance to change χ field
- Time dilation τ effects
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
from matplotlib.colors import LogNorm

# Physical constants
G = 6.67430e-11
c = 299792458
M_sun = 1.989e30

class BlackHole3DSimulation:
    """3D simulation of black hole using universal change equation."""
    
    def __init__(self, mass=10*M_sun):
        self.mass = mass
        self.r_s = 2 * G * mass / (c**2)  # Schwarzschild radius
        print(f"🕳️ 3D Black Hole Simulation")
        print(f"Mass: {mass/M_sun:.1f} Solar Masses")
        print(f"Schwarzschild Radius: {self.r_s:.2e} meters")
        print(f"Using: μ = ρ/χ = r/(2r_s) = 1/τ")
        print()
    
    def calculate_radius_3d(self, x, y, z):
        """Calculate radius from center in 3D."""
        return np.sqrt(x**2 + y**2 + z**2)
    
    def calculate_mu_3d(self, x, y, z):
        """Calculate μ = r/(2r_s) in 3D space."""
        r = self.calculate_radius_3d(x, y, z)
        # Avoid division by zero at center
        r = np.maximum(r, self.r_s * 1e-6)
        mu = r / (2 * self.r_s)
        return mu
    
    def calculate_rho_3d(self, x, y, z):
        """Calculate energy density ρ = GM/(r³c²) in 3D."""
        r = self.calculate_radius_3d(x, y, z)
        r = np.maximum(r, self.r_s * 1e-6)  # Avoid singularity
        rho = G * self.mass / (r**3 * c**2)
        return rho
    
    def calculate_chi_3d(self, x, y, z):
        """Calculate resistance χ = (r_s/r)² in 3D."""
        r = self.calculate_radius_3d(x, y, z)
        r = np.maximum(r, self.r_s * 1e-6)
        chi = (self.r_s / r)**2
        return chi
    
    def calculate_tau_3d(self, x, y, z):
        """Calculate time dilation τ = 2r_s/r in 3D."""
        r = self.calculate_radius_3d(x, y, z)
        r = np.maximum(r, self.r_s * 1e-6)
        tau = 2 * self.r_s / r
        return tau
    
    def create_3d_grid(self, grid_size=50, max_radius_factor=2.0):
        """Create 3D coordinate grid."""
        max_radius = self.r_s * max_radius_factor
        coords = np.linspace(-max_radius, max_radius, grid_size)
        X, Y, Z = np.meshgrid(coords, coords, coords)
        return X, Y, Z, coords
    
    def simulate_cross_section(self, z_slice=0, grid_size=100):
        """Create 2D cross-section through black hole center."""
        max_radius = self.r_s * 3
        x = np.linspace(-max_radius, max_radius, grid_size)
        y = np.linspace(-max_radius, max_radius, grid_size)
        X, Y = np.meshgrid(x, y)
        Z = np.full_like(X, z_slice)
        
        # Calculate fields
        mu_field = self.calculate_mu_3d(X, Y, Z)
        rho_field = self.calculate_rho_3d(X, Y, Z)
        chi_field = self.calculate_chi_3d(X, Y, Z)
        tau_field = self.calculate_tau_3d(X, Y, Z)
        
        return X, Y, mu_field, rho_field, chi_field, tau_field
    
    def plot_2d_cross_sections(self):
        """Plot 2D cross-sections of all fields."""
        X, Y, mu_field, rho_field, chi_field, tau_field = self.simulate_cross_section()
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Convert to units of Schwarzschild radius for plotting
        X_rs = X / self.r_s
        Y_rs = Y / self.r_s
        
        # Plot 1: Change Flow Rate μ
        im1 = ax1.contourf(X_rs, Y_rs, mu_field, levels=50, cmap='viridis')
        ax1.set_title('Change Flow Rate μ = r/(2r_s)')
        ax1.set_xlabel('x/r_s')
        ax1.set_ylabel('y/r_s')
        ax1.add_patch(plt.Circle((0, 0), 1, fill=False, color='red', linewidth=2, label='Event Horizon'))
        plt.colorbar(im1, ax=ax1, label='μ')
        ax1.legend()
        
        # Plot 2: Energy Density ρ (log scale)
        im2 = ax2.contourf(X_rs, Y_rs, np.log10(rho_field), levels=50, cmap='plasma')
        ax2.set_title('Energy Density ρ = GM/(r³c²)')
        ax2.set_xlabel('x/r_s')
        ax2.set_ylabel('y/r_s')
        ax2.add_patch(plt.Circle((0, 0), 1, fill=False, color='red', linewidth=2))
        plt.colorbar(im2, ax=ax2, label='log₁₀(ρ)')
        
        # Plot 3: Resistance to Change χ (log scale)
        im3 = ax3.contourf(X_rs, Y_rs, np.log10(chi_field), levels=50, cmap='inferno')
        ax3.set_title('Resistance to Change χ = (r_s/r)²')
        ax3.set_xlabel('x/r_s')
        ax3.set_ylabel('y/r_s')
        ax3.add_patch(plt.Circle((0, 0), 1, fill=False, color='red', linewidth=2))
        plt.colorbar(im3, ax=ax3, label='log₁₀(χ)')
        
        # Plot 4: Time Dilation τ (log scale)
        im4 = ax4.contourf(X_rs, Y_rs, np.log10(tau_field), levels=50, cmap='coolwarm')
        ax4.set_title('Time Dilation τ = 2r_s/r')
        ax4.set_xlabel('x/r_s')
        ax4.set_ylabel('y/r_s')
        ax4.add_patch(plt.Circle((0, 0), 1, fill=False, color='red', linewidth=2))
        plt.colorbar(im4, ax=ax4, label='log₁₀(τ)')
        
        plt.tight_layout()
        plt.suptitle('Black Hole Cross-Section: Universal Change Fields', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def plot_3d_isosurfaces(self):
        """Plot 3D isosurfaces of μ field."""
        # Create smaller grid for 3D visualization
        X, Y, Z, coords = self.create_3d_grid(grid_size=30, max_radius_factor=2.0)
        
        # Calculate μ field
        mu_field = self.calculate_mu_3d(X, Y, Z)
        
        fig = plt.figure(figsize=(15, 5))
        
        # Plot 1: μ = 0.5 surface (event horizon)
        ax1 = fig.add_subplot(131, projection='3d')
        
        # Find points where μ ≈ 0.5 (event horizon)
        mask_horizon = np.abs(mu_field - 0.5) < 0.05
        if np.any(mask_horizon):
            x_h, y_h, z_h = X[mask_horizon], Y[mask_horizon], Z[mask_horizon]
            ax1.scatter(x_h/self.r_s, y_h/self.r_s, z_h/self.r_s, 
                       c='red', s=1, alpha=0.6, label='μ = 0.5 (Event Horizon)')
        
        ax1.set_title('Event Horizon\nμ = 0.5')
        ax1.set_xlabel('x/r_s')
        ax1.set_ylabel('y/r_s')
        ax1.set_zlabel('z/r_s')
        ax1.legend()
        
        # Plot 2: μ = 0.1 surface (deep interior)
        ax2 = fig.add_subplot(132, projection='3d')
        
        mask_interior = np.abs(mu_field - 0.1) < 0.02
        if np.any(mask_interior):
            x_i, y_i, z_i = X[mask_interior], Y[mask_interior], Z[mask_interior]
            ax2.scatter(x_i/self.r_s, y_i/self.r_s, z_i/self.r_s, 
                       c='orange', s=1, alpha=0.8, label='μ = 0.1')
        
        ax2.set_title('Deep Interior\nμ = 0.1')
        ax2.set_xlabel('x/r_s')
        ax2.set_ylabel('y/r_s')
        ax2.set_zlabel('z/r_s')
        ax2.legend()
        
        # Plot 3: Multiple μ surfaces
        ax3 = fig.add_subplot(133, projection='3d')
        
        mu_levels = [0.5, 0.2, 0.1, 0.05]
        colors = ['red', 'orange', 'yellow', 'white']
        
        for mu_level, color in zip(mu_levels, colors):
            mask = np.abs(mu_field - mu_level) < 0.02
            if np.any(mask):
                x_m, y_m, z_m = X[mask], Y[mask], Z[mask]
                ax3.scatter(x_m/self.r_s, y_m/self.r_s, z_m/self.r_s, 
                           c=color, s=0.5, alpha=0.6, label=f'μ = {mu_level}')
        
        ax3.set_title('Change Flow Surfaces')
        ax3.set_xlabel('x/r_s')
        ax3.set_ylabel('y/r_s')
        ax3.set_zlabel('z/r_s')
        ax3.legend()
        
        plt.tight_layout()
        plt.show()
        
        return fig
    
    def plot_radial_profiles(self):
        """Plot radial profiles of all fields."""
        # Create radial distance array
        r_array = np.logspace(np.log10(self.r_s * 0.01), np.log10(self.r_s * 5), 1000)
        
        # Calculate fields along radial direction
        mu_radial = r_array / (2 * self.r_s)
        rho_radial = G * self.mass / (r_array**3 * c**2)
        chi_radial = (self.r_s / r_array)**2
        tau_radial = 2 * self.r_s / r_array
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        r_rs = r_array / self.r_s
        
        # Plot 1: μ vs radius
        ax1.loglog(r_rs, mu_radial, 'b-', linewidth=3, label='μ = r/(2r_s)')
        ax1.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax1.set_xlabel('r/r_s')
        ax1.set_ylabel('Change Flow Rate μ')
        ax1.set_title('Change Flow Rate vs Radius')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Plot 2: ρ vs radius
        ax2.loglog(r_rs, rho_radial, 'r-', linewidth=3, label='ρ = GM/(r³c²)')
        ax2.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax2.set_xlabel('r/r_s')
        ax2.set_ylabel('Energy Density ρ')
        ax2.set_title('Energy Density vs Radius')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Plot 3: χ vs radius
        ax3.loglog(r_rs, chi_radial, 'g-', linewidth=3, label='χ = (r_s/r)²')
        ax3.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax3.set_xlabel('r/r_s')
        ax3.set_ylabel('Resistance to Change χ')
        ax3.set_title('Resistance to Change vs Radius')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # Plot 4: τ vs radius
        ax4.loglog(r_rs, tau_radial, 'purple', linewidth=3, label='τ = 2r_s/r')
        ax4.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax4.set_xlabel('r/r_s')
        ax4.set_ylabel('Time Dilation Factor τ')
        ax4.set_title('Time Dilation vs Radius')
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        plt.tight_layout()
        plt.suptitle('Radial Profiles: Universal Change Fields', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def analyze_3d_structure(self):
        """Analyze the 3D structure of the black hole."""
        print("🔬 3D STRUCTURE ANALYSIS")
        print("=" * 40)
        
        # Key radii analysis
        key_radii = {
            'Event Horizon': self.r_s,
            'Half Radius': self.r_s / 2,
            'Quarter Radius': self.r_s / 4,
            'Near Singularity': self.r_s / 1000
        }
        
        print(f"{'Location':<20} {'r/r_s':<10} {'μ':<12} {'τ':<12} {'Physical State'}")
        print("-" * 70)
        
        for name, radius in key_radii.items():
            mu = radius / (2 * self.r_s)
            tau = 2 * self.r_s / radius
            
            if mu > 0.4:
                state = "Normal spacetime"
            elif mu > 0.1:
                state = "Moderate dilation"
            elif mu > 0.01:
                state = "Strong dilation"
            else:
                state = "Extreme dilation"
            
            print(f"{name:<20} {radius/self.r_s:<10.3f} {mu:<12.6f} {tau:<12.2f} {state}")
        
        print()
        print("🌟 3D INSIGHTS:")
        print("• Spherical symmetry: μ depends only on distance from center")
        print("• Event horizon: Perfect sphere where μ = 0.5, τ = 2")
        print("• Interior: Nested spherical shells of decreasing μ")
        print("• Singularity: Point where μ = 0, τ = ∞")
        print("• Change flow: Radially inward, slowing toward center")

def main():
    """Run complete 3D black hole simulation."""
    # Create simulation for 10 solar mass black hole
    sim = BlackHole3DSimulation(mass=10*M_sun)
    
    print("🚀 Starting 3D Visualization...")
    
    # 1. Plot 2D cross-sections
    print("\n📊 Generating 2D cross-sections...")
    fig1 = sim.plot_2d_cross_sections()
    
    # 2. Plot 3D isosurfaces
    print("\n🌐 Generating 3D isosurfaces...")
    fig2 = sim.plot_3d_isosurfaces()
    
    # 3. Plot radial profiles
    print("\n📈 Generating radial profiles...")
    fig3 = sim.plot_radial_profiles()
    
    # 4. Analyze 3D structure
    print("\n🔍 Analyzing 3D structure...")
    sim.analyze_3d_structure()
    
    print("\n🎯 3D SIMULATION COMPLETE!")
    print("The Universal Change Equation reveals the true 3D structure")
    print("of black holes as nested spheres of decreasing change flow!")

if __name__ == "__main__":
    main()