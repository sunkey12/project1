pipeline {
    agent any

    stages {
      
      
       stage('GitClone') {
            steps {
                sh 'git clone -b main https://github.com/sunkey12/project1.git'
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
