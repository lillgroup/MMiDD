#!/bin/bash

# MMiDD Environment Setup Script
# This script clones the MMiDD repository and sets up a selected micromamba environment
# for the Molecular Modelling in Drug Design course.

# Exit immediately if any command fails
set -e

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_prompt() {
    echo -e "${BLUE}[INPUT]${NC} $1"
}

# Print welcome message
echo "==============================================="
echo "  MMiDD Environment Setup Script"
echo "  Molecular Modelling in Drug Design"
echo "==============================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "git is not installed. Please install git first."
    print_info "Visit: https://git-scm.com/downloads"
    exit 1
fi

# Check if micromamba is installed
if ! command -v micromamba &> /dev/null; then
    print_error "micromamba is not installed. Please install micromamba first."
    print_info "Visit: https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html"
    exit 1
fi

print_success "Prerequisites check passed (git and micromamba are installed)"
echo ""

# Remove existing MMiDD folder if it exists
if [ -d "MMiDD" ]; then
    print_warning "MMiDD directory already exists. Removing it..."
    rm -rf MMiDD
    print_success "Existing directory removed"
fi

# Clone the repository into MMiDD folder
print_info "Step 1/3: Cloning MMiDD repository..."
git clone https://github.com/lillgroup/MMiDD MMiDD
print_success "Repository cloned successfully into MMiDD/"
echo ""

# Change to MMiDD directory
cd MMiDD

# List available environment files
print_info "Step 2/3: Discovering available environments..."
echo ""
echo "Available environments:"
echo "-----------------------------------------------"

# Find all .yml files in environments directory and store them in an array
mapfile -t env_files < <(find environments -name "*.yml" -type f | sort)

# Check if any environment files were found
if [ ${#env_files[@]} -eq 0 ]; then
    print_error "No environment files found in environments/ directory"
    exit 1
fi

# Display the environments with indices
for i in "${!env_files[@]}"; do
    env_file="${env_files[$i]}"
    env_name=$(basename "$env_file" .yml)
    echo "  [$i] $env_name"
    echo "      File: $env_file"
done

echo "-----------------------------------------------"
echo ""

# Prompt user to select an environment
print_prompt "Enter the number of the environment you want to install (0-$((${#env_files[@]}-1))):"
read -r selection

# Validate the selection
if ! [[ "$selection" =~ ^[0-9]+$ ]] || [ "$selection" -lt 0 ] || [ "$selection" -ge ${#env_files[@]} ]; then
    print_error "Invalid selection. Please enter a number between 0 and $((${#env_files[@]}-1))"
    exit 1
fi

# Get the selected environment file
selected_env_file="${env_files[$selection]}"
selected_env_name=$(basename "$selected_env_file" .yml)

echo ""
print_info "Step 3/3: Creating environment '$selected_env_name'..."

# Check if environment already exists and remove it
if micromamba env list | grep -q "$selected_env_name"; then
    print_warning "Environment '$selected_env_name' already exists. Removing it..."
    micromamba env remove -n "$selected_env_name" -y
    print_success "Existing environment removed"
fi

# Create the selected environment
micromamba env create -y -f "$selected_env_file"
print_success "Environment '$selected_env_name' created successfully"
echo ""

# Final success message
echo "==============================================="
print_success "Setup completed successfully!"
echo "==============================================="
echo ""
print_info "Repository location: $(pwd)"
print_info "Environment created: $selected_env_name"
echo ""
print_info "Next steps:"
echo "  1. Navigate to the repository: cd MMiDD"
echo "  2. Activate the environment: micromamba activate $selected_env_name"
echo "  3. Start working on your course materials!"
echo ""
print_info "To deactivate the environment later: micromamba deactivate"
print_info "To list all environments: micromamba env list"
echo ""
print_success "Happy modelling! 🧬"
