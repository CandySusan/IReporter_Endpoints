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
        self.images =args.get('images'),
        self.videos = args.get('videos'),
        self.comment =args.get('comment')

    def red_flag_dict(self):
        red_flag = dict(
            Id = self.id,
            createdBy = self.createdBy,
            incident_type = self.incident_type,
            location = self.location,
            images = self.images,
            videos = self.videos,
            comment= self.comment
        )
        return red_flag
  


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
