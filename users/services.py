import stripe
from config.settings import SECRET_KEY_STRIPE

stripe.api_key = SECRET_KEY_STRIPE


def create_stripe_product(product):
    """ Создание продукта """

    if product.payment_course is None:
        lesson = product.payment_lesson
        product_create = stripe.Product.create(name="lesson")
    else:
        course = product.payment_course
        product_create = stripe.Product.create(name="course")
    return product_create.get("id")


def create_stripe_payment(summ_payment, amount_id):
    """ Создание платежа """

    return stripe.Price.create(
        currency="rub",
        unit_amount=summ_payment * 100,
        product_data={"name": amount_id},
    )


def create_stripe_url(amount):
    """ Создание ссылки на оплату """

    session_payment = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/users/payment/",
        line_items=[{"price": amount.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session_payment.get("id"), session_payment.get("url")
