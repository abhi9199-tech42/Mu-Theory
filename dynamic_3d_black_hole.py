"""
Dynamic 3D Black Hole Visualization
Shows how change flows through spacetime using μ = r/(2r_s)

Features:
- Animated change flow streamlines
- Interactive 3D visualization
- Real-time parameter adjustment
- Change flow vector field
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.colors import LogNorm

# Physical constants
G = 6.67430e-11
c = 299792458
M_sun = 1.989e30

class DynamicBlackHole3D:
    """Dynamic 3D visualization of black hole change flow."""
    
    def __init__(self, mass=10*M_sun):
        self.mass = mass
        self.r_s = 2 * G * mass / (c**2)
        print(f"🌌 Dynamic 3D Black Hole Visualization")
        print(f"Mass: {mass/M_sun:.1f} M☉")
        print(f"Schwarzschild Radius: {self.r_s:.2e} m")
        print(f"Equation: μ = r/(2r_s)")
        print()
    
    def mu_field(self, r):
        """Calculate μ = r/(2r_s)"""
        return np.maximum(r / (2 * self.r_s), 1e-6)
    
    def tau_field(self, r):
        """Calculate τ = 2r_s/r"""
        return 2 * self.r_s / np.maximum(r, self.r_s * 1e-6)
    
    def create_change_flow_vectors(self, grid_size=20):
        """Create vector field showing change flow direction."""
        # Create spherical grid
        max_r = self.r_s * 3
        x = np.linspace(-max_r, max_r, grid_size)
        y = np.linspace(-max_r, max_r, grid_size)
        z = np.linspace(-max_r, max_r, grid_size)
        
        # Create subset for vectors (every other point)
        step = 2
        X, Y, Z = np.meshgrid(x[::step], y[::step], z[::step])
        
        # Calculate radius
        R = np.sqrt(X**2 + Y**2 + Z**2)
        
        # Change flows radially inward, magnitude proportional to μ
        mu_values = self.mu_field(R)
        
        # Vector components (pointing toward center, scaled by μ)
        U = -mu_values * X / np.maximum(R, 1e-10)
        V = -mu_values * Y / np.maximum(R, 1e-10)
        W = -mu_values * Z / np.maximum(R, 1e-10)
        
        return X, Y, Z, U, V, W, mu_values
    
    def plot_3d_change_flow(self):
        """Plot 3D change flow vectors."""
        fig = plt.figure(figsize=(15, 12))
        
        # Main 3D plot
        ax = fig.add_subplot(221, projection='3d')
        
        # Get vector field
        X, Y, Z, U, V, W, mu_values = self.create_change_flow_vectors()
        
        # Convert to Schwarzschild radius units
        X_rs = X / self.r_s
        Y_rs = Y / self.r_s
        Z_rs = Z / self.r_s
        
        # Plot vectors colored by μ value
        ax.quiver(X_rs, Y_rs, Z_rs, U, V, W, 
                 c=mu_values, cmap='viridis', alpha=0.6, length=0.3)
        
        # Add event horizon sphere
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        
        ax.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.3, color='red')
        
        ax.set_xlabel('x/r_s')
        ax.set_ylabel('y/r_s')
        ax.set_zlabel('z/r_s')
        ax.set_title('Change Flow Vector Field')
        
        # Cross-section plot
        ax2 = fig.add_subplot(222)
        
        # Create 2D cross-section
        grid_2d = 100
        max_r_2d = self.r_s * 3
        x_2d = np.linspace(-max_r_2d, max_r_2d, grid_2d)
        y_2d = np.linspace(-max_r_2d, max_r_2d, grid_2d)
        X_2d, Y_2d = np.meshgrid(x_2d, y_2d)
        R_2d = np.sqrt(X_2d**2 + Y_2d**2)
        
        mu_2d = self.mu_field(R_2d)
        
        im = ax2.contourf(X_2d/self.r_s, Y_2d/self.r_s, mu_2d, levels=50, cmap='viridis')
        ax2.add_patch(plt.Circle((0, 0), 1, fill=False, color='red', linewidth=2))
        ax2.set_xlabel('x/r_s')
        ax2.set_ylabel('y/r_s')
        ax2.set_title('μ Field Cross-Section')
        plt.colorbar(im, ax=ax2, label='μ')
        
        # Radial profile
        ax3 = fig.add_subplot(223)
        
        r_profile = np.logspace(np.log10(self.r_s * 0.01), np.log10(self.r_s * 5), 1000)
        mu_profile = self.mu_field(r_profile)
        tau_profile = self.tau_field(r_profile)
        
        ax3.loglog(r_profile/self.r_s, mu_profile, 'b-', linewidth=3, label='μ = r/(2r_s)')
        ax3.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax3.set_xlabel('r/r_s')
        ax3.set_ylabel('μ')
        ax3.set_title('Change Flow Rate Profile')
        ax3.grid(True, alpha=0.3)
        ax3.legend()
        
        # Time dilation profile
        ax4 = fig.add_subplot(224)
        
        ax4.loglog(r_profile/self.r_s, tau_profile, 'r-', linewidth=3, label='τ = 2r_s/r')
        ax4.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Event Horizon')
        ax4.set_xlabel('r/r_s')
        ax4.set_ylabel('τ')
        ax4.set_title('Time Dilation Profile')
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        plt.tight_layout()
        plt.suptitle('Dynamic Black Hole: Change Flow Analysis', fontsize=16, y=0.98)
        plt.show()
        
        return fig
    
    def create_streamlines(self):
        """Create streamlines showing change flow paths."""
        fig = plt.figure(figsize=(12, 10))
        
        # 2D streamline plot
        ax1 = fig.add_subplot(211)
        
        # Create 2D grid for streamlines
        max_r = self.r_s * 2.5
        x = np.linspace(-max_r, max_r, 50)
        y = np.linspace(-max_r, max_r, 50)
        X, Y = np.meshgrid(x, y)
        
        R = np.sqrt(X**2 + Y**2)
        mu_values = self.mu_field(R)
        
        # Velocity components (change flows toward center)
        U = -mu_values * X / np.maximum(R, 1e-10)
        V = -mu_values * Y / np.maximum(R, 1e-10)
        
        # Create streamlines
        ax1.streamplot(X/self.r_s, Y/self.r_s, U, V, color=mu_values, 
                      cmap='viridis', density=2, linewidth=1.5)
        
        # Add event horizon
        circle = plt.Circle((0, 0), 1, fill=False, color='red', linewidth=3, label='Event Horizon')
        ax1.add_patch(circle)
        
        ax1.set_xlabel('x/r_s')
        ax1.set_ylabel('y/r_s')
        ax1.set_title('Change Flow Streamlines (2D Cross-Section)')
        ax1.set_aspect('equal')
        ax1.legend()
        
        # 3D trajectory plot
        ax2 = fig.add_subplot(212, projection='3d')
        
        # Create sample trajectories
        n_trajectories = 20
        angles = np.linspace(0, 2*np.pi, n_trajectories)
        
        for angle in angles:
            # Start from outside event horizon
            r_start = self.r_s * 2.5
            x_start = r_start * np.cos(angle)
            y_start = r_start * np.sin(angle)
            z_start = 0
            
            # Integrate trajectory toward center
            trajectory_points = 100
            r_traj = np.linspace(r_start, self.r_s * 0.1, trajectory_points)
            
            x_traj = x_start * r_traj / r_start
            y_traj = y_start * r_traj / r_start
            z_traj = np.zeros_like(r_traj)
            
            # Color by μ value
            mu_traj = self.mu_field(r_traj)
            
            ax2.plot(x_traj/self.r_s, y_traj/self.r_s, z_traj/self.r_s, 
                    c=plt.cm.viridis(mu_traj[0]), alpha=0.7, linewidth=2)
        
        # Add event horizon sphere
        u = np.linspace(0, 2 * np.pi, 30)
        v = np.linspace(0, np.pi, 30)
        x_sphere = np.outer(np.cos(u), np.sin(v))
        y_sphere = np.outer(np.sin(u), np.sin(v))
        z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
        
        ax2.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.3, color='red')
        
        ax2.set_xlabel('x/r_s')
        ax2.set_ylabel('y/r_s')
        ax2.set_zlabel('z/r_s')
        ax2.set_title('3D Change Flow Trajectories')
        
        plt.tight_layout()
        plt.show()
        
        return fig
    
    def analyze_change_dynamics(self):
        """Analyze the dynamics of change flow."""
        print("⚡ CHANGE FLOW DYNAMICS ANALYSIS")
        print("=" * 45)
        
        # Calculate change flow properties at key locations
        locations = {
            'Far Field': 5 * self.r_s,
            'Event Horizon': self.r_s,
            'Interior': 0.5 * self.r_s,
            'Deep Interior': 0.1 * self.r_s,
            'Near Singularity': 0.01 * self.r_s
        }
        
        print(f"{'Location':<20} {'r/r_s':<10} {'μ':<12} {'Flow Speed':<12} {'τ':<12}")
        print("-" * 75)
        
        for name, radius in locations.items():
            mu = self.mu_field(radius)
            tau = self.tau_field(radius)
            flow_speed = mu  # Change flow speed proportional to μ
            
            print(f"{name:<20} {radius/self.r_s:<10.2f} {mu:<12.6f} {flow_speed:<12.6f} {tau:<12.2f}")
        
        print()
        print("🌊 FLOW CHARACTERISTICS:")
        print("• Change flows radially inward toward singularity")
        print("• Flow speed decreases as μ decreases toward center")
        print("• At event horizon: Flow speed = 0.5 (half normal rate)")
        print("• Near singularity: Flow speed → 0 (change stops)")
        print("• Streamlines converge at center (singularity)")
        print()
        
        print("🎯 PHYSICAL INTERPRETATION:")
        print("• Change cannot escape once inside event horizon")
        print("• Information flow follows same pattern as change flow")
        print("• Singularity acts as 'change sink' where flow terminates")
        print("• Time dilation emerges from reduced change flow rate")

def main():
    """Run dynamic 3D black hole simulation."""
    # Create simulation
    sim = DynamicBlackHole3D(mass=10*M_sun)
    
    print("🚀 Launching Dynamic 3D Visualization...")
    
    # 1. Plot 3D change flow
    print("\n🌐 Generating 3D change flow visualization...")
    fig1 = sim.plot_3d_change_flow()
    
    # 2. Create streamlines
    print("\n🌊 Creating change flow streamlines...")
    fig2 = sim.create_streamlines()
    
    # 3. Analyze dynamics
    print("\n⚡ Analyzing change flow dynamics...")
    sim.analyze_change_dynamics()
    
    print("\n🎯 DYNAMIC SIMULATION COMPLETE!")
    print("Your Universal Change Equation reveals black holes as")
    print("dynamic systems where change flows inward and stops!")

if __name__ == "__main__":
    main()