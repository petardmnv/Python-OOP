from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    categories: List[Category]
    topics: List[Topic]
    documents: List[Document]

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        ids = [c.id for c in self.categories]
        if category.id not in ids:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        ids = [t.id for t in self.topics]
        if topic.id not in ids:
            self.topics.append(topic)

    def add_document(self, document: Document):
        ids = [d.id for d in self.documents]
        if document.id not in ids:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        curr_c = self.get_by_id(category_id, self.categories)
        curr_c.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        [t for t in self.topics if t.id == topic_id][0].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        curr_d = self.get_by_id(document_id, self.documents)
        curr_d.file_name = new_file_name

    def delete_category(self, category_id: int):
        curr_c = self.get_by_id(category_id, self.categories)
        self.categories.remove(curr_c)

    def delete_topic(self, topic_id: int):
        curr_t = self.get_by_id(topic_id, self.topics)
        self.topics.remove(curr_t)

    def delete_document(self, document_id: int):
        curr_d = self.get_by_id(document_id, self.documents)
        self.documents.remove(curr_d)

    def get_document(self, document_id: int):
        return self.get_by_id(document_id, self.documents)

    def __repr__(self):
        res = []
        for d in self.documents:
            res.append(d.__repr__())
        return '\n'.join(res)

    @staticmethod
    def get_by_id(wanted_id: int, paramerters):
        for p in paramerters:
            if p.id == wanted_id:
                return p
