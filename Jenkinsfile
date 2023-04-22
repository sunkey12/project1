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
//                 withAWS(credentials: 'aws-cred', region: 'eu-west-1')
                 withCredentials([usernamePassword(credentialsId: 'aws-cred', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')]) {
                      sh 'echo $AWS_ACCESS_KEY_ID'
                      sh 'echo $AWS_SECRET_ACCESS_KEY'  
                      dir('project1') {
                        sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
//                       sh 'docker run -t -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY arik12/project1:${BUILD_NUMBER}'
                      }
                }
            }
       }
        
       stage('DockerloginPush') {
            steps {
               withCredentials([usernamePassword(credentialsId: 'docker-cred', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                      sh 'echo $DOCKERHUB_PASSWORD'
                      sh 'echo $DOCKERHUB_USERNAME'  
                    env.dockeruser = $DOCKERHUB_USERNAME
                    env.dockerpassword = $DOCKERHUB_PASSWORD
               }

                    
                sh 'docker login -u ${env.dockeruser} -p ${env.dockerpassword}
                         sh 'pwd'
                         sh 'docker push -t arik12/project1:${BUILD_NUMBER}'

            }
       }    
        
    }
}
//         stage('RunDockerFile') {
//             steps {
//                 script {
//                     sh 'pwd'
//                     sh 'ls -l'
//                     sh 'docker --version'
//                     sh  'echo ${BUILD_NUMBER}'
//                     dir('project1') {
//                         sh 'pwd'
//     	                sh 'ls -l'
                        
// //                         sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
// //                         sh 'docker run -t arik12/project1:${BUILD_NUMBER}'

//                        // sh 'docker build -t arik12/project1:${BUILD_NUMBER} .'
//                     }
//                 }
//                 echo 'Hello World'   
//             }
//         }
      
      
//         stage('Hello') {
//             steps {
//                 echo 'Hello World'
//             }
//         }
//     }
// }
// }  
