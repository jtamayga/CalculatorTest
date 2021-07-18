pipeline {
    agent none 
    stages {
        stage('Build') { 
            steps {
                sh 'python -m py_compile test_calculator.py'  
            }
        }
    }
}