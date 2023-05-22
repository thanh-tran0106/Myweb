pipeline {
  agent {
     label "robot1"
   }
  stages {
    stage('Checkout: Myweb source code') {
      steps {
        dir('Myweb') {
          git branch : 'main',
            url : 'https://github.com/thanh-tran0106/Myweb.git'
        }     
      }
    }
  
  stage('Docker provisioning') {
    steps {
      script {
        dir('Myweb') {
          sh 'ls -la'
          sh 'docker rm -f streamlit'
          sh 'docker build -t streamlit .'
          sh 'docker run --name streamlit -p 8501:8501 -d streamlit'
        }
      }
    }
  }
}
}
