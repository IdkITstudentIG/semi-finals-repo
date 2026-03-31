from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class DelacruzCategories(Base):
    __tablename__ = "ebdao_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class DelacruzProducts(Base):
    __tablename__ = "ebdao_products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("ebdao_categories.id"))

class DelacruzCustomers(Base):
    __tablename__ = "ebdao_customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class DelacruzSales(Base):
    __tablename__ = "ebdao_sales"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("ebdao_customers.id"))
