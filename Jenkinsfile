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
                // Using the explicit path to python3 from your prompt
                sh """
                    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m venv venv
                    ./venv/bin/python -m pip install --upgrade pip
                    ./venv/bin/pip install pandas numpy tensorflow flask
                """
            }
        }

        stage('Run Flask App') {
            steps {
                // Correcting paths for a Unix-like system and using 'sh'
                sh "./venv/bin/python app.py"
            }
        }
    }
}
