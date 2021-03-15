class Contact:
    def __init__(self, full_name, last_name, contact_no, email_id):
        self.full_name = full_name
        self.last_name = last_name
        self.contact_no = contact_no
        self.email_id = email_id
        pass

    def getters(self):
        return(self.full_name, self.last_name, self.contact_no, self.email_id)
