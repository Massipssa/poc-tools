pipeline {
    agent any
    stages {

        stage('Build') {
            steps {
                sh 'pip install -r requirements/requirements-python3.7.txt'
            }
        }

        stage('Test') {
             steps {
                sh 'pytest'
            }
        }

        stage('SonarQube analysis') {
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
       
        stage("Quality Gate") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }

        /*
        stage('Deploy') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        */
    }
}
