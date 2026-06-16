from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from models import AuthManager, StockManager, PaymentProcessor, PhysicalProduct, DigitalProduct
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # Required for session management and flash messages

# ==========================================
# Initialize Managers (Singletons for this demo)
# ==========================================
auth_manager = AuthManager()
stock_manager = StockManager()
payment_processor = PaymentProcessor(stock_manager)

# Pre-load users
auth_manager.register("DeveloperPro", "dev@example.com", "password123")

from products_data import load_mock_products
load_mock_products(stock_manager)

# ==========================================
# Helper to get current user
# ==========================================
def get_current_user():
    if 'username' in session:
        return auth_manager.get_user(session['username'])
    return None

# ==========================================
# Authentication Routes
# ==========================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = auth_manager.authenticate(username, password)
        if user:
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "error")
    return render_template('auth.html', mode='login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if auth_manager.register(username, email, password):
            session['username'] = username # Auto-login
            return redirect(url_for('index'))
        else:
            flash("Username already exists.", "error")
    return render_template('auth.html', mode='signup')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# ==========================================
# Storefront Routes
# ==========================================

@app.route('/')
def index():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    query = request.args.get('q', '').lower()
    products = stock_manager.get_all_products()
    
    if query:
        products = [p for p in products if query in p.name.lower()]
        
    return render_template('index.html', user=user, products=products, query=query)

@app.route('/product/<sku>')
def product_detail(sku):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    product = stock_manager.get_product(sku)
    if not product:
        flash("Product not found.", "error")
        return redirect(url_for('index'))
        
    return render_template('product_detail.html', user=user, product=product)

# ==========================================
# Cart & Checkout Routes
# ==========================================

@app.route('/cart')
def cart():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    cart_details = user.cart.get_cart_details()
    tax = cart_details['subtotal'] * PaymentProcessor.TAX_RATE
    total = cart_details['subtotal'] + cart_details['total_shipping'] + tax
    
    summary = {
        "subtotal": round(cart_details['subtotal'], 2),
        "shipping": round(cart_details['total_shipping'], 2),
        "tax": round(tax, 2),
        "total": round(total, 2)
    }
        
    return render_template('cart.html', user=user, items=user.cart.items, summary=summary)

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    user = get_current_user()
    if not user:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    data = request.json
    sku = data.get('sku')
    
    product = stock_manager.get_product(sku)
    if not product:
        return jsonify({"success": False, "message": "Product not found."}), 404
        
    # Check current stock vs what's already in the cart
    in_cart_count = sum(1 for item in user.cart.items if item.sku == sku)
    if not stock_manager.check_stock(sku, in_cart_count + 1):
        return jsonify({"success": False, "message": "Out of stock."}), 400

    user.cart.add_item(product)
    return jsonify({
        "success": True, 
        "message": f"{product.name} added to cart.",
        "cart_count": len(user.cart.items)
    })
    
@app.route('/api/cart/remove', methods=['POST'])
def remove_from_cart():
    user = get_current_user()
    if not user:
        return jsonify({"success": False}), 401
    
    sku = request.json.get('sku')
    if user.cart.remove_item(sku):
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/checkout', methods=['POST'])
def checkout():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    result = payment_processor.checkout(user)
    if result.get("success"):
        # Save result in session to pass to success page
        session['last_receipt'] = result
        return redirect(url_for('success'))
    else:
        flash(result.get("message", "Checkout failed."), "error")
        return redirect(url_for('cart'))

@app.route('/success')
def success():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    receipt = session.get('last_receipt')
    if not receipt:
        return redirect(url_for('index'))
        
    return render_template('success.html', user=user, receipt=receipt)

# ==========================================
# Dashboard Routes
# ==========================================

@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
