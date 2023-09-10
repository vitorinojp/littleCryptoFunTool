import os
import secrets
import string

word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apricot", "blueberry",
    "cantaloupe", "cranberry", "grapefruit", "guava", "lime", "papaya", "peach", "pineapple", "plum", "pomegranate",
    "blackberry", "boysenberry", "currant", "kiwifruit", "nectarine", "passionfruit", "rhubarb", "tamarind",
    "persimmon", "mulberry",
    "avocado", "coconut", "olive", "guarana", "cucumber", "pumpkin", "eggplant", "zucchini", "tomato", "bell-pepper",
    "carrot", "broccoli", "cauliflower", "cabbage", "spinach", "lettuce", "potato", "onion", "garlic", "ginger",
    "turmeric", "cinnamon", "nutmeg", "coriander", "cumin", "basil", "oregano", "thyme", "rosemary", "parsley",
    "dill", "tarragon", "bayleaf", "cloves", "saffron", "vanilla", "chocolate", "caramel", "butterscotch",
    "marshmallow",
    "peanut", "almond", "cashew", "pecan", "walnut", "hazelnut", "macadamia", "pistachio", "coconut", "sesame",
    "sunflower", "flaxseed", "chia", "poppyseed", "oatmeal", "barley", "quinoa", "couscous", "bulgur", "rice",
    "pasta", "bread", "baguette", "croissant", "muffin", "pancake", "waffle", "toast", "sandwich", "hamburger",
    "hotdog", "pizza", "lasagna", "spaghetti", "sushi", "tempura", "sashimi", "rice", "noodle", "stew",
    "soup", "salad", "appetizer", "dessert", "beverage", "water", "juice"
]


def choose_word() -> str:
    return word_list[os.urandom(1)[0] % len(word_list)]


def choose_pin(size=6) -> str:
    return ''.join(secrets.choice(string.digits) for i in range(size))


def generate_password(size=8) -> str:
    return "-".join([choose_word() for _ in range(size - 1)]) + "-" + choose_pin()
