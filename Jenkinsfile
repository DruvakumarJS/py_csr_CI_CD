pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/DruvakumarJS/py_csr_CI_CD.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest Tests/ --maxfail=1 --disable-warnings -v --html=report.html --junitxml=results.xml'
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'results.xml'
                publishHTML(target: [
                    reportName: 'HTML Report',
                    reportDir: '.',
                    reportFiles: 'report.html',
                    keepAll: true
                ])
            }
        }
    }
}
