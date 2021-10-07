pipeline {
    agent {
        label 'windowsnode'
    }
    
    stages {
        stage('clone git') {
            steps {
                git 'https://github.com/ayomodu/flashapp.git'
            }
        }
        stage('build image') {
            steps {
                script {
                    newImage = docker.build("ayomodu/flashapp:${env.BUILD_ID}")
                }
            }
        }
        stage('push to dockerhub') {
            steps {
                script{
                    docker.withRegistry('', 'ayomodu') {
                    newImage.push('latest')
                        
                    }

                }
            }
        }
        stage('run container locally') {
            steps {
                bat 'docker run -d -p 5000:5000 --name newlay ayomodu/flashapp:latest'
            }
        }
    }
}
