# CRUD API ON NODE.JS

With this simple api we can register, get, update and delete items with name, price and description.

## Dependencies

this node.js application requires mongodb and express

### How it works

Get: Can either be made in /api/products to fetch all documents. Or on /api/products/name for a specific product

Post: must be sent to /api/products with params name,desc and price

Put: same as post, but update a single product at /api/products/name

delete: Same as put, but no params
