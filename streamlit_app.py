# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
# from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)

name_on_order = st.text_input('Name on Smoothie: ')
st.write('The name on your smoothie will be - ', name_on_order)
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose upto 5 ingredients:', my_dataframe)

if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    # st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

    # if ingredients_string:
    #     session.sql(my_insert_stmt).collect()

        st.success('Your smoothie is ordered!')

og_dataset = session.table("smoothies.public.orders")
edited_dataset = session.create_dataframe(editable_df)
og_dataset.merge(edited_dataset, (og_dataset['ORDER_UID'] == edited_dataset['ORDER_UID']), [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
                    )
