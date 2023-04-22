# Devops-assignment-step-2
Create CI CD pipeline that does the following setup:
Checkout -> build -> test -> push -> Deploy for QA environment -> Deploy for PROD - deploy your application on kubernetes cluster, use Terraform to create deployment

 - 1 stage 1 call "Checkout" - check your repositoreis
 - 2 stage 2 call "Build" - Build nginx application on container system, Change the Nginx welcome text to "<your name> is doing the assignment."
 - 3 stage 3 call "test" - do same test with any tools and checks if your changes has been setup
 - 4 stage 4 call "push" - upload your application to cloud
 - 5 stage 4 call "deploy for QA" - Deploy the application on the QA environment
 - 6 stage 5 call "Deploy for PROD" - deploy your application on kubernetes cluster, use Terraform to create deployment
 - 7 All changes should persist through kubernetes restart 
 - 8 All the system should be run as a container

![image](https://user-images.githubusercontent.com/113102456/233776122-cd159fdd-3aef-437a-a147-6b00fb9c2c83.png)
![image](https://user-images.githubusercontent.com/113102456/233776140-1c9ee4f3-49b2-45ea-b556-5f37768021f8.png)
