from tinydb import TinyDB, Query, where
from tinydb.operations import delete
import ValueError

class User():
  user_collection = TinyDB("user_collection.json")  
  
  def __init__(self,username):
    self.username = username

  @classmethod
  def commit_user(cls,user):
    user_list = cls.user_collection.search(where('username') == user.username)
    
    if len(user_list) == 0:
      cls.tree_collection.insert({"id" : user.id,
                           "coordinates" : user.coordinates,
                           "address" : user.address ,
                           "species" : user.species})  
    else:
      raise ValueError("Inserting a tree with id that already exists") 
    pass


  

  