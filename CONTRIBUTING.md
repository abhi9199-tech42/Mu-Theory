# Contributing to Mu-Theory

Thank you for your interest in contributing to Mu-Theory! This project aims to advance our understanding of fundamental physics through the Universal Change Framework.

## 🌟 How to Contribute

### Areas of Contribution

1. **Theoretical Development**
   - Mathematical derivations
   - New physics domain applications
   - Theoretical extensions

2. **Computational Simulations**
   - New simulation scenarios
   - Performance optimizations
   - Visualization improvements

3. **Experimental Validation**
   - Experimental protocol design
   - Data analysis methods
   - Comparison with observations

4. **Documentation**
   - Code documentation
   - Tutorial creation
   - Paper improvements

5. **Code Quality**
   - Bug fixes
   - Test coverage
   - Code refactoring

## 🚀 Getting Started

### 1. Fork the Repository

```bash
git clone https://github.com/abhi9199-tech42/Mu-Theory.git
cd Mu-Theory
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

- Follow Python PEP 8 style guidelines
- Add docstrings to all functions
- Include comments for complex logic
- Write tests for new features

### 4. Test Your Changes

```bash
# Run existing simulations to ensure nothing breaks
python refined_earth_sim.py
python black_hole_simulation.py
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of your changes"
```

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 📝 Code Style

### Python Guidelines

```python
def calculate_mu_gravitational(rho: float, chi: float) -> float:
    """
    Calculate change flow rate using gravitational formulation.
    
    Args:
        rho: Energy density (kg/m³)
        chi: Resistance to change (dimensionless)
        
    Returns:
        Change flow rate μ
        
    Example:
        >>> mu = calculate_mu_gravitational(1e10, 1e6)
        >>> print(f"μ = {mu:.6e}")
    """
    if abs(chi) < 1e-15:
        raise ValueError("Chi cannot be zero")
    
    return rho / chi
```

### Documentation Standards

- Use clear, descriptive variable names
- Include type hints
- Write comprehensive docstrings
- Add inline comments for complex logic
- Provide usage examples

## 🧪 Testing

### Running Tests

```bash
# Run all simulations
python -m pytest tests/

# Run specific test
python test_universal_change.py
```

### Writing Tests

```python
def test_mu_calculation():
    """Test μ calculation for known values."""
    calc = UniversalChangeCalculator()
    
    # Test at event horizon
    mu = calc.calculate_mu_gravitational(rho=1e10, chi=1e10)
    assert abs(mu - 1.0) < 1e-10
    
    # Test edge cases
    with pytest.raises(ValueError):
        calc.calculate_mu_gravitational(rho=1.0, chi=0.0)
```

## 📚 Documentation

### Adding Documentation

1. **Code Documentation**: Use docstrings
2. **README Updates**: Keep README.md current
3. **Theory Papers**: Update academic papers for theoretical changes
4. **Examples**: Add usage examples for new features

### Documentation Format

```markdown
## Feature Name

### Overview
Brief description of the feature.

### Usage
```python
# Example code
result = function_name(parameters)
```

### Parameters
- `param1`: Description
- `param2`: Description

### Returns
Description of return value

### Example
Complete working example
```

## 🐛 Reporting Bugs

### Bug Report Template

```markdown
**Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Run script X
2. With parameters Y
3. Observe error Z

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10]
- Python version: [e.g., 3.10]
- Mu-Theory version: [e.g., 1.0.0]

**Additional Context**
Any other relevant information
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed?

**Proposed Implementation**
How might this be implemented?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Any other relevant information
```

## 🔬 Research Contributions

### Theoretical Contributions

If you're contributing theoretical work:

1. Provide mathematical derivations
2. Show connection to existing μ formulations
3. Include physical interpretation
4. Suggest experimental tests
5. Update relevant documentation

### Experimental Proposals

If you're proposing experiments:

1. Clear hypothesis statement
2. Detailed experimental protocol
3. Expected results
4. Required equipment/resources
5. Data analysis methods

## 📊 Simulation Contributions

### Adding New Simulations

1. Create simulation script in appropriate directory
2. Follow existing naming conventions
3. Include comprehensive comments
4. Add visualization if applicable
5. Document results in README
6. Update main documentation

### Simulation Template

```python
"""
Simulation Name
Brief description of what this simulates

Using Universal Change Equation: μ = ...
"""

import numpy as np
from time_dilation_visualizer.core.universal_change import UniversalChangeCalculator

class YourSimulation:
    """Simulation class description."""
    
    def __init__(self, parameters):
        """Initialize simulation with parameters."""
        self.calc = UniversalChangeCalculator()
        # Setup code
    
    def run_simulation(self):
        """Run the simulation."""
        # Simulation code
        pass
    
    def analyze_results(self):
        """Analyze and display results."""
        # Analysis code
        pass

def main():
    """Run simulation."""
    sim = YourSimulation(parameters)
    sim.run_simulation()
    sim.analyze_results()

if __name__ == "__main__":
    main()
```

## 🤝 Code Review Process

### What We Look For

1. **Correctness**: Does it work as intended?
2. **Clarity**: Is the code readable?
3. **Documentation**: Is it well-documented?
4. **Testing**: Are there appropriate tests?
5. **Performance**: Is it efficient?
6. **Style**: Does it follow conventions?

### Review Timeline

- Initial review: Within 1 week
- Follow-up: Within 3 days
- Merge: After approval from maintainers

## 📞 Communication

### Getting Help

- **GitHub Issues**: For bugs and features
- **Discussions**: For questions and ideas
- **Email**: For private inquiries

### Community Guidelines

- Be respectful and constructive
- Focus on ideas, not individuals
- Welcome newcomers
- Share knowledge generously
- Acknowledge contributions

## 🎯 Priority Areas

Current priority areas for contribution:

1. **Experimental Validation**: Design testable experiments
2. **Quantum Field Theory**: Integrate with QFT
3. **Cosmological Applications**: Universe expansion models
4. **Visualization**: Interactive 3D visualizations
5. **Performance**: Optimize large-scale simulations

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

All contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in relevant papers
- Credited in release notes

Thank you for helping advance Mu-Theory! 🌌✨