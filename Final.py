"""
Class: CS230--Section 004 
Name: Mason Matos
Description: Final Project
I pledge that I have completed the programming assignment independently. 
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
import streamlit as st
import pandas as pd
import csv
import matplotlib.pyplot as plt


def page0():  # Home page
    st.image("cambridge.jpg")
    st.title("Cambridge Properties")
    st.header("CS230 Final Project - Mason Matos")
    st.write("This application will provide extensive knowledge on Cambridge properties. This will include"
             " a map of the properties, price selection, size selection, and a mortgage plan for purchase.")


def get_data():  # Get the data
    df = pd.read_csv("Cambridge_Property_Database_FY2022.csv",
                     header=0,
                     names=["Address", "latitude", "longitude", "Property Class",
                            "Land_Area", "Value", "Style",
                            "Bedrooms", "Kitchen", "Bathroom", "Half Bathrooms",
                            "Fireplaces", "Laundry", "Property Tax"])
    return df


def filter_bedrooms(df, number_bedrooms):
    filtered = (df["Bedrooms"] == number_bedrooms)
    df_bedroom_filter = df.loc[filtered]
    return df_bedroom_filter


def filter_bathrooms(df, number_bathrooms):
    filtered = (df["Bathroom"] == number_bathrooms)
    df_bathroom_filter = df.loc[filtered]
    return df_bathroom_filter


def filter_price(df, maximum_price):  # Function to filter data by price
    filtered = (df["Value"] < maximum_price)  # Create a filter
    df_price_filter = df.loc[filtered]
    return df_price_filter


def filter_prop(df, property_choices):  # Function to filter data by property type
    if not property_choices:
        df_property_filter = df
    else:  # Filtered by the property type
        df_property_filter = df[df["Property Class"].isin(property_choices)]
    return df_property_filter


def bar_chart():  # bar chart
    df = get_data()
    filtered_property = df.query("Bedrooms == 1")
    average_price_1 = filtered_property["Value"].mean()

    filtered_property = df.query("Bedrooms == 2")
    average_price_2 = filtered_property["Value"].mean()

    filtered_property = df.query("Bedrooms == 3")
    average_price_3 = filtered_property["Value"].mean()

    filtered_property = df.query("Bedrooms == 4")
    average_price_4 = filtered_property["Value"].mean()

    data = [average_price_1,average_price_2,average_price_3,average_price_4,]
    bedrooms = ["1", "2", "3", "4"]
    plt.bar(bedrooms, data, color='red')
    plt.xlabel("Number of Bedrooms")
    plt.ylabel("Average Value in Millions")
    plt.title("Property Value and Bedrooms Relationship")
    plt.grid(color="gray", linestyle="-.", linewidth=.25)
    st.pyplot(plt, clear_figure=True)


def line_chart():  # area chart
    df = get_data()

    filtered_property = df.query("Fireplaces == 0")
    average_price_1 = filtered_property["Value"].mean()

    filtered_property = df.query("Fireplaces == 1")
    average_price_2 = filtered_property["Value"].mean()

    filtered_property = df.query("Fireplaces == 2")
    average_price_3 = filtered_property["Value"].mean()

    filtered_property = df.query("Fireplaces == 3")
    average_price_4 = filtered_property["Value"].mean()

    data = [average_price_1,average_price_2,average_price_3,average_price_4,]
    fireplace = ["0", "1", "2", "3"]
    plt.plot(fireplace, data, color='red')
    plt.xlabel("Number of Fireplaces")
    plt.ylabel("Average Property Value in Millions")
    plt.title("Property Value and Fireplace Relationship")
    plt.grid(color="gray", linestyle="-.", linewidth=.25)
    st.pyplot(plt, clear_figure=True)


def hist_chart():  # line chart
    df = get_data()
    filtered_property = df.query("Land_Area >= 0 & Land_Area <=2000")
    average_price_1 = filtered_property["Value"].mean()

    filtered_property = df.query("Land_Area >= 2001 & Land_Area <=4000")
    average_price_2 = filtered_property["Value"].mean()

    filtered_property = df.query("Land_Area >= 4001 & Land_Area <=6000")
    average_price_3 = filtered_property["Value"].mean()

    filtered_property = df.query("Land_Area >= 6001 & Land_Area <=8000")
    average_price_4 = filtered_property["Value"].mean()

    filtered_property = df.query("Land_Area >= 8001 & Land_Area <=10000")
    average_price_5 = filtered_property["Value"].mean()

    data2 = [average_price_1, average_price_2, average_price_3, average_price_4, average_price_5]
    land = ["0-2", "2-4", "4-6", "6-8", "8-10"]
    plt.barh(land, data2, color='red')
    plt.title("Property Value and Land Relationship")
    plt.ylabel("Land (1000s Sqft)")
    plt.xlabel("Average Value in Millions")
    plt.grid(color="gray", linestyle="-.", linewidth=.25)
    st.pyplot(plt, clear_figure=True)


def page1():  # map page
    df = get_data()
    col1, buffer, col2 = st.columns([9, 1, 20])
    property_types = []
    for t in df["Property Class"]:
        if t not in property_types:
            property_types.append(t)

    with col1:  # Left narrow column
        st.header("Filters")
        st.write("Filter by both the price point and the property type.")
        maximum_price = st.slider("Max Price:", max_value=10000000, step=10000, value=200000)

        property_types.append("All")
        prop_choices = st.multiselect("Select property type:", property_types)

    with col2:
        st.header("Map of Cambridge Properties")
        df_property_filter = filter_prop(df, prop_choices)  # Filters by property type
        df2 = pd.DataFrame(df_property_filter[["latitude", "longitude", "Value"]])
        df2 = df2.apply(pd.to_numeric, errors='coerce')
        df2 = df2.dropna()
        df_price_filter = filter_price(df2, maximum_price)  # Filters by price
        st.map(df_price_filter)


def page2():
    st.title("How to increase property value?")
    bar_chart()
    line_chart()
    hist_chart()
    st.subheader("In Summary")
    st.write("If you want a property with high value the solution is simple. "
             "Buy a lot of land, put a lot of fireplaces, and add a lot of bedrooms.")


def page3():
    df = get_data()
    col1, buffer, col2 = st.columns([9, 1, 20])
    property_types = []
    for t in df["Property Class"]:
        if t not in property_types:
            property_types.append(t)

    with col1:  # Left narrow column
        st.header("Filters")
        property_types.append("All")
        prop_choices = st.multiselect("Select property type:", property_types)
        number_bedrooms = st.slider("Number of bedrooms:", min_value=1, max_value=10, value=1)
        number_bathrooms = st.slider("Number of bathrooms:", min_value=1, max_value=10, value=1)

    with col2:
        st.header("Table of Filtered Properties")
        df_property_filter = filter_prop(df, prop_choices)  # Filters by property type
        df2 = pd.DataFrame(df_property_filter[["Property Class", "Bedrooms", "Bathroom", "Value"]])
        df_bedroom_filter = filter_bedrooms(df2, number_bedrooms)
        df_bathroom_filter = filter_bathrooms(df_bedroom_filter, number_bathrooms)
        average_price = df_bathroom_filter["Value"].mean().round(2)
        # df2 = df2.apply(pd.to_numeric, errors='coerce')
        # df2 = df2.dropna()
        st.write(df_bathroom_filter)
        st.header("Mortgage Calculator")
        st.write("The average price of a property with the selected features:")
        st.write(average_price)
        mortgage_rate = st.slider("Mortgage rate:", min_value=1.0, max_value=6.0, value=5.0, step=0.25)
        mortgage_types = ["15 year", "30 year"]
        mortgage_type = st.radio("What type of mortgage", mortgage_types)
        if mortgage_type == '15 year':
            months = 15 * 12
        elif mortgage_type == '30 year':
            months = 30 * 12
        mortgage_payment = average_price * (1 + (mortgage_rate/100)) ** (months/12) / months
        st.write("The mortgage payments for the average property with the selected features:")
        st.write(mortgage_payment.round(2))


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Map", "Charts", "Mortgage Calculator"])
    if selection == "Home":
        page0()
    if selection == "Map":
        page1()
    if selection == "Charts":
        page2()
    if selection == "Mortgage Calculator":
        page3()


main()
