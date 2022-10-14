from tinydb import TinyDB, Query, where
from tinydb.operations import delete
import ValueError

class Story():
  story_collection = TinyDB("story_collection.json")  
  
  
  def __init__(self,story_id,username,tree_id,text,story_date):  
    self.story_id = story_id
    self.username = username
    self.tree_id = tree_id
    self.text = text
    self.date = story_date

  @classmethod
  def commit_story(cls,story):
    """
    Input: An instance of a Story
    Output: The Story is persisted in database
    """
    pass

  @classmethod
  def top_huggers(cls):
    """
    Output: Dictionary user.username -> number of stories this user has
    Hint: Create some stories so you can create a meaningful test case
    """
    pass

  @classmethod
  def best_friend(cls,Tree):
    """
    Input: A tree
    Output: The user that has written most stories involving the input Tree.
    """
    pass

    
