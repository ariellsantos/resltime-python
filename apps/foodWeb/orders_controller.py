from flask import Flask, render_template


def index():
    return render_template('admin/orders/index.html')

