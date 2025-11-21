"""
Time Dilation Visualizer - Universal Change Equation Implementation
μ = ∂ν/∂ε = ΔΨ/Δζ = (ΔS/t)/χ = ρ/χ = 1/τ

A comprehensive physics simulation tool for exploring time dilation
across quantum, thermodynamic, gravitational, and cosmological domains.
"""

__version__ = "1.0.0"
__author__ = "Physics Research Team"

from .core.universal_change import UniversalChangeCalculator
from .physics.quantum import QuantumDomain
from .physics.thermodynamic import ThermodynamicDomain
from .physics.gravitational import GravitationalDomain
from .visualization.plotter import PhysicsPlotter
from .interactive.controller import InteractiveController

__all__ = [
    'UniversalChangeCalculator',
    'QuantumDomain',
    'ThermodynamicDomain', 
    'GravitationalDomain',
    'PhysicsPlotter',
    'InteractiveController'
]