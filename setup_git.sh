#!/bin/bash
# Setup script for pushing Mu-Theory to GitHub

echo "🚀 Setting up Mu-Theory Git Repository"
echo "========================================"

# Initialize git if not already initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
else
    echo "✓ Git repository already initialized"
fi

# Add remote if not exists
if ! git remote | grep -q origin; then
    echo "🔗 Adding remote repository..."
    git remote add origin https://github.com/abhi9199-tech42/Mu-Theory.git
else
    echo "✓ Remote origin already exists"
fi

# Stage all files
echo "📝 Staging files..."
git add .

# Commit
echo "💾 Creating commit..."
git commit -m "Initial commit: Universal Change Theory (Mu-Theory)

- Complete theoretical framework
- Near-Earth time dilation simulations
- Black hole singularity analysis
- 3D visualizations
- Full academic paper
- Comprehensive documentation"

# Push to GitHub
echo "🌐 Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Successfully pushed to GitHub!"
echo "🌟 Repository: https://github.com/abhi9199-tech42/Mu-Theory"
echo ""
echo "Next steps:"
echo "1. Visit your repository on GitHub"
echo "2. Add a description and topics"
echo "3. Enable GitHub Pages (optional)"
echo "4. Share with the community!"