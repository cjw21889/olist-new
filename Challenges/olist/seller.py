import pandas as pd
import numpy as np
from olist.data import Olist
from olist.order import Order


class Seller:
    def __init__(self):
        # Import data only once
        olist = Olist()
        self.data = olist.get_data()
        self.matching_table = olist.get_matching_table()
        self.order = Order()

    def get_seller_features(self):
        """
        Returns a DataFrame with:
        'seller_id', 'seller_city', 'seller_state'
        """
        pass  # YOUR CODE HERE

    def get_seller_delay_wait_time(self):
        """
        Returns a DataFrame with:
        'seller_id', 'delay_to_carrier', 'wait_time'
        """
        pass  # YOUR CODE HERE

    def get_active_dates(self):
        """
        Returns a DataFrame with:
        'seller_id', 'date_first_sale', 'date_last_sale'
        """
        pass  # YOUR CODE HERE

    def get_review_score(self):
        """
        Returns a DataFrame with:
        'seller_id', 'share_of_five_stars', 'share_of_one_stars', 'review_score'
        """
        pass  # YOUR CODE HERE

    def get_quantity(self):
        """
        Returns a DataFrame with:
        'seller_id', 'n_orders', 'quantity', 'quantity_per_order'
        """
        # Hint: Here, you cannot start from the `matching_table`
        pass  # YOUR CODE HERE

    def get_sales(self):
        """
        Returns a DataFrame with:
        'seller_id', 'sales'
        """
        pass  # YOUR CODE HERE

    def get_training_data(self):
        """
        Returns a DataFrame with:
        ['seller_id', 'seller_city', 'seller_state', 'delay_to_carrier',
        'wait_time', 'date_first_sale', 'date_last_sale', 'share_of_one_stars',
        'share_of_five_stars', 'review_score', 'n_orders', 'quantity',
        'quantity_per_order', 'sales']
        """
        pass  # YOUR CODE HERE
