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
1. Open browser to here:  https://github.com/rbocchinfuso/di2020_clint
2. Click "Fork" in the upper right corner of the screen.
3. Clone the repo localy: "git clone https://github.com/ccfs-crhubart/di2020_clint.git"
4. chmod 755 *.sh
5. chmod 755 *.py
6. ./nuke.sh
7. Start the ghetto ci/cd process in a second terminal session (it will just sit there):  ./ghetto_cicd.py
8. Build and run your container:  ./wrapper.sh
9. Modify the README.md (later you can try to modify the mytimeback.py app)
10. Commit the changes by typing: ./commit.sh "commit message"
11. You should see the container rebuild and restart.



