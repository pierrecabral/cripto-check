pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Actual State:'
                sh 'docker ps'
                echo 'Building docker image...'
                sh 'ls -la'
                sh 'docker build -t cripto-check .'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker images'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Removing old deployment...'
                sh 'docker-compose down'
                echo 'Deploying new image...'
                sh 'docker-compose up -d'
            }
        }
        stage('Verify') {
            steps {
                echo 'Verifying....'
                sh 'docker inspect cripto-check'
            }
        }
    }
}
