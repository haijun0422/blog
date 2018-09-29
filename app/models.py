# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


# 用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # 对user模型扩展
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.now)
    last_see = db.Column(db.DateTime(), default=datetime.now)
    post = db.relationship('Post', backref='users')
    comment = db.relationship('Comment', backref='users')

    # 在模型中加入密码散列
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


# 角色
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    default = db.Column(db.Boolean, default=False, index=True)  # 用户注册时，角色会被设为默认角色
    permissions = db.Column(db.Integer)  # 表示位标志，各操作都对应一个位位置，能执行某项操作的角色，其位会被设为1
    users = db.relationship('User', backref='roles')


# 文章
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='posts')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
    disable = db.Column(db.Boolean)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


