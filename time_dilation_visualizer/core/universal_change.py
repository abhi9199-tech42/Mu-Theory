"""
Universal Change Calculator
Implements: μ = ∂ν/∂ε = ΔΨ/Δζ = (ΔS/t)/χ = ρ/χ = 1/τ
"""

import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
import warnings


@dataclass
class PhysicsParameters:
    """Container for all physics parameters across domains."""
    # Quantum domain
    nu: Optional[float] = None  # Observable change state
    epsilon: Optional[float] = None  # Perturbation input
    
    # State function domain  
    psi: Optional[float] = None  # State function
    zeta: Optional[float] = None  # Entropy interaction space
    
    # Thermodynamic domain
    delta_s: Optional[float] = None  # Entropy change
    t: Optional[float] = None  # Time
    chi: Optional[float] = None  # Resistance to change
    
    # Gravitational domain
    rho: Optional[float] = None  # Energy density
    
    # Universal
    mu: Optional[float] = None  # Change flow rate
    tau: Optional[float] = None  # Time dilation factor


class UniversalChangeCalculator:
    """
    Core calculator implementing the universal change equation across all physics domains.
    """
    
    def __init__(self):
        self.tolerance = 1e-10  # For handling near-zero values
        
    def calculate_mu_quantum(self, nu: float, epsilon: float) -> float:
        """
        Calculate μ = ∂ν/∂ε for quantum scenarios.
        
        Args:
            nu: Observable change state (quantum transitions)
            epsilon: Perturbation/interaction input
            
        Returns:
            Change flow rate μ
        """
        if abs(epsilon) < self.tolerance:
            warnings.warn("Epsilon approaching zero - quantum uncertainty limit")
            return float('inf') if nu > 0 else 0.0
            
        return nu / epsilon
    
    def calculate_mu_state(self, psi1: float, psi2: float, 
                          zeta1: float, zeta2: float) -> float:
        """
        Calculate μ = ΔΨ/Δζ for state function changes.
        
        Args:
            psi1, psi2: Initial and final state function values
            zeta1, zeta2: Initial and final entropy interaction space values
            
        Returns:
            Change flow rate μ
        """
        delta_psi = psi2 - psi1
        delta_zeta = zeta2 - zeta1
        
        if abs(delta_zeta) < self.tolerance:
            warnings.warn("Delta zeta approaching zero - state change singularity")
            return float('inf') if delta_psi > 0 else 0.0
            
        return delta_psi / delta_zeta
    
    def calculate_mu_thermodynamic(self, delta_s: float, t: float, chi: float) -> float:
        """
        Calculate μ = (ΔS/t)/χ for thermodynamic scenarios.
        
        Args:
            delta_s: Entropy change (J/K)
            t: Time (subordinate to μ)
            chi: Resistance to change
            
        Returns:
            Change flow rate μ
        """
        if abs(chi) < self.tolerance:
            warnings.warn("Chi approaching zero - no resistance to change")
            return float('inf')
            
        if abs(t) < self.tolerance:
            warnings.warn("Time approaching zero - instantaneous change")
            return float('inf') if delta_s != 0 else 0.0
            
        entropy_rate = delta_s / t
        return entropy_rate / chi
    
    def calculate_mu_gravitational(self, rho: float, chi: float) -> float:
        """
        Calculate μ = ρ/χ for gravitational scenarios.
        
        Args:
            rho: Energy density or internal state property
            chi: Resistance to change
            
        Returns:
            Change flow rate μ
        """
        if abs(chi) < self.tolerance:
            warnings.warn("Chi approaching zero - gravitational singularity")
            return float('inf')
            
        return rho / chi
    
    def calculate_tau_from_mu(self, mu: float) -> float:
        """
        Calculate τ = 1/μ (time dilation from change flow rate).
        
        Args:
            mu: Change flow rate
            
        Returns:
            Time dilation factor τ
        """
        if abs(mu) < self.tolerance:
            warnings.warn("Mu approaching zero - time dilation approaching infinity")
            return float('inf')
            
        return 1.0 / mu
    
    def calculate_mu_from_tau(self, tau: float) -> float:
        """
        Calculate μ = 1/τ (change flow rate from time dilation).
        
        Args:
            tau: Time dilation factor
            
        Returns:
            Change flow rate μ
        """
        if abs(tau) < self.tolerance:
            warnings.warn("Tau approaching zero - change flow approaching infinity")
            return float('inf')
            
        return 1.0 / tau
    
    def simulate_scenario(self, scenario: str, **params) -> Dict:
        """
        Simulate specific physics scenarios with predefined parameter relationships.
        
        Args:
            scenario: One of 'black_hole', 'light_speed', 'quantum_vacuum', 'universe_expansion'
            **params: Scenario-specific parameters
            
        Returns:
            Dictionary with calculated values and analysis
        """
        results = {'scenario': scenario, 'parameters': params}
        
        if scenario == 'black_hole':
            # χ → ∞, ρ → extreme ⇒ μ → 0 ⇒ τ → ∞
            chi = params.get('chi', 1e6)  # Very large resistance
            rho = params.get('rho', 1e3)  # High energy density
            mu = self.calculate_mu_gravitational(rho, chi)
            tau = self.calculate_tau_from_mu(mu)
            results.update({'mu': mu, 'tau': tau, 'analysis': 'Time stops at singularity'})
            
        elif scenario == 'light_speed':
            # μ → ∞ ⇒ τ → 0 (no proper time for photons)
            epsilon = params.get('epsilon', 1e-10)  # Very small perturbation
            nu = params.get('nu', 1.0)  # Observable change
            mu = self.calculate_mu_quantum(nu, epsilon)
            tau = self.calculate_tau_from_mu(mu)
            results.update({'mu': mu, 'tau': tau, 'analysis': 'Light experiences no time'})
            
        elif scenario == 'quantum_vacuum':
            # Virtual particle creation/annihilation
            psi1, psi2 = params.get('psi_range', (0.0, 1.0))
            zeta1, zeta2 = params.get('zeta_range', (0.0, 0.1))
            mu = self.calculate_mu_state(psi1, psi2, zeta1, zeta2)
            tau = self.calculate_tau_from_mu(mu)
            results.update({'mu': mu, 'tau': tau, 'analysis': 'Vacuum fluctuation dynamics'})
            
        elif scenario == 'universe_expansion':
            # Cosmic field changes over cosmic scales
            delta_s = params.get('delta_s', 1e23)  # Cosmic entropy change
            t = params.get('t', 1e17)  # Cosmic time scale
            chi = params.get('chi', 1e6)  # Cosmic resistance
            mu = self.calculate_mu_thermodynamic(delta_s, t, chi)
            tau = self.calculate_tau_from_mu(mu)
            results.update({'mu': mu, 'tau': tau, 'analysis': 'Cosmic expansion dynamics'})
            
        return results
    
    def validate_parameters(self, params: PhysicsParameters) -> Tuple[bool, List[str]]:
        """
        Validate physics parameters for consistency and physical meaning.
        
        Args:
            params: PhysicsParameters object
            
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        
        # Check for negative values where inappropriate
        if params.epsilon is not None and params.epsilon < 0:
            errors.append("Epsilon (perturbation) should be positive")
            
        if params.chi is not None and params.chi <= 0:
            errors.append("Chi (resistance to change) must be positive")
            
        if params.t is not None and params.t <= 0:
            errors.append("Time must be positive")
            
        if params.rho is not None and params.rho < 0:
            errors.append("Energy density (rho) should be non-negative")
            
        # Check for consistency between mu and tau
        if params.mu is not None and params.tau is not None:
            expected_tau = 1.0 / params.mu if params.mu != 0 else float('inf')
            if abs(params.tau - expected_tau) > self.tolerance:
                errors.append("Mu and tau are inconsistent (τ ≠ 1/μ)")
        
        return len(errors) == 0, errors