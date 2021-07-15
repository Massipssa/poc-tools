pipeline {
    agent any
    stages {

        /**
        * Install requirements and test the code
        */

        stage('Install') {
            steps {
                sh 'echo pip -V'
                sh 'pip install -r requirements/requirements.txt'
            }
        }
        stage('Test') {
             steps {
                sh 'pytest'
            }
        }

        /*
        * Run sonar analysis and checks quality gates
        */

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
        * Deploy the project to
        */
        stage('Deploy') {
            steps {
                sh 'python'
            }
        }
    }
}
