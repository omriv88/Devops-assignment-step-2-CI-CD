pipeline {
    agent {label 'AWS-DOCKER'}
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
        TEST_FILE = 'nginx_test.py'
        LOCAL_IMAGE = 'omriv/nginx'
        QA_IMAGE = 'nginx-dl-qa'
        IMAGE = 'omriv/nginx_dl:1.1'
        VERSION = '1.1'
        QA_PORT = '8080'
        PROD_PORT = '30201'
        BUILD_PORT = '8080:80'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch:'main', credentialsId: 'bfa3b3d0-d166-4cf9-b5c6-511432a4be29', url:'https://github.com/omriv88/Deploy-nginx-on-k8s-using-terraform.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t ${env.IMAGE} .'
                sh 'docker run -d -p ${env.BUILD_PORT} ${env.IMAGE}'
            }
        }
        stage('Test') {
            agent {label 'LOCAL-WIN-SERVER'}
                steps {
                    git branch:'main', credentialsId: 'bfa3b3d0-d166-4cf9-b5c6-511432a4be29', url:'https://github.com/omriv88/CI-CD-nginx.git'
                    bat 'pyhton ${env.TEST_FILE}'
            }        
        }
        stage('Push 1/2') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push 2/2') {
            steps {
                sh 'docker push ${env.LOCAL_IMAGE}'
            }
        }
        post {
            always {
                sh 'docker logout'
            }
        }
        stage('Deploy for QA') {
            steps {
                sh 'docker rm -f $(docker ps -a -q)'
                sh 'docker rmi $(docker images -a -q)'
                sh 'docker run --name ${env.QA_IMAGE} -p ${env.BUILD_PORT} -d ${env.IMAGE}'
                echo ''
            }
        }
        stage('Deploy on K8S for PROD') {
            agent {label 'LOCAL-WIN-SERVER'}
                steps {
                    git branch: 'main', credentialsId: 'bfa3b3d0-d166-4cf9-b5c6-511432a4be29', url: 'https://github.com/omriv88/Deploy-nginx-on-k8s-using-terraform.git'
                    bat 'terraform init'
                    bat 'terraform plan'
                    bat 'terraform apply --auto-approve'
            }        
        }
    }
}
