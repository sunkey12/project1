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

       stage('DockerBuild') {
            steps {  
                 withCredentials([usernamePassword(credentialsId: 'aws-cred', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                      sh 'echo $AWS_ACCESS_KEY_ID'
                      sh 'echo $AWS_SECRET_ACCESS_KEY'  
                      dir('project1') {
                        sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
                //        sh 'docker run -t -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY arik12/project1:${BUILD_NUMBER} cat check.txt'
                      }
                }
            }
       }
        
       stage('Dockerlogin') {
            steps {
               withCredentials([usernamePassword(credentialsId: 'docker-cred', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                      sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                      sh 'echo $DOCKERHUB_PASSWORD'
                      sh 'echo $DOCKERHUB_USERNAME'  

               }
                       
            }
       }    
       stage('DockerPush') {
            steps { 
                sh 'pwd'
                sh 'docker push  arik12/project1:${BUILD_NUMBER}'
            }
       }    
        
    }
}

