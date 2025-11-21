@echo off
REM Setup script for pushing Mu-Theory to GitHub (Windows)

echo 🚀 Setting up Mu-Theory Git Repository
echo ========================================

REM Initialize git if not already initialized
if not exist .git (
    echo 📦 Initializing Git repository...
    git init
) else (
    echo ✓ Git repository already initialized
)

REM Add remote
echo 🔗 Adding remote repository...
git remote add origin https://github.com/abhi9199-tech42/Mu-Theory.git 2>nul
if errorlevel 1 (
    echo ✓ Remote origin already exists
)

REM Stage all files
echo 📝 Staging files...
git add .

REM Commit
echo 💾 Creating commit...
git commit -m "Initial commit: Universal Change Theory (Mu-Theory)" -m "- Complete theoretical framework" -m "- Near-Earth time dilation simulations" -m "- Black hole singularity analysis" -m "- 3D visualizations" -m "- Full academic paper" -m "- Comprehensive documentation"

REM Push to GitHub
echo 🌐 Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo ✅ Successfully pushed to GitHub!
echo 🌟 Repository: https://github.com/abhi9199-tech42/Mu-Theory
echo.
echo Next steps:
echo 1. Visit your repository on GitHub
echo 2. Add a description and topics
echo 3. Enable GitHub Pages (optional)
echo 4. Share with the community!

pause