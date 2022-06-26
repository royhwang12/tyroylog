#!/bin/bash

curl --request POST http://localhost:5000/api/timeline_post -d 'name=Roy&email=rh1160@georgetown.edu&content=Added a Database!'

curl --request GET http://localhost:5000/api/timeline_post

curl --request DELETE http://localhost:5000/api/timeline_post

