docker.exe stop dev
docker.exe rm dev
docker.exe rmi $(docker.exe images dev:v1 -q)
docker.exe build -t dev:v1 .
docker.exe images
docker.exe run --name dev -itd -p 80:80 -v /c/Users/JWD/Documents/git/juewei:/home/juewei dev:v1
docker.exe ps