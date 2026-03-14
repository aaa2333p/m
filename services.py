from models import Product, Customer, Transaction, Invoice, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

class ProductService:
    @staticmethod
    def add_product(name, description, price):
        session = Session()
        product = Product(name=name, description=description, price=price)
        session.add(product)
        session.commit()
        session.close()
        return product

    @staticmethod
    def get_all_products():
        session = Session()
        products = session.query(Product).all()
        session.close()
        return products

    @staticmethod
    def update_product(product_id, name, description, price):
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            product.name = name
            product.description = description
            product.price = price
            session.commit()
        session.close()
        return product

    @staticmethod
    def delete_product(product_id):
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            session.delete(product)
            session.commit()
        session.close()

class CustomerService:
    @staticmethod
    def add_customer(name, contact_info):
        session = Session()
        customer = Customer(name=name, contact_info=contact_info)
        session.add(customer)
        session.commit()
        session.close()
        return customer

    @staticmethod
    def get_all_customers():
        session = Session()
        customers = session.query(Customer).all()
        session.close()
        return customers

    @staticmethod
    def update_customer(customer_id, name, contact_info):
        session = Session()
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            customer.name = name
            customer.contact_info = contact_info
            session.commit()
        session.close()
        return customer

    @staticmethod
    def delete_customer(customer_id):
        session = Session()
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()
        session.close()

class TransactionService:
    @staticmethod
    def create_transaction(user_id, product_id, quantity):
        session = Session()
        product = session.query(Product).filter(Product.id == product_id).first()
        if product:
            total_price = product.price * quantity
            transaction = Transaction(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price)
            session.add(transaction)
            session.commit()
            session.close()
            return transaction
        session.close()
        return None

    @staticmethod
    def get_all_transactions():
        session = Session()
        transactions = session.query(Transaction).all()
        session.close()
        return transactions

class InvoiceService:
    @staticmethod
    def create_invoice(transaction_id, invoice_date, amount_due):
        session = Session()
        invoice = Invoice(transaction_id=transaction_id, invoice_date=invoice_date, amount_due=amount_due)
        session.add(invoice)
        session.commit()
        session.close()
        return invoice

    @staticmethod
    def get_all_invoices():
        session = Session()
        invoices = session.query(Invoice).all()
        session.close()
        return invoices