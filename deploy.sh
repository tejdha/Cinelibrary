#!/bin/bash
echo "Starting deployment process..."

# Stage changes
git add .

# Commit changes with an automated message
git commit -m "${1:-Automated deployment: $(date +'%Y-%m-%d %H:%M:%S')}"

# Push changes to your GitHub repository
git push origin main

echo "Deployment process complete!"
