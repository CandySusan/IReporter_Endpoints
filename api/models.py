import random

incident_inventory = []
user_list = []


class Record():
    def __init__(self, **args):

        self.id = args.get("id"),
        self.createdOn = args.get('createdOn'),
        self.createdBy = args.get('createdBy'),
        self.incident_type = args.get('incident_type'),
        self.location = args.get('location'),
        self.status = args.get('draft'),
        self.Images =args.get('Images'),
        self.Videos = args.get(' Videos'),
        self.comment =args.get('comment')
  


class User:
    def __init__(self, **args):

        self.UserId =args.get("UserId"),
        self.firstname = args.get("firstname"),
        self.lastname = args.get("lastname"),
        self.othernames = args.get("othernames"),
        self.email =args.get("email"),
        self.phoneNumber = args.get("phoneNumber"),
        self.username = args.get("username"),
        self.registered = args.get("registered"),
        self.isAdmin = args.get("isAdmin")
