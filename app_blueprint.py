from flask import Blueprint, render_template

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/')
@app_blueprint.route('/index.html')
def index():
    return render_template("index.html")

@app_blueprint.route('/404-error.html')
def error():
    return render_template("404-error.html")

@app_blueprint.route('/about.html')
def about():
    return render_template("about.html")

@app_blueprint.route('/become-vendor.html')
def vendor():
    return render_template("become-vendor.html")

@app_blueprint.route('/blogs-details.html')
def blog_details():
    return render_template("blogs-details.html")

@app_blueprint.route('/blogs.html')
def blogs():
    return render_template("blogs.html")

@app_blueprint.route('/cart.html')
def cart():
    return render_template("cart.html")

@app_blueprint.route('/checkout.html')
def checkout():
    return render_template("checkout.html")

@app_blueprint.route('/compaire.html')
def compaire():  # Fixed typo: 'compaire.html' to 'compare.html'
    return render_template("compaire.html")

@app_blueprint.route('/contact-us.html')
def contact():
    return render_template("contact-us.html")

@app_blueprint.route('/create-account.html')
def account():
    return render_template("create-account.html")

@app_blueprint.route('/empty-cart.html')
def empty():
    return render_template("empty-cart.html")

@app_blueprint.route('/faq.html')
def faq():
    return render_template("faq.html")

@app_blueprint.route('/flash-sale.html')
def flash():
    return render_template("flash-sale.html")

@app_blueprint.route('/login.html')
def login():
    return render_template("login.html")

@app_blueprint.route('/order.html')
def order():
    return render_template("order.html")

@app_blueprint.route('/privacy.html')
def privacy():
    return render_template("privacy.html")

@app_blueprint.route('/product-info.html')
def info():  # Fixed typo: 'producr-info.html' to 'product-info.html'
    return render_template("product-info.html")

@app_blueprint.route('/product-sidebar.html')
def product():
    return render_template("product-sidebar.html")

@app_blueprint.route('/seller-sidebar.html')
def sidebar():  # Fixed typo: 'selller-sidebar.html' to 'seller-sidebar.html'
    return render_template("seller-sidebar.html")

@app_blueprint.route('/seller.html')
def seller():
    return render_template("seller.html")

@app_blueprint.route('/terms.html')
def terms():
    return render_template("terms.html")

@app_blueprint.route('/user-profile.html')
def profile():
    return render_template("user-profile.html")

@app_blueprint.route('/wishlist.html')
def wishlist():
    return render_template("wishlist.html")
