# Password-Generation-Service

Project Structure

The project involves building a Password generator in flask microservices. It has 4 services which described below:
-
Service One - This is responsible for rendering jinja template (frontend part) to interact with user
-
Service Two - Responsible for handling number of digits for password length
-
Service Three - Responsible for handling characters for the password
-
Service Four - Combine service two and service three to generate a strong password

The requirements set by QA Academy:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.

* Feature-Branch model into a Version Control System to be applied.

* User CI server and deploy the project to a cloud-based virtual machine.

* User Webhooks such as Jenkins to recreate and redeploy the changed application

* Follow Service-oriented architecture.

* Deploy the project using containerisation and an orchestration tool.

* Create an Ansible Playbook that will provision the environment of the project.

* Reverse proxy to make your application accessible to the user.

# Proposal
I've decided to come up with the project which involves building a Password generator in flask microservices. It has 4 services which described below:
-
Service One - This is responsible for rendering jinja template (frontend part) to interact with user
-
Service Two - Responsible for handling number of digits for password length
-
Service Three - Responsible for handling characters for the password
-
Service Four - Combine service two and service three to generate a strong password

## Architecture
# Risk Assessment
The risk assessment below highlights the potential risks that would prevent me from completing the project. I find it extremely important to have a plan when dealing with difficult situations and luckily - none of the risks were something I've been dealing with by the end of the project. I always like to think about the technical risks as well as enviromental ones.
![](LINK OF THE IMAGE HERE)







# Planning Board (GITBOOK)
Can be seen here: (GITBOOK LINK )
I've chosen Trello because it's very quick and easy to use.

# Testing
I've managed to achieve 97% coverage using pytest for unit testing and all of my tests were ran by Jenkins.
The test in Service 1 is a mock test that inputs variables that would have been generated by service 2, 3 and 4 together.
The rest tests whether correct things have been generated and the status codes of the server.
![](Jenkins SCREENSHOT )

## Infrastructure

* Jenkins
I've used Jenkins to automate my deployment and therefore reduce the time it takes from development to actually deploying the application. Whenever a push is made to my Dev branch on github, Jenkins runs the whole job for me and quickly updates the page of my application using a webhook.
![](PIPELINE SCREENSHOT )

The Jenkins pipeline is as follows:
* Installing Dependencies.
* Tests using Pytest together with detailed logs.
* Build images using Docker-compose while handing the DockerHub credentials.
* VM configuration - Ansible - Setting up the swarm by generating the join tokens on manager VM for the worker VM, and also setting up my NGINX as the load balancer.
* Deployment using docker-compose.yaml

![](https://i.imgur.com/kPRMgqJ.png)



# Interactions
![](https://i.imgur.com/88EDeGm.png)
I've orchestrated a network of virtual machines using docker swarm that are all able to communicate with each other.
The list of virtual machiens:
* Load Balancer
* Manager
* Worker
I've also had a Jenkins VM that was communicating with my Github using a webhook and a Development VM where I've made all the pushes from therefore sending my code to Jenkins and triggering a build.



## Application

# Front-End
When navigating to the load balancer IP on port 80, your character will be generated as mentioned above.
I've used HTML and a CSS bootstrap to display the returned outcome of my applications together.

* ![](SCREENSHOT OF FRONTEND)












