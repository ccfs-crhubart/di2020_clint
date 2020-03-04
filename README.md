# Clint DI 2020 DevOps Project Help

## The Application
The application is the beginning of solving the Seatgeek human robot problem.

#### Files:
- Application: mytimeback.py
- Data:  file1.txt and file2.txt
-- These are snippets of switch output
- Dockerfile:  Commands to assemble the Docker container
- wrapper.sh:  Shell script to cleanup, build and deploy mytimeback.py as a containerized application
- commit.sh:  Shell script to simplify git commits
- ghetto\_cicd.py:  Process that manages the CI/CD process on git commit from commit.sh
-- For automated build an deploy this process needs to be running
-- Triggered by "touch build"

Usage:

