from app.models.user import session, User

def get_users():
    return session.query(User).all()

def get_user(user_id):
    return session.query(User).filter(User.user_id == user_id).first()

def add_user(email, password):
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user

def update_user(user_id, username=None, password=None):
    user = get_user(user_id)
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        session.commit()
    return user

def delete_user(user_id):
    user = get_user(user_id)
    if user:
        session.delete(user)
        session.commit()
    return user
