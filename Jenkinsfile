pipeline {
    agent any
    stages {

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
        
    }
}
