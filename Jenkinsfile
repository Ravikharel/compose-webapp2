pipeline{ 
    agent any
    environment{ 
        COMPOSE_APP_NAME = "my-compose-app"
        HARBOR_URL = "harbor.registry.local/jenkins1/"
        IMAGE_NAME_FRONTEND = "web"
        IMAGE_NAME_MYSQL = "mysql"
        IMAGE_TAG = "v1"
        HARBOR_PASSWORD = "Harbor12345"
    }
    stages{ 
        stage('Building the Images') {
            steps { 
                script { 
                    sh '''
                        docker image build -t ${HARBOR_URL}${IMAGE_NAME_FRONTEND}:${IMAGE_TAG} -f web/Dockerfile web/
                    '''
                }
            }
        }
        stage('Pushing the Images to Harbor Registry') { 
            steps { 
                script { 
                    sh '''
                        echo ${HARBOR_PASSWORD} | docker login ${HARBOR_URL} -u admin --password-stdin
                        docker push ${HARBOR_URL}${IMAGE_NAME_FRONTEND}:${IMAGE_TAG}
                    '''
                }
            }
        }
        stage('Pulling Images and Running MySQL Container on Agent Node') { 
            agent { 
                label "vagrant-slave"
            }
            steps { 
                script { 
                    sh '''
                        echo ${HARBOR_PASSWORD} | docker login ${HARBOR_URL} -u admin --password-stdin
                        docker pull ${HARBOR_URL}${IMAGE_NAME_FRONTEND}:${IMAGE_TAG}
                    '''
                }
            }
        }
        stage('Running Docker Containers') { 
            agent {
                label "vagrant-slave"
            }
            steps { 
                script { 
                    sh """
                        scp docker-compose.yml vagrant@192.168.56.13:/
                        docker compose up -d
                    """
                }
            }
        }
        stage('Wait for service'){ 
            steps{
                script{ 
                    sh "sleep 10"
                }
            }
        }
        stage('') {
            steps {
                script {
                    sh "docker ps"
                }
            }
        }



    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}