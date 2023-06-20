
# MYWEB DEMO

This is my personal project for practicing devops skills

## Author
Thanh Tran

## Description
- This is a PoC (Proof-of-Concept) to showcase a working solution for enterprise/company based on DevOps Skillsets that I have.
- This is a continuous development project so there will be additional changes and improvement over time.
- This is a standalone project that I work by myself.
- This project consists of 2 parts:
     - Infrastructure provisioning: setup, config backend servers (DNS, NGINX, JENKINS, JFROG)
     - Front-end application: streamlit
- Technologies have been used:
   - Containerization (Docker, Kubernetes)
   - Automation and Orchestration (Jenkins, Packer, Ansible, Vagrant)
   - Virtualization (AWS, VMWare Fusion)
   - CI/CD
     
## Getting Started
- To automate infrastructure, we use packer/vagrant to provision backend servers (DNS, NGINX, JENKINS, JFROG)
- After having the infrastructure ready, we load the backup jobs to Jenkins server and run the provison jobs to but the front end application in DEV environment (on 1 VMware VM)
- Once we have tested the application working in DEV, we can deploy the application to PROD environment (AWS/VM running k8s) using Jenkins job. 
### Dependencies
- Sufficient computer performance (RAM, Storage)
- Valid AWS account

### Installing
- Packer/Vagrant installed in your host machine.
- Hypervisor of your choosing installed.
- Run the packer/vagrant command to provision all the servers.
- Go to Jenkins server and run command to load the backup files.

### Diagrams
![DNS-NGINX](https://github.com/thanh-tran0106/Myweb/assets/74903521/89cce842-840b-4025-a078-44fb9b9d430d) 
- Backend servers diagram /

![CI:CD](https://github.com/thanh-tran0106/Myweb/assets/74903521/6cfc5ced-a56a-4235-ae95-8a1fd4be58e9)
- CI/CD diagram /
![Untitled Diagram](https://github.com/thanh-tran0106/Myweb/assets/74903521/9e8b8846-23c5-4714-9fdb-7bfd98270f28)

### Executing program
TBD
