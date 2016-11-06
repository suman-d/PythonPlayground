from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        self.user = input("Enter the author name : ")
        self.user_blog = None

        # Check is the author exists

        if self._user_has_account():
            print("Welcome Back {}".format(self.user))

        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {"author": self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter the tile of the Blog : ")
        description = input("Enter the blog description : ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("What would you like to do, Read(R) or Write(W) Blog ? :")
        if read_or_write == "R":
            self._list_blogs()
            self._view_blogs()
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging !! ")

    def _list_blogs(self):
        blogs = Database.find(collection="blogs", query={})
        for blog in blogs:
            print("ID : {}, Tile : {}, Author : {}".format(blog["id"], blog["title"], blog["author"]))

    def _view_blogs(self):
        blog_to_see = input("Enter the ID of the blog you would like to view : ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()

        for post in posts:
            print("Date : {}, Title : {}\n\n{}".format(post["created_date"], post["title"], post["content"]))










