pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python3 -m pytest

                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t flask-demo .
                '''
            }
        }

        stage('Remove Old Container') {
            steps {
                sh '''
                docker stop flask-demo-container || true
                docker rm flask-demo-container || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d \
                --name flask-demo-container \
                -p 5000:5000 \
                flask-demo
                '''
            }
        }
    }

    post {

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}