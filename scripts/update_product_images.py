#!/usr/bin/env python3
"""
Update all product images to use uniform nourishing face oil image
"""

from app import create_app, db
from app.models import Product


def update_product_images():
    """Update all product images to use the same uniform image"""
    app = create_app()
    with app.app_context():
        products = Product.query.all()

        for product in products:
            product.image_main = 'static/images/nourishing-face-oil.jpg'
            product.image_hover = 'static/images/nourishing-face-oil.jpg'

        db.session.commit()
        print(f"Updated {len(products)} products to use uniform image")


if __name__ == '__main__':
    update_product_images()