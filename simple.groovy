properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    environment {
        DOCKER_COMPOSE = "/usr/bin/compose"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage("Testing myapp") {
            steps {
                withEnv(["PATH+EXTRA=$DOCKER_COMPOSE"]) {
                    sh "cd $WORKSPACE/final_project"
                    dir ("$WORKSPACE/final_project") {
                        sh "ls -a"
                        sh "docker compose up --abort-on-container-exit"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'alluredir']]
            ])
            script {
                withEnv(["PATH+EXTRA=$DOCKER_COMPOSE"]) {
                    sh "cd $WORKSPACE/final_project"
                    dir("$WORKSPACE/final_project") {
                        sh 'docker compose down'
                    }
                }
            }
            cleanWs()
        }
    }
}
