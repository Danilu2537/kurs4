import hashlib

from project.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, user_d):
        return self.dao.update(user_d)

    def get_by_email_and_password(self, email, password):
        return self.dao.get_by_email_and_password(email, password)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def partially_update(self, user_d):
        user = self.get_one(user_d['id'])
        if 'email' in user_d:
            user.email = user_d.get('email')
        if 'password' in user_d:
            password = user_d.get('password')
            user.password = hashlib.sha256(password.encode()).hexdigest()
        if 'name' in user_d:
            user.name = user_d.get('name')
        if 'surname' in user_d:
            user.surname = user_d.get('surname')
        if 'favourite_genre' in user_d:
            user.favourite_genre = user_d.get('favourite_genre')
        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)
