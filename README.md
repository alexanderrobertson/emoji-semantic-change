# Emoji semantic

Code and data for https://emoji-semantic-change.herokuapp.com/

Simple dashboard made in Dash.

## `change.csv`

Monthly semantic change score for emoji. The anchor point for calculating semantic change is usually 01/01/2012 (the first data point for such emoji will be 2012-02-01). For newer emoji, or those with missing data, the anchor point is the date of the blank line preceding the first non-blank line. For example, the anchor point for 🌼 is 2013-05-01.

Semantic scores are provided in two formats: smoothed and z-normed.

The cluster assigned to each emoji (if there is one - not all emoji were clustered due to lack of data) is also given.

## `year_list.csv`

For each emoji, for each year, shows the top 15 most similar words by cosine similarity.

This data is generated from Twitter content, so be prepared for terms you might find offensive!

## `month_list.csv`

For each emoji, for each month, shows the top 15 most similar words by cosine similarity.

Monthly data is calculated using aggregate data across all years. So the top 15 most similar words for 🌀 in January is based on lemmatised word frequencies for January in 2012, 2013 and so on until 2018.

This data is generated from Twitter content, so be prepared for terms you might find offensive!

##`nn_sim.csv`

For each emoji, in a given month, shows the mean cosine similarity to that emoji's 500 nearest neighbours, along with upper/lower bounds on 95% confidence intervals. (This data is not used by the dashboard and didn't make it into the paper!)