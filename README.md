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

How To:

1. ./nuke.sh
2. Start the ghetto ci/cd process in a second terminal session (it will just sit there): ./ghetto_cicd.py
3. Build and run your container:  ./wrapper.sh
4. Modify the README.md (or modify the mytimeback.py app)
5. Commit the changes by typing: ./commit.sh "commit message"
6. In the terminal where you started ghetto_cicd.py you should see the container rebuild and restart.


- v5.21.1
	-Small Changes to Alert Messages
	-Updates to Readme
- v5.21.2
	-Updates to Readme
- v5.21.3
	-Updates to Readme