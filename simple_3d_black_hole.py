"""
Simple 3D Black Hole Center Visualization
Using Universal Change Equation: μ = r/(2r_s) = 1/τ

Creates clear 3D visualizations without complex matplotlib features.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Physical constants
G = 6.67430e-11
c = 299792458
M_sun = 1.989e30

class Simple3DBlackHole:
    """Simple 3D black hole visualization."""
    
    def __init__(self, mass=10*M_sun):
        self.mass = mass
        self.r_s = 2 * G * mass / (c**2)
        print(f"🕳️ Simple 3D Black Hole Visualization")
        print(f"Mass: {mass/M_sun:.1f} Solar Masses")
        print(f"Schwarzschild Radius: {self.r_s:.2e} meters")
        print(f"Universal Equation: μ = r/(2r_s) = 1/τ")
        print()
    
    def mu_field(self, r):
        """Calculate μ = r/(2r_s)"""
        return np.maximum(r / (2 * self.r_s), 1e-6)
    
    def tau_field(self, r):
        """Calculate τ = 2r_s/r"""
        return 2 * self.r_s / np.maximum(r, self.r_s * 1e-6)
    
    def create_spherical_shells(self):
        """Create 3D spherical shells showing μ levels."""
        fig = plt.figure(figsize=(15, 12))
        
        # Create 4 subplots for different views
        ax1 = fig.add_subplot(221, projection='3d')
        ax2 = fig.add_subplot(222, projection='3d')
        ax3 = fig.add_subplot(223, projection='3d')
        ax4 = fig.add_subplot(224, projection='3d')
        
        # Define μ levels and corresponding radii
        mu_levels = [0.5, 0.25, 0.125, 0.0625]  # Event horizon, half, quarter, eighth
        colors = ['red', 'orange', 'yellow', 'white']
        labels = ['Event Horizon (μ=0.5)', 'μ=0.25', 'μ=0.125', 'μ=0.0625']
        
        # Create spherical coordinates
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 20)
        
        axes = [ax1, ax2, ax3, ax4]
        titles = ['Nested μ Shells', 'Event Horizon Detail', 'Interior Structure', 'Near Singularity']
        
        for i, ax in enumerate(axes):
            for j, (mu_level, color, label) in enumerate(zip(mu_levels, colors, labels)):
                # Calculate radius for this μ level: r = 2r_s * μ
                radius = 2 * self.r_s * mu_level
                
                # Create sphere coordinates
                x = radius * np.outer(np.cos(u), np.sin(v))
                y = radius * np.outer(np.sin(u), np.sin(v))
                z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
                
                # Convert to Schwarzschild radius units
                x_rs = x / self.r_s
                y_rs = y / self.r_s
                z_rs = z / self.r_s
                
                # Plot sphere with different transparency for each view
                alpha = 0.3 if i == 0 else 0.5
                if i == 1 and j > 0:  # Event horizon detail - skip inner shells
                    continue
                if i == 2 and j == 0:  # Interior - skip event horizon
                    continue
                if i == 3 and j < 2:  # Near singularity - only innermost shells
                    continue
                
                ax.plot_surface(x_rs, y_rs, z_rs, alpha=alpha, color=color, label=label)
            
            ax.set_xlabel('x/r_s')
            ax.set_ylabel('y/r_s')
            ax.set_zlabel('z/r_s')
            ax.set_title(titles[i])
            
            # Set appropriate limits for each view
            if i == 0:  # Full view
                ax.set_xlim([-1.2, 1.2])
                ax.set_ylim([-1.2, 1.2])
                ax.set_zlim([-1.2, 1.2])
            elif i == 1:  # Event horizon
                ax.set_xlim([-1.1, 1.1])
                ax.set_ylim([-1.1, 1.1])
                ax.set_zlim([-1.1, 1.1])
            elif i == 2:  # Interior
                ax.set_xlim([-0.6, 0.6])
                ax.set_ylim([-0.6, 0.6])
                ax.set_zlim([-0.6, 0.6])
            else:  # Near singularity
                ax.set_xlim([-0.2, 0.2])
                ax.set_ylim([-0.2, 0.2])
                ax.set_zlim([-0.2, 0.2])
        
        plt.tight_layout()
        plt.suptitle('3D Black Hole Structure: Spherical μ Shells', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def plot_cross_sections_3d(self):
        """Plot multiple cross-sections in 3D."""
        fig = plt.figure(figsize=(15, 10))
        
        # Create 2D cross-sections at different z-levels
        ax1 = fig.add_subplot(231)
        ax2 = fig.add_subplot(232)
        ax3 = fig.add_subplot(233)
        ax4 = fig.add_subplot(234)
        ax5 = fig.add_subplot(235)
        ax6 = fig.add_subplot(236)
        
        axes = [ax1, ax2, ax3, ax4, ax5, ax6]
        z_levels = [0, 0.2, 0.4, 0.6, 0.8, 1.0]  # Different z/r_s levels
        
        # Create 2D grid
        max_r = self.r_s * 2
        x = np.linspace(-max_r, max_r, 100)
        y = np.linspace(-max_r, max_r, 100)
        X, Y = np.meshgrid(x, y)
        
        for i, (ax, z_level) in enumerate(zip(axes, z_levels)):
            # Calculate radius including z component
            Z = np.full_like(X, z_level * self.r_s)
            R = np.sqrt(X**2 + Y**2 + Z**2)
            
            # Calculate μ field
            mu_field = self.mu_field(R)
            
            # Plot contours
            contour = ax.contourf(X/self.r_s, Y/self.r_s, mu_field, levels=20, cmap='viridis')
            
            # Add event horizon circle (adjusted for z-level)
            if z_level < 1.0:
                horizon_radius = np.sqrt(1 - z_level**2) if z_level < 1 else 0
                if horizon_radius > 0:
                    circle = plt.Circle((0, 0), horizon_radius, fill=False, color='red', linewidth=2)
                    ax.add_patch(circle)
            
            ax.set_xlabel('x/r_s')
            ax.set_ylabel('y/r_s')
            ax.set_title(f'z/r_s = {z_level:.1f}')
            ax.set_aspect('equal')
            
            # Add colorbar for first plot
            if i == 0:
                plt.colorbar(contour, ax=ax, label='μ')
        
        plt.tight_layout()
        plt.suptitle('3D Cross-Sections: μ Field at Different z-levels', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def create_radial_analysis(self):
        """Create comprehensive radial analysis."""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Create radial array
        r_array = np.logspace(np.log10(self.r_s * 0.001), np.log10(self.r_s * 5), 1000)
        r_rs = r_array / self.r_s
        
        # Calculate fields
        mu_values = self.mu_field(r_array)
        tau_values = self.tau_field(r_array)
        rho_values = G * self.mass / (r_array**3 * c**2)
        chi_values = (self.r_s / r_array)**2
        
        # Plot 1: μ vs radius
        ax1.loglog(r_rs, mu_values, 'b-', linewidth=3, label='μ = r/(2r_s)')
        ax1.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax1.axhline(y=1, color='gray', linestyle=':', alpha=0.5, label='μ = 1')
        ax1.set_xlabel('r/r_s')
        ax1.set_ylabel('Change Flow Rate μ')
        ax1.set_title('Change Flow Rate')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # Plot 2: τ vs radius
        ax2.loglog(r_rs, tau_values, 'r-', linewidth=3, label='τ = 2r_s/r')
        ax2.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax2.axhline(y=1, color='gray', linestyle=':', alpha=0.5, label='τ = 1')
        ax2.set_xlabel('r/r_s')
        ax2.set_ylabel('Time Dilation Factor τ')
        ax2.set_title('Time Dilation')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        
        # Plot 3: ρ vs radius
        ax3.loglog(r_rs, rho_values, 'g-', linewidth=3, label='ρ = GM/(r³c²)')
        ax3.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax3.set_xlabel('r/r_s')
        ax3.set_ylabel('Energy Density ρ')
        ax3.set_title('Energy Density')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # Plot 4: χ vs radius
        ax4.loglog(r_rs, chi_values, 'purple', linewidth=3, label='χ = (r_s/r)²')
        ax4.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax4.set_xlabel('r/r_s')
        ax4.set_ylabel('Resistance to Change χ')
        ax4.set_title('Resistance to Change')
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        plt.tight_layout()
        plt.suptitle('Radial Profiles: All Universal Change Parameters', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def analyze_3d_geometry(self):
        """Analyze the 3D geometry of the black hole."""
        print("📐 3D GEOMETRY ANALYSIS")
        print("=" * 40)
        
        # Key geometric properties
        print("🌐 SPHERICAL SYMMETRY:")
        print(f"• Event horizon radius: r_s = {self.r_s:.2e} m")
        print(f"• Event horizon surface area: 4πr_s² = {4*np.pi*self.r_s**2:.2e} m²")
        print(f"• Event horizon volume: (4/3)πr_s³ = {(4/3)*np.pi*self.r_s**3:.2e} m³")
        print()
        
        # μ shell analysis
        print("🔄 CHANGE FLOW SHELLS:")
        mu_shells = [0.5, 0.25, 0.125, 0.0625, 0.03125]
        
        print(f"{'μ Level':<10} {'Radius (r_s)':<15} {'Surface Area':<20} {'Volume Ratio'}")
        print("-" * 70)
        
        for mu in mu_shells:
            radius_rs = 2 * mu  # r/r_s = 2μ
            surface_area_ratio = (2 * mu)**2  # (r/r_s)²
            volume_ratio = (2 * mu)**3  # (r/r_s)³
            
            print(f"{mu:<10.3f} {radius_rs:<15.3f} {surface_area_ratio:<20.3f} {volume_ratio:<10.3f}")
        
        print()
        print("🎯 KEY INSIGHTS:")
        print("• Perfect spherical symmetry around singularity")
        print("• μ shells are concentric spheres")
        print("• Volume decreases as μ³ toward center")
        print("• Surface area decreases as μ² toward center")
        print("• All change flows radially inward")
        print("• Singularity is a point where μ = 0, τ = ∞")

def main():
    """Run simple 3D black hole visualization."""
    # Create simulation
    sim = Simple3DBlackHole(mass=10*M_sun)
    
    print("🚀 Starting Simple 3D Visualization...")
    
    # 1. Create spherical shells
    print("\n🌐 Creating spherical μ shells...")
    fig1 = sim.create_spherical_shells()
    
    # 2. Plot cross-sections
    print("\n📊 Generating cross-sections...")
    fig2 = sim.plot_cross_sections_3d()
    
    # 3. Radial analysis
    print("\n📈 Creating radial analysis...")
    fig3 = sim.create_radial_analysis()
    
    # 4. Geometry analysis
    print("\n📐 Analyzing 3D geometry...")
    sim.analyze_3d_geometry()
    
    print("\n🎯 3D VISUALIZATION COMPLETE!")
    print("The Universal Change Equation μ = r/(2r_s) reveals")
    print("black holes as perfectly spherical systems with")
    print("nested shells of decreasing change flow!")

if __name__ == "__main__":
    main()