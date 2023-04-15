pipeline {
    agent any

    stages {
      
      
       stage('GitClone') {
            steps {
                cleanWs()
                sh 'ls -an'
                sh 'git clone -b main https://github.com/sunkey12/project1.git'
                sh 'pwd'
                sh 'ls -an'
                echo 'Clone Completed'
            }
        }    

       stage('aws2') {
            steps {  
                withAWS(credentials: 'aws-cred', region: 'us-east-1')
//                 withCredentials([usernamePassword(credentialsId: 'aws-cred', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
//                      sh 'echo $AWS_ACCESS_KEY_ID'
//                      sh 'echo $AWS_SECRET_ACCESS_KEY'  
                }
            }
       }
        
        stage('RunDockerFile') {
            steps {
                script {
                    sh 'pwd'
                    sh 'ls -l'
                    sh 'docker --version'
                    sh  'echo ${BUILD_NUMBER}'
                    dir('project1') {
                        sh 'pwd'
    	                sh 'ls -l'
                        
                        sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
                        sh 'docker run -t arik12/project1:${BUILD_NUMBER}'

                       // sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
                    }
                }
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
