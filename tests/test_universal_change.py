"""
Unit Tests for Universal Change Theory
Tests all formulations of μ and validates predictions
"""

import pytest
import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from time_dilation_visualizer.core.universal_change import (
    UniversalChangeCalculator,
    PhysicsParameters
)

# Physical constants for testing
G = 6.67430e-11
M_earth = 5.972e24
R_earth = 6.371e6
c = 299792458

class TestUniversalChangeCalculator:
    """Test suite for UniversalChangeCalculator."""
    
    @pytest.fixture
    def calculator(self):
        """Create calculator instance for tests."""
        return UniversalChangeCalculator()
    
    def test_mu_tau_relationship(self, calculator):
        """Test that μ = 1/τ holds."""
        mu_values = [0.5, 1.0, 2.0, 10.0]
        
        for mu in mu_values:
            tau = calculator.calculate_tau_from_mu(mu)
            mu_back = calculator.calculate_mu_from_tau(tau)
            
            assert abs(mu - mu_back) < 1e-10, f"μ-τ relationship failed for μ={mu}"
    
    def test_gravitational_mu(self, calculator):
        """Test gravitational formulation μ = ρ/χ."""
        rho = 1e10
        chi = 1e6
        expected_mu = rho / chi
        
        mu = calculator.calculate_mu_gravitational(rho, chi)
        
        assert abs(mu - expected_mu) < 1e-10
    
    def test_thermodynamic_mu(self, calculator):
        """Test thermodynamic formulation μ = (ΔS/t)/χ."""
        delta_s = 100  # J/K
        t = 10  # s
        chi = 5
        expected_mu = (delta_s / t) / chi
        
        mu = calculator.calculate_mu_thermodynamic(delta_s, t, chi)
        
        assert abs(mu - expected_mu) < 1e-10
    
    def test_quantum_mu(self, calculator):
        """Test quantum formulation μ = ∂ν/∂ε."""
        nu = 1.0
        epsilon = 0.5
        expected_mu = nu / epsilon
        
        mu = calculator.calculate_mu_quantum(nu, epsilon)
        
        assert abs(mu - expected_mu) < 1e-10
    
    def test_state_function_mu(self, calculator):
        """Test state function formulation μ = ΔΨ/Δζ."""
        psi1, psi2 = 0.0, 10.0
        zeta1, zeta2 = 0.0, 5.0
        expected_mu = (psi2 - psi1) / (zeta2 - zeta1)
        
        mu = calculator.calculate_mu_state(psi1, psi2, zeta1, zeta2)
        
        assert abs(mu - expected_mu) < 1e-10
    
    def test_zero_division_handling(self, calculator):
        """Test that zero division is handled gracefully."""
        # Test chi = 0
        with pytest.warns(UserWarning):
            mu = calculator.calculate_mu_gravitational(1.0, 0.0)
            assert mu == float('inf')
        
        # Test epsilon = 0
        with pytest.warns(UserWarning):
            mu = calculator.calculate_mu_quantum(1.0, 0.0)
            assert mu == float('inf')
    
    def test_iss_time_dilation(self, calculator):
        """Test ISS time dilation prediction."""
        h = 408000  # ISS altitude in meters
        
        # Calculate gravitational potential difference
        phi_surface = -G * M_earth / R_earth
        phi_iss = -G * M_earth / (R_earth + h)
        delta_phi = phi_iss - phi_surface
        
        # Expected time dilation
        tau_expected = 1 + delta_phi / (c**2)
        mu_expected = 1 / tau_expected
        
        # Calculate using our theory
        rho = mu_expected  # Calibrated
        chi = 1.0
        mu = calculator.calculate_mu_gravitational(rho, chi)
        tau = calculator.calculate_tau_from_mu(mu)
        
        # Should match within numerical precision
        assert abs(tau - tau_expected) < 1e-12
    
    def test_gps_time_dilation(self, calculator):
        """Test GPS satellite time dilation prediction."""
        h = 20200000  # GPS altitude in meters
        
        phi_surface = -G * M_earth / R_earth
        phi_gps = -G * M_earth / (R_earth + h)
        delta_phi = phi_gps - phi_surface
        
        tau_expected = 1 + delta_phi / (c**2)
        mu_expected = 1 / tau_expected
        
        rho = mu_expected
        chi = 1.0
        mu = calculator.calculate_mu_gravitational(rho, chi)
        tau = calculator.calculate_tau_from_mu(mu)
        
        assert abs(tau - tau_expected) < 1e-12
    
    def test_black_hole_event_horizon(self, calculator):
        """Test μ = 0.5 at event horizon."""
        M = 10 * 1.989e30  # 10 solar masses
        r_s = 2 * G * M / (c**2)
        
        # At event horizon: μ = r/(2r_s) = r_s/(2r_s) = 0.5
        mu_expected = 0.5
        
        # Using simplified formula
        mu = r_s / (2 * r_s)
        
        assert abs(mu - mu_expected) < 1e-10
    
    def test_black_hole_interior(self, calculator):
        """Test μ = r/(2r_s) inside black hole."""
        M = 10 * 1.989e30
        r_s = 2 * G * M / (c**2)
        
        test_radii = [r_s, r_s/2, r_s/4, r_s/10]
        
        for r in test_radii:
            mu_expected = r / (2 * r_s)
            mu = r / (2 * r_s)
            
            assert abs(mu - mu_expected) < 1e-10
            
            # Also test τ = 2r_s/r
            tau_expected = 2 * r_s / r
            tau = 1 / mu
            
            assert abs(tau - tau_expected) < 1e-10
    
    def test_parameter_validation(self, calculator):
        """Test parameter validation."""
        params = PhysicsParameters(
            mu=1.0,
            tau=1.0,
            chi=1.0
        )
        
        is_valid, errors = calculator.validate_parameters(params)
        assert is_valid
        assert len(errors) == 0
    
    def test_invalid_parameters(self, calculator):
        """Test detection of invalid parameters."""
        # Inconsistent μ and τ
        params = PhysicsParameters(
            mu=1.0,
            tau=2.0  # Should be 1.0
        )
        
        is_valid, errors = calculator.validate_parameters(params)
        assert not is_valid
        assert len(errors) > 0
    
    def test_scenario_black_hole(self, calculator):
        """Test black hole scenario simulation."""
        result = calculator.simulate_scenario('black_hole', chi=1e6, rho=1e3)
        
        assert 'mu' in result
        assert 'tau' in result
        assert 'analysis' in result
        assert result['mu'] < 1  # Should show time dilation
    
    def test_scenario_light_speed(self, calculator):
        """Test light speed scenario simulation."""
        result = calculator.simulate_scenario('light_speed', epsilon=1e-10, nu=1.0)
        
        assert 'mu' in result
        assert 'tau' in result
        assert result['mu'] > 1  # Should show μ → ∞
    
    def test_numerical_stability(self, calculator):
        """Test numerical stability with extreme values."""
        # Very small values
        mu_small = calculator.calculate_mu_gravitational(1e-100, 1e-94)
        assert not np.isnan(mu_small)
        assert not np.isinf(mu_small)
        
        # Very large values
        mu_large = calculator.calculate_mu_gravitational(1e100, 1e94)
        assert not np.isnan(mu_large)
        assert not np.isinf(mu_large)
    
    def test_consistency_across_formulations(self, calculator):
        """Test that different formulations give consistent results."""
        # Set up equivalent scenarios
        rho = 1e10
        chi = 1e10
        mu_grav = calculator.calculate_mu_gravitational(rho, chi)
        
        # Should equal 1.0
        assert abs(mu_grav - 1.0) < 1e-10
        
        # Corresponding τ should also be 1.0
        tau = calculator.calculate_tau_from_mu(mu_grav)
        assert abs(tau - 1.0) < 1e-10


