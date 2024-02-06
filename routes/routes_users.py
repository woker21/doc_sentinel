from fastapi import APIRouter, Response
from config.db import conn
from schemas.schemas_user import userEntity, usersEntity
from models.models_user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

# obtener todos los usuarios


@user.get('/users', response_model=list[User], tags=['users'])
def find_all_users():
    return usersEntity(conn.DocSentinel.user.find())

# crear un usuario


@user.post('/user', response_model=User, tags=['users'])
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']

    id = conn.DocSentinel.user.insert_one(new_user).inserted_id
    user = conn.DocSentinel.user.find_one({"_id": id})
    return userEntity(user)

# obtener 1 solo usuario


@user.get('/user/{id}', response_model=User, tags=['users'])
def find_user(id: str):
    return userEntity(conn.DocSentinel.user.find_one({'_id': ObjectId(id)}))


# actualizar un usuario
@user.put('/users/{id}', response_model=User, tags=['users'])
def update_user(id: str, user: User):
    result = conn.DocSentinel.user.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': dict(user)})

    return userEntity(result)


# eliminar un usuario
@user.delete('/users/{id}', tags=['users'])
def delete_user(id: str):
    userEntity(conn.DocSentinel.user.find_one_and_delete(
        {'_id': ObjectId(id)}, {'$set': dict(user)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
