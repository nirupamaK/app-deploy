# Required Tols 
* Docker for contanierzing applications
* Jenkins for CI & CD pipeline
* python3.6
* pytest for running test cases.

# Instruction to deploy app-deploy
* A multi container application to deploy backend-challenge.
* The backed-challenge repository to */root/app-deploy* location on local VM.
* To verify whole deployment, test stage, and teardown is configured via my-test-pipeline jenkins script.
* The my-test-pipeline jenkins script runs wholw deployment on local VM only.
* It is necessary to add jenkins user in sudoers file on jenkins server.
* The file docker-compose.yml can be user deploy application. However as of now not user by jenkins pipeline.