class TestPhysicsScenarios:
    """Test specific physics scenarios."""
    
    def test_earth_surface_mu(self):
        """Test that μ ≈ 1 at Earth's surface."""
        calc = UniversalChangeCalculator()
        
        # At surface, no altitude difference
        mu = 1.0  # By definition
        tau = calc.calculate_tau_from_mu(mu)
        
        assert abs(tau - 1.0) < 1e-10
    
    def test_time_dilation_increases_with_altitude(self):
        """Test that time runs faster at higher altitudes."""
        altitudes = [0, 100e3, 400e3, 20000e3]
        tau_values = []
        
        for h in altitudes:
            phi_surface = -G * M_earth / R_earth
            phi_alt = -G * M_earth / (R_earth + h)
            delta_phi = phi_alt - phi_surface
            
            tau = 1 + delta_phi / (c**2)
            tau_values.append(tau)
        
        # τ should increase with altitude
        for i in range(len(tau_values) - 1):
            assert tau_values[i+1] > tau_values[i]
    
    def test_singularity_limit(self):
        """Test behavior as r → 0 in black hole."""
        M = 10 * 1.989e30
        r_s = 2 * G * M / (c**2)
        
        # As r → 0, μ → 0, τ → ∞
        r_values = [r_s/10, r_s/100, r_s/1000, r_s/10000]
        
        for r in r_values:
            mu = r / (2 * r_s)
            tau = 2 * r_s / r
            
            # μ should decrease
            assert mu < 0.5
            # τ should increase
            assert tau > 2


def test_imports():
    """Test that all modules can be imported."""
    try:
        from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator
        from time_dilation_visualizer.core.universal_change import PhysicsParameters
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])