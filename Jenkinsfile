pipeline {
    agent any

    environment {
        // Optional: Path to Python if not in system PATH
        PYTHON = "python"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                // Ensure no old .git or venv remains
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/DruvakumarJS/py_csr_CI_CD.git',
                    branch: 'master', // use the exact branch from your repo
                    credentialsId: '' // leave empty if public, otherwise use your Jenkins credentials ID
                )
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat "${env.PYTHON} -m venv venv"

                // Upgrade pip inside venv
                bat "venv\\Scripts\\python.exe -m pip install --upgrade pip"

                // Install requirements if you have a requirements.txt
                bat "venv\\Scripts\\python.exe -m pip install -r requirements.txt"

            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest or your preferred test runner
                bat "venv\\Scripts\\python.exe -m pytest"
            }
        }

        stage('Publish Reports') {
            steps {
                // Example: archive test results
                junit '**/test-reports/*.xml'
            }
        }
    }

    post {
        always {
            echo "Build finished, cleaning up if needed"
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
