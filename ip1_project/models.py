from sqlalchemy import Column, Integer, String, Numeric, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class EbdaoCategories(Base):
    __tablename__ = "ebdao_categories"
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

class EbdaoSuppliers(Base):
    __tablename__ = "ebdao_suppliers"
    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

class EbdaoCashiers(Base):
    __tablename__ = "ebdao_cashiers"
    cashier_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False, default="cashier")
    status = Column(String(20), nullable=False, default="active")

class EbdaoCustomers(Base):
    __tablename__ = "ebdao_customers"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    loyalty_points = Column(Integer, nullable=False, default=0)

class EbdaoProducts(Base):
    __tablename__ = "ebdao_products"
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("ebdao_categories.category_id"))
    supplier_id = Column(Integer, ForeignKey("ebdao_suppliers.supplier_id"))
    name = Column(String(200), nullable=False)
    sku = Column(String(80), nullable=False, unique=True)
    barcode = Column(String(80))
    cost_price = Column(Numeric(10,2), nullable=False, default=0.00)
    selling_price = Column(Numeric(10,2), nullable=False, default=0.00)
    stock_qty = Column(Integer, nullable=False, default=0)
    reorder_level = Column(Integer, nullable=False, default=0)
    unit = Column(String(30), nullable=False, default="piece")
    status = Column(String(20), nullable=False, default="active")

class EbdaoDiscounts(Base):
    __tablename__ = "ebdao_discounts"
    discount_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    type = Column(String(30), nullable=False)
    value = Column(Numeric(8,2), nullable=False)
    valid_from = Column(Date)
    valid_until = Column(Date)
    applies_to = Column(String(50))
    status = Column(String(20), nullable=False, default="active")

class EbdaoSales(Base):
    __tablename__ = "ebdao_sales"
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    cashier_id = Column(Integer, ForeignKey("ebdao_cashiers.cashier_id"))
    customer_id = Column(Integer, ForeignKey("ebdao_customers.customer_id"))
    sale_date = Column(DateTime, nullable=False)
    subtotal = Column(Numeric(12,2), nullable=False, default=0.00)
    discount_amount = Column(Numeric(12,2), nullable=False, default=0.00)
    tax_amount = Column(Numeric(12,2), nullable=False, default=0.00)
    total_amount = Column(Numeric(12,2), nullable=False, default=0.00)
    payment_method = Column(String(30), nullable=False)
    amount_tendered = Column(Numeric(12,2), nullable=False, default=0.00)
    change_given = Column(Numeric(12,2), nullable=False, default=0.00)
    status = Column(String(20), nullable=False, default="completed")

class EbdaoSaleItems(Base):
    __tablename__ = "ebdao_sale_items"
    sale_item_id = Column(Integer, primary_key=True, autoincrement=True)
    sale_id = Column(Integer, ForeignKey("ebdao_sales.sale_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("ebdao_products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Numeric(10,2), nullable=False)
    discount_pct = Column(Numeric(5,2), nullable=False, default=0.00)
    line_total = Column(Numeric(12,2), nullable=False)

class EbdaoStockMovements(Base):
    __tablename__ = "ebdao_stock_movements"
    movement_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("ebdao_products.product_id"), nullable=False)
    cashier_id = Column(Integer, ForeignKey("ebdao_cashiers.cashier_id"))
    type = Column(String(20), nullable=False)
    quantity = Column(Integer, nullable=False)
    reason = Column(Text)
    moved_at = Column(DateTime, nullable=False)

class EbdaoPurchaseOrders(Base):
    __tablename__ = "ebdao_purchase_orders"
    po_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey("ebdao_suppliers.supplier_id"))
    cashier_id = Column(Integer, ForeignKey("ebdao_cashiers.cashier_id"))
    order_date = Column(DateTime, nullable=False)
    received_date = Column(Date)
    total_cost = Column(Numeric(12,2), nullable=False, default=0.00)
    status = Column(String(20), nullable=False, default="pending")

class EbdaoPOItems(Base):
    __tablename__ = "ebdao_po_items"
    po_item_id = Column(Integer, primary_key=True, autoincrement=True)
    po_id = Column(Integer, ForeignKey("ebdao_purchase_orders.po_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("ebdao_products.product_id"), nullable=False)
    qty_ordered = Column(Integer, nullable=False, default=0)
    qty_received = Column(Integer, nullable=False, default=0)
    unit_cost = Column(Numeric(10,2), nullable=False, default=0.00)