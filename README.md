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

1. chmod 755 *.sh
2. chmod 755 *.py
3. ./nuke.sh
4. Start the ghetto ci/cd process in a second terminal session (it will just sit there): ./ghetto_cicd.py
5. Build and run your container:  ./wrapper.sh
6. Modify the README.md (later you can try to modify the mytimeback.py app)
7. Commit the changes by typing: ./commit.sh "commit message"
8. In the terminal where you started ghetto_cicd.py you should see the container rebuild and restart.


- v5.21.1
	-Small Changes to Alert Messages
	-Updates to Readme
	

