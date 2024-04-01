pipeline {
    agent any

    stages {
        stage("Packaging/Push image") {
            steps {
                withDockerRegistry(credentialdId:"dockerhub",url:"https://index.docker.io/v1/"){
                    sh 'docker build -t lebahoai3003/fastapiapp'
                    sh 'docker push lebahoai3003/fastapiapp'
                }
            }
        }
        stage("Deploy") {
            steps {
                echo 'Deploy'
                sh 'docker image pull lebahoai3003/fastapiapp'
                sh 'docker stop hoailb-fastapi || echo "this container does not exist"'
                sh 'docker run -d --name hoailb-fastapi -p 8989:8989 lebahoai3003/fastapiapp'
            }
        }
    }
}