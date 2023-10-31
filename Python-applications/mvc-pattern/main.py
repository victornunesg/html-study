from model_view_controller import Controller, ModelBasic, View

# my_items = [
#     {'name': 'bread', 'price': 0.5, 'quantity': 20},
#     {'name': 'milk', 'price': 1.0, 'quantity': 10},
#     {'name': 'wine', 'price': 10.0, 'quantity': 5},
# ]

my_items = list()
c = Controller(ModelBasic(my_items), View())
c.show_items()
c.show_items(bullet_points=True)
