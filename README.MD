# Json Validator on Python
```
This is simple json validator main purpose of which is to check if your json file has some errors in it or not.
If your file is correct it will format it with all tabs and spaces requried.
If it is not, it will show where is the error.

```
## Working with Maven:
To build use next command:
```
sudo docker build -t v github.com/DanilovArt/jsonValidator
```
To run server:
```
sudo docker run -t -i --rm -p 80:80 v (You can use 4000:80 if port 80 is not free)
```
To test your file use:
```
curl -s --upload-file filename.json http://localhost (or curl -s --upload-file 1.json http://localhost:4000 in case port 80 was not free)
```


## Working with Gradle:
Here we got a problem that docker cannot be run or build without "sudo".


To overcome this difficulies we have to do the following steps:


1) Create the docker group.
```
$ sudo groupadd docker
```
2) Add your user to the docker group.
```
$ sudo usermod -aG docker $USER
```
3) Log out and log back in so that your group membership is re-evaluated.
If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.
On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.


After this we cant easily build our image with:
```
./gradlew clean
./gradlew buildImage
```
Then run the image with:
```
docker run -i -t --rm -p 4000:80 validator-gradle
```
