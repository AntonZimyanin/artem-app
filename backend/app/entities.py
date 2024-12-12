from pydantic import BaseModel
from typing import Optional


class Group(BaseModel):
    group_id: int
    flow: int
    speciality: str
    number: str
    subgroup: int


class Subject(BaseModel):
    sub_id: int
    name: str


class Teacher(BaseModel):
    id: int
    name: str
    schedule: list[list[int]]


class Lesson(BaseModel):
    id: int
    group: list[Group]
    subject: Subject
    type: str
    length: int
    teacher: int
    is_set: bool = False

    def get_groud_ids(self) -> list[int]:
        ids = []
        for group in self.group:
            ids.append(group.group_id)
        return ids


class Lessons(BaseModel):
    lessons: list[Lesson]
    teachers: list[Teacher]

    def get_lesson(self, id):
        lesson = [x for x in self.lessons if x.id == id][0]
        teacher = [x for x in self.teachers if x.id == lesson.teacher][0]
        if lesson.type == 'Лекция':
            les_type = 'ЛК'
        elif lesson.type == 'Лабораторные':
            les_type = 'ЛАБ'
        return lesson.subject.name, les_type, teacher.name

    def get_group(self, id):
        lesson = [x for x in self.lessons if x.id == id][0]
        return lesson.group
