## Review Classification

Measuring customer satisfaction is an important part of successful online services. Airbnb, Amazon or Uber leverage precious information contained in customer reviews to predict demand patterns, filter out low quality supply and ever improve their offer.

In this section we want to build a classification model that will inform us, whether a review is a `low_review` or not. We define low reviews as ones with a 1 or 2 `review_score`.

If this model is precise enough, it can help teams focus on at risk orders and target their efforts to manage and improve customer expectations.

### Baseline

**Open `04_02_review_classification.ipynb` and follows instructions (copied below)**

- Retrieve `orders` training_set defined in previous exercises and define a new column `dim_is_low_review`.

👉Hint: `dim_is_low_review` is defined as reviews with 1 or 2 stars.

- What's the probability of getting a low order review?
- Plot side by side distribution plot for each variable contained in `orders` object. What do you observe?

### First Model

We now want to build a classification model to predict whether an order is low review or not.

- Load `orders` training data and split it with a 30% test size in `X_train`, `X_test`, `y_train`, `y_test` and `random_state = 42` so we can compare our results

- Train a classification model with the algorithm of your choice. Evaluate the performance of your model with the following metrics:

  - `confusion_matrix`
  - `accuracy_score`
  - `recall_score`

- Make sure you remove all features that would cause data leaks (review_score, wait_time, etc...)

### More features

**Open file `olist/reviews.py`, add the method `get_training_data`**

It should return the following features available from `olist_order_reviews_dataset`.

    - `review_id` (_str_) _the id of the review_
    - `order_id` (_str_) _the id of the order_
    - `review_comment_length` (_int_) _string length of review comment_
    - `product_category` (_str_) _name of the main category for that review. Main category is defined as the most expensive category in the order_.

**Back to your notebook `04_02_review_classification.ipynb`**

Let's add more features to our model.

- Plot a distribution of `review_comment_length` per `review_score`. What do you observe?

- Fit `model_2`, the same model you used previously, but trained on a training set with those additional features. How much `accuracy` and `recall` do you gain?

### AutoML

Using the library [Tpot](http://epistasislab.github.io/tpot/), find the best model to optimize `dim_is_low_review`.
What is the best `accuracy` and `recall` scores you can achieve?

Make sure you are able to recreate and manipulate the model Tpot suggests you to use. After few minutes of training with Tpot, you should always get a higher score than your linear regression above.
