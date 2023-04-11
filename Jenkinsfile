pipeline {
    agent any

    stages {
      
      
       stage('GitClone') {
            steps {
                sh 'git clone -b main 
                sh 'pwd'
                sh 'ls -an'
                echo 'Hello World'
            }
        }
      
      
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
