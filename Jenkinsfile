pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jtamayga/CalculatorTest.git']]])
            }
        }
        stage('Build'){
            steps {
                git branch: 'main', url: 'https://github.com/jtamayga/CalculatorTest.git'
                sh 'python calculator.py'
            }
        }
        stage('Static Code Analysis'){
            steps {
                withSonarQubeEnv('SonarQube'){
                    sh "${scannerHome}/opt/sonar-scanner/"
                }
            }
        }
        stage('Quality Gate'){
            steps {
                timeout(time: 1, unit: ‘MINUTES’) {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}

