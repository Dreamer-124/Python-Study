@classmethod
@DB.connection_context()
def get_list(cls, joined_tenant_ids, user_id,
             page_number, items_per_page, orderby, desc, id, name):
    kbs = cls.model
    # 这里是方法的具体实现