from documentmanagement.category import Category
from documentmanagement.topic import Topic
from documentmanagement.document import Document
from documentmanagement.storage import Storage


c1 = Category(1, "work")

t1 = Topic(1, "daily tasks", "C:\\work_documents")

d1 = Document(1, 1, 1, "finilize documentmanagement")



d1.add_tag("urgent")

d1.add_tag("work")



storage = Storage()

storage.add_category(c1)

storage.add_topic(t1)

storage.add_document(d1)



print(c1)

print(t1)

print(storage.get_document(1))

print(storage)


