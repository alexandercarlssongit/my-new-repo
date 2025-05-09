from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TriangleCalculation(Base):
    __tablename__ = 'triangle_calculations'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    side1 = Column(Float, nullable=False)
    side2 = Column(Float, nullable=False)
    side3 = Column(Float, nullable=False)
    is_triangle = Column(Integer, nullable=False)  # 1 for true, 0 for false
    triangle_type = Column(String(50), nullable=False)
    angle1 = Column(Float, nullable=False)
    angle2 = Column(Float, nullable=False)
    angle3 = Column(Float, nullable=False)
    area = Column(Float, nullable=False)
    perimeter = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'side1': self.side1,
            'side2': self.side2,
            'side3': self.side3,
            'is_triangle': bool(self.is_triangle),
            'triangle_type': self.triangle_type,
            'angles': (self.angle1, self.angle2, self.angle3),
            'area': self.area,
            'perimeter': self.perimeter,
            'created_at': self.created_at.isoformat()
        }

def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session() 