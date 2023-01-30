properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/NatalyPro/DevOps3006.git"
    }
    stage("show files"){
        bat "dir"
    }
}
