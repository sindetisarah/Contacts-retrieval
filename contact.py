class Contact:
    """
        class contact to create and save it to a list
    """

    contact_list = []
# instance of the constructor method to initialise instancess of new class
    def __init__ (self,first_name,second_name,number):
        self.first_name=first_name
        self.second_name=second_name
        self.number=number

    def save(self):
        """
         saving  contacts to the contact list

        """
# adding the contacts to the contactlist using self to get access
        Contact.contact_list.append(self)

# static method is valid when there is no interaction to the attributes in  our object
@staticmethod
def display_all_contacts():
    """
        method to return contacts saved
    """
    return self.contact_list

# used class method due to the expected interaction by the user
@classmethod
def delete_contact(contact):
    """
         method to delete the contacts saved in the contact_list
    """
    return self.contact_list

# creating instances of new objects
sindet=Contact("Sindet","Sarah","0791776135")
shadya=Contact("Shadya","Obuya","0723446789")
juliet=Contact("JUliet","Kemunto","o123456009")

print(sindet)
print(shadya)
print(juliet)