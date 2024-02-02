from .db import get_session
from sqlmodel import select, insert, update, delete

class BaseDAO:
    
    model = None
    
    @classmethod
    def find_all(cls, session):
        print(cls.model.id)
        query = select(cls.model).order_by(cls.model.id.asc())
        result = session.exec(query)
        return result.all()
        
    @classmethod
    def find_by_id(cls, session, model_id):
        query = select(cls.model).filter_by(id=model_id)
        result = session.exec(query).one_or_none()
        return result
    
    @classmethod
    def add(cls, session, data):
        
        query = insert(cls.model).values(**data)
        session.exec(query)
        session.commit()
    
    @classmethod
    def update(cls, session, model_id, data):
        query = update(cls.model).where(cls.model.id==model_id).values(**data)
        session.exec(query)
        session.commit()
    
    @classmethod
    def delete(cls, session,model_id):
        query = delete(cls.model).filter_by(id=model_id)
        session.exec(query)
        session.commit()