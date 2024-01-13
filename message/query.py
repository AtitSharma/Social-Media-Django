from usermanagement.query import QueryPatterns



class MessageQuery(QueryPatterns):
    def get_all_data(self):
        all_datas =[]
        for data in self.data:
            all_data_in_dict = {}
            all_data_in_dict["id"] = data.id
            all_data_in_dict["from_user"] = data.from_user.name
            all_data_in_dict["to_user"] = data.to_user.name
            all_data_in_dict["message"] = data.message
            all_datas.append(all_data_in_dict)
        return all_datas
