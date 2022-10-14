#We use TinyDB as persistence: https://tinydb.readthedocs.io/en/latest/
from tinydb import TinyDB, Query, where
from tinydb.operations import delete

class Tree():
  tree_collection = TinyDB("tree_collection.json")  
    
  def __init__(self,ident,coordinates,address,species):
    self.id = ident
    #Tuple of (Lat,Lon)
    self.coordinates = coordinates
    self.address = address
    self.species = species
  
  def __str__(self):
    """
    Output: string representation of Tree
    """
    return """This is tree with
    id ={}
    coordinates={}
    address={}
    species = {}
    """.format(self.id,self.coordinates,self.address,self.species)

  @classmethod
  def commit_tree(cls,tree):
    """
    Commits tree to the tree collection
    Note: Development frameworks have an Object Relational Mapper (ORM) doing this automagically for you when you create a class. 
    Sometimes you can deploy those in the Cloud. Sometimes you can't (legacy app), forcing to rethink how you move persistence to the Cloud.

    """
    # Activity: Find a more efficient way to do this check
    tree_list = cls.tree_collection.search(where('id') == tree.id)
    
    if len(tree_list) == 0:
      cls.tree_collection.insert({"id" : tree.id,
                           "coordinates" : tree.coordinates,
                           "address" : tree.address ,
                           "species" : tree.species})  
    else:
      raise ValueError("Inserting a tree with id that already exists") 
      
    
  

   