from database import get_db
from database.models import *


def add_post_db(main_text:str, user_id:int):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()
        if not user:
            return False
        new_post = Post(main_text=main_text, user_id=user_id)
        db.add(new_post)
        db.commit()
        return "Пост успешно опубликован!"


def add_comment_db(user_id:int, post_id:int, main_text:str):
    with next(get_db()) as db:
        user = db.query(Comment).filter_by(user_id=user_id).first()
        if not user:
            return False
        post = db.query(Post).filter_by(id=post_id).first()  # Проверяем пост
        if not post:
            return False
        new_comment = Comment(user_id=user_id, post_id=post_id, main_text=main_text)
        db.add(new_comment)
        db.commit()
        return "Успешно добавлен комментарий."


def add_message_db(user_id:int, main_text:str, name="Аноним"):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()  # Проверка существования пользователя
        if not user:
            return False
        new_message = Message(to_user=user_id, main_text=main_text, name=name)
        db.add(new_message)
        db.commit()
        return "Вы отправили анонимное сообщение."

def remove_post_db(post_id:int):
    with next(get_db()) as db:
        post = db.query(Post).filter_by(id=post_id).first()
        if not post:
            return False
        db.delete(post)
        db.commit()
        return "Пост успешно удален"





def change_comment_db(comment_id:int, main_text:str):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            comment.main_text = main_text
            db.commit()
            db.refresh(comment)
            return "Пост успешно изменен!"
        return "Пост не найден."

