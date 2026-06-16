import uuid
from typing import List, Dict, Optional
import copy

# ==========================================
# OOP Concepts: Classes & Objects, Inheritance
# ==========================================

class Product:
    """
    Base class representing a generic product.
    Demonstrates INHERITANCE: PhysicalProduct and DigitalProduct will inherit from this.
    """
    def __init__(self, name: str, price: float, sku: str, image_url: str, stock_quantity: int, specifications: dict = None):
        self.name = name
        self.price = price
        self.sku = sku
        self.image_url = image_url
        self.stock_quantity = stock_quantity
        self.specifications = specifications or {}

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "sku": self.sku,
            "image_url": self.image_url,
            "stock_quantity": self.stock_quantity,
            "specifications": self.specifications,
            "type": "Generic"
        }

class PhysicalProduct(Product):
    """
    Inherits from Product. Adds physical attributes.
    Demonstrates INHERITANCE.
    """
    def __init__(self, name: str, price: float, sku: str, image_url: str, stock_quantity: int, shipping_weight: float, shipping_cost: float, specifications: dict = None):
        super().__init__(name, price, sku, image_url, stock_quantity, specifications)
        self.shipping_weight = shipping_weight
        self.shipping_cost = shipping_cost

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Physical",
            "shipping_weight": self.shipping_weight,
            "shipping_cost": self.shipping_cost
        })
        return data

class DigitalProduct(Product):
    """
    Inherits from Product. Adds digital attributes. Digital products typically have 'infinite' stock.
    Demonstrates INHERITANCE.
    """
    def __init__(self, name: str, price: float, sku: str, image_url: str, stock_quantity: int, download_link: str, file_size: str, specifications: dict = None):
        super().__init__(name, price, sku, image_url, stock_quantity, specifications)
        self.download_link = download_link
        self.file_size = file_size

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Digital",
            "download_link": self.download_link,
            "file_size": self.file_size
        })
        return data

# ==========================================
# OOP Concept: Composition
# ==========================================

class ShoppingCart:
    """
    Contains a list of Product objects. Does not inherit from Product.
    Demonstrates COMPOSITION.
    """
    def __init__(self):
        self.items: List[Product] = [] # List of Product objects

    def add_item(self, product: Product) -> bool:
        """Adds item to cart. (Stock check handled by StockManager before adding)"""
        self.items.append(product)
        return True
        
    def remove_item(self, sku: str) -> bool:
        """Removes the first occurrence of an item by sku."""
        for item in self.items:
            if item.sku == sku:
                self.items.remove(item)
                return True
        return False

    def get_subtotal(self) -> float:
        return sum(item.price for item in self.items)

    def get_total_shipping(self) -> float:
        total_shipping = 0.0
        for item in self.items:
            if isinstance(item, PhysicalProduct):
                total_shipping += item.shipping_cost
        return total_shipping

    def get_cart_details(self) -> dict:
        return {
            "items": [item.to_dict() for item in self.items],
            "subtotal": self.get_subtotal(),
            "total_shipping": self.get_total_shipping()
        }
        
    def clear(self):
        self.items = []

# ==========================================
# OOP Concept: Classes & Objects
# ==========================================

class User:
    """
    Represents a User. Has a ShoppingCart instance and a list of past orders.
    Demonstrates CLASSES & OBJECTS, as well as COMPOSITION.
    """
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password # In real-world, this should be hashed!
        self.cart = ShoppingCart() # Composition: User HAS-A ShoppingCart
        self.past_orders = []      # List of receipt dictionaries

    def add_order(self, receipt: dict):
        self.past_orders.append(receipt)

# ==========================================
# NEW OOP Concept: Encapsulation (User Management)
# ==========================================

class AuthManager:
    """
    Handles user registration and authentication logic.
    Encapsulates the 'database' of users and the logic to verify them.
    """
    def __init__(self):
        # Mock database of users keyed by username
        self._users: Dict[str, User] = {}
        
    def register(self, username: str, email: str, password: str) -> bool:
        if username in self._users:
            return False # User already exists
        self._users[username] = User(username, email, password)
        return True
        
    def authenticate(self, username: str, password: str) -> Optional[User]:
        user = self._users.get(username)
        if user and user.password == password:
            return user
        return None
        
    def get_user(self, username: str) -> Optional[User]:
        return self._users.get(username)

# ==========================================
# NEW OOP Concept: Inventory Management
# ==========================================

class StockManager:
    """
    Manages the central inventory. Validates stock and decreases it upon purchase.
    """
    def __init__(self):
        self._inventory: Dict[str, Product] = {}
        
    def add_product(self, product: Product):
        self._inventory[product.sku] = product
        
    def get_all_products(self) -> List[Product]:
        return list(self._inventory.values())
        
    def get_product(self, sku: str) -> Optional[Product]:
        return self._inventory.get(sku)
        
    def check_stock(self, sku: str, requested_qty: int = 1) -> bool:
        """Checks if a product has enough stock."""
        product = self.get_product(sku)
        if product:
            # For digital products, stock is virtually infinite (represented by high number)
            return product.stock_quantity >= requested_qty
        return False
        
    def decrement_stock(self, sku: str, qty: int = 1):
        """Reduces the stock after a successful purchase."""
        product = self.get_product(sku)
        if product and product.stock_quantity >= qty:
            # If it's a digital product (e.g. stock > 9999), we might not even decrement,
            # but for consistency we can decrement. 
            product.stock_quantity -= qty

# ==========================================
# OOP Concept: Abstraction
# ==========================================

class PaymentProcessor:
    """
    Hides the complex logic of calculating tax, summing totals, and simulating payment.
    Also coordinates with StockManager to deduct inventory upon success.
    Demonstrates ABSTRACTION.
    """
    TAX_RATE = 0.18 # 18% GST

    def __init__(self, stock_manager: StockManager):
        self.stock_manager = stock_manager

    def checkout(self, user: User) -> dict:
        if not user.cart.items:
            return {"success": False, "message": "Cart is empty. Cannot checkout."}

        # Verify stock again just before checkout
        sku_counts = {}
        for item in user.cart.items:
            sku_counts[item.sku] = sku_counts.get(item.sku, 0) + 1
            
        for sku, count in sku_counts.items():
            if not self.stock_manager.check_stock(sku, count):
                prod_name = self.stock_manager.get_product(sku).name
                return {"success": False, "message": f"Insufficient stock for {prod_name}."}

        subtotal = user.cart.get_subtotal()
        shipping = user.cart.get_total_shipping()
        tax = subtotal * self.TAX_RATE
        total = subtotal + shipping + tax

        # Simulate complex payment processing logic here...
        payment_successful = True # Mocking a successful payment

        if payment_successful:
            # Deduct stock
            for sku, count in sku_counts.items():
                self.stock_manager.decrement_stock(sku, count)

            order_id = str(uuid.uuid4())[:8].upper()
            receipt = {
                "success": True,
                "order_id": order_id,
                "message": "Payment successful!",
                "user": user.username,
                "subtotal": round(subtotal, 2),
                "shipping": round(shipping, 2),
                "tax": round(tax, 2),
                "total": round(total, 2),
                "items_purchased": len(user.cart.items),
                # We save a deepcopy of the items list for the dashboard history
                "items_details": [item.to_dict() for item in user.cart.items]
            }
            
            # Save receipt to user's past orders
            user.add_order(receipt)
            # Empty cart after successful checkout
            user.cart.clear() 
            
            return receipt
        else:
            return {"success": False, "message": "Payment failed."}
