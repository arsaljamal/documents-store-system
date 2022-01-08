# documents-store-system
This is a python project demonstrating a document store system

## To run the application in docker
1. clone the project from git
2. in terminal `cd /documentsstoresystem`
3. `docker-compose up -d --build`
4. then run migration scripts `docker-compose exec docstore python manage.py migrate --noinput`

### open browser and type `localhost:8000`

## Populating data
1.) For Folder `localhost:8000/api/folders` both GET AND POST method are supported, 
Json : `{
 "name" : "test-folder"
 "size" : 10
}`

2.) For Documents `localhost:8000/api/documents` both GET AND POST method are supported, 
Json : `{
 "name" : "test-doc"
 "size" : 10
 "folder" : 1 //folder-id
}`

3.) For Topics `localhost:8000/api/topics` both GET AND POST method are supported, 
Json : ` {
 "longDescription" : "test topic"
 "shortDescription" : "test"
 "folder" : 1 //folder-id
 "document" : 1 //document-id
}`

## Searching for documents based on certain Folder and Topic
api GET : `localhost:8062/api/search/documents?folderName=test-folder&shortDescription=test`, 
result : 
`
[
    {
        "id": 1,
        "name": "test-doc1",
        "size": 10,
        "folder": 1
    },
    {
        "id": 2,
        "name": "test-doc2",
        "size": 20,
        "folder": 1
    }
]
`
