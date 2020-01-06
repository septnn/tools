docker.exe stop centos
docker.exe rm centos
docker.exe run -itd --name centos -p 80:80 -v /c/User/Jwd/Document/git:/home/git centos