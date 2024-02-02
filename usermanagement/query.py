from abc import ABC,abstractmethod
from post.models import PostImages


class QueryPatterns(ABC):

    def __init__(self,data):
        self.data = data

    @abstractmethod
    def get_all_data(self):
        return self.data





class GetAllFriendRequestQuery(QueryPatterns):

    def get_all_data(self):
        all_datas = []
        for data in self.data :
            all_data_in_dict = {}
            all_data_in_dict["id"]= data.id
            all_data_in_dict["to_user"] = data.to_user.all().first().name
            all_data_in_dict["from_user"] = data.from_user.all().first().name
            all_data_in_dict["status"] = data.status
            all_datas.append(all_data_in_dict)
        return all_datas
    

class GetUserAllPostQuery(QueryPatterns):

    def get_all_data(self):
        all_datas = []
        for post in self.data :
            all_data_in_dict = {}
            all_data_in_dict["id"] = post.id
            all_data_in_dict["description"] = post.description
            all_data_in_dict["username"] = post.user.name
            all_data_in_dict["likes"] = post.get_likes
            all_data_in_dict["images"] = GetPostImages(data=post).get_all_data()
            all_data_in_dict["profile_pic"] = post.user.profile_picture.url if post.user.profile_picture else None
            all_datas.append(all_data_in_dict)
        return all_datas




class GetSharedPostQuery(QueryPatterns):

    def get_all_data(self):
        all_datas=[]
        for shared_post in self.data:
            all_data_in_dict={}
            all_data_in_dict["id"] = shared_post.id
            all_data_in_dict["user"] = shared_post.user.all().first().name
            all_data_in_dict["description"] = shared_post.description
            all_data_in_dict["post"] = GetUserAllPostQuery(data=shared_post.post.all()).get_all_data()
            all_data_in_dict["likes"] = shared_post.get_likes
            all_datas.append(all_data_in_dict)
        return all_datas





class GetPostImages(QueryPatterns):

    def get_all_data(self):
        all_images = [image.image.url for image in PostImages.objects.filter(post=self.data)]
        return all_images


        

    