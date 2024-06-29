import pandas as pd

last_review = pd.read_csv("NYC_Airbnb/airbnb_last_review.csv")
price = pd.read_csv("NYC_Airbnb/airbnb_price.csv")
roomtype = pd.read_excel('NYC_Airbnb/airbnb_room_type.xlsx')

last_review_df = pd.DataFrame(last_review)
price_df = pd.DataFrame(price)
roomtype_df =pd.DataFrame(roomtype)

# roomtype_df.set_index('listing_id').join(price_df.set_index('listing_id')).head(5)
roomtype_df.join(price_df.set_index('listing_id'), on='listing_id').head(5)

#commented code below makes the last two columns NaN
#roomtype_df.join(price_df.set_index('listing_id'), on='listing_id').join(last_review_df.set_index(' listing_id')).head(5)
rp = roomtype_df.set_index('listing_id').join(price_df.set_index('listing_id')).join(last_review_df.set_index(' listing_id')).head(5)

#identify NAN
rp.isna().sum()

null_mask = rp.isnull().all(axis=1)
null_rows = rp[null_mask]
print(null_rows.count())