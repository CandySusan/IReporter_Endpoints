
import datetime

red_flags =[]
incident_inventory = []
user_list = []


class Record():
    def __init__(self, **args):

        self.red_flag_id = args.get("red_flag_id"),
        self.createdOn = args.get(datetime.date.today()),
        self.createdBy = args.get('createdBy'),
        self.incident_type = args.get('incident_type'),
        self.location = args.get('location'),
        self.status = args.get('draft'),
        self.images =args.get('images'),
        self.videos = args.get('videos'),
        self.comment =args.get('comment')
    
    def red_flag_dict(self):
        
        red_flag = dict(
            red_flag_id = len(red_flags)+1,
            createdOn = datetime.date.today(),
            createdBy = self.createdBy,
            incident_type= self.incident_type,
            location = self.location,
            images=self.images,
            videos=self.videos,
            comment=self.comment
        )
        red_flags.append(red_flag)
        return red_flags
  


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
