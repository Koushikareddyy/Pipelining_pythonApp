pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-https', url: 'https://github.com/koushikareddyy/Pipelining_pythonApp.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                bat '"//Library//Frameworks//Python.framework//Versions//3.13/bin//python3" -m venv venv'
                bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.\\venv\\Scripts\\pip install pandas numpy tenserflow flask'
            }
        }

        stage('Run Flask App') {
            steps {
                bat '.\\venv\\Scripts\\python app.py'
            }
        }
    }
}

