# Json Validator on Python

This is simple json validator main purpose of which is to check if your json file has some errors in it or not.
If your file is correct it will format it with all tabs and spaces requried.
If it is not, it will show where is the error.

To build use next command:
sudo docker build -t v github.com/DanilovArt/jsonValidator

To run server:
sudo docker run -t -i --rm -p 80:80 v
(You can use 4000:80 if port 80 is not free)

To test your file use:
curl -s --upload-file filename.json http://localhost
(or curl -s --upload-file 1.json http://localhost:4000 in case port 80 was not free)
