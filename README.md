# HelloActions-ZachFlorez

What is the purpose of the `on` section?  
The `on` section defines which events trigger the GitHub Actions workflow.

What does `workflow_dispatch` do?  
`workflow_dispatch` lets you to manually trigger a workflow from the GHA tab.

What does `runs-on` specify?  
`runs-on` hooks a fresh virtual host machine for the job. 

Why is `actions/checkout` needed?  
`actions/checkout` authenticates and downloads raw repo source into the sandbox environment. 

What does the language setup action do?  
Installs runtime package managers natively. 

What is the difference between compiling and running the program?  
Compiling translates source code into an executable format, while running executes the compiled program to perform its intended tasks.

Where can you see the program output?  
You can see the program output in the GitHub Actions workflow: "RUn the Python program" step if you click on the running workflow. 

What is the difference between a workflow, a job, and a step?  
A workflow is the automated process, a job is a group of tasks that run on a runner, and a step is the one task inside a job.