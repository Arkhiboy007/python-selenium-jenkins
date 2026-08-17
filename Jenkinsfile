pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment & Dependencies') {
            steps {
                bat '''
                @echo off

                echo [1/3] Creating virtual environment...

                if exist venv rmdir /s /q venv

                "C:\\Users\\WCLAB\\AppData\\Local\\Python\\bin\\python.exe" -m venv venv

                echo [2/3] Upgrading pip...

                venv\\Scripts\\python.exe -m pip install --upgrade pip

                echo [3/3] Installing testing packages...

                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Execute Selenium Tests') {
            steps {
                bat '''
                @echo off

                if not exist reports mkdir reports

                echo Running Pytest Suite...

                venv\\Scripts\\python.exe -m pytest tests/ --junitxml=reports/junit-report.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit-report.xml',
                  allowEmptyResults: true
        }
    }
}