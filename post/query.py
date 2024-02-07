from usermanagement.query import QueryPatterns,GetUserAllPostQuery
from post.models import Comment

class GetAllCommentsQuery(QueryPatterns):

    def get_all_data(self):
        all_datas = []
        for data in self.data:
            all_data_in_dict = {}
            all_data_in_dict["id"] = data.id
            all_data_in_dict["message"] = data.message
            all_data_in_dict["user"] = data.user.name
            all_data_in_dict["profile_pic"] = data.user.profile_picture.url if data.user.profile_picture else None
            all_datas.append(all_data_in_dict)
        return all_datas
    

class GetAallPostDetailQuery(QueryPatterns):

    def get_all_data(self,request):
        all_datas =[]
        comments = Comment.objects.filter(post=self.data.first()).order_by("-created_at")
        for data in self.data:
            all_data_in_dict = {}
            all_data_in_dict["post"] = GetUserAllPostQuery(data=[data]).get_all_data(request=request)
            all_data_in_dict["comments"] = GetAllCommentsQuery(data=comments).get_all_data()
            all_datas.append(all_data_in_dict)
        return all_datas     