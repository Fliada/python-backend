class Request:
    def __init__(self, id_, user_id, staff_id, address_id, comment, status_id,
                 date_creation, date_selected, date_actual):
        self.id_ = id_
        self.user_id = user_id
        self.staff_id = staff_id
        self.address_id = address_id
        self.comment = comment
        self.status_id = status_id
        self.date_creation = date_creation
        self.date_selected = date_selected
        self.date_actual = date_actual
