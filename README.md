# Tromzo Backend Challenge 

Design an ObjectMgr which manages a pool of objects. Objects can be considered to be ints (from 1 to n). It should provide api’s to get_object() and free_object().

get_object(): It returns any object , available in the pool. An object cannot be given away again, unless it has been freed.

free_object(int obj): It returns the obj back to the pool, so that it can be given out again.

Discuss the api’s definitions, data structures and write tests.

Follow-on:

Write a Graphql API /object to use the above functions to create, get and free objects.

Deploy it as a service/container that can be used to deploy on a linux server.

Feel free to use standard libraries and pick your choice of language.


## Stack

* Python
* Postgres
* Django
* Grafene Django
* Gunicorn/Uvicorn
* Docker

## Tests

```sh

# run tests locally
./bin/test.sh

# run tests in Docker
docker-compose -f docker-compose.test.yml up -d
```
