from usermanagement.query import QueryPatterns


class GetAllCommentsQuery(QueryPatterns):

    def get_all_data(self):
        all_datas = []
        for data in self.data:
            all_data_in_dict = {}
            all_data_in_dict["id"] = data.id
            all_data_in_dict["message"] = data.message
            all_data_in_dict["user"] = data.user.name
            all_datas.append(all_data_in_dict)
        return all_datas