import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_page_config(page_title="CO2 Emissions", page_icon="🌍")
# Title and dataset details
st.title('Countrywise Production-Based CO2 Emissions')
col1, col2 = st.columns(2)
with col1:
         st.image('./pollution.jpg')
with col2:
         st.write('The Production Based CO2 Emissions Dataset provides valuable insights into the carbon emissions associated with production processes in various industries. Understanding and analyzing these emissions is crucial for businesses and policymakers to develop strategies aimed at reducing environmental impact and fostering sustainable production practices. This dataset captures emissions data related to different production activities, helping stakeholders make informed decisions to mitigate their carbon footprint and contribute to a greener future. Its essential to recognize that this dataset serves as a valuable resource, particularly for those focused on environmental sustainability and climate action. This Synthetic Dataset has been created for educational purposes to aid beginners in understanding and analyzing production-based CO2 emissions.')

st.subheader('Dataset Glossary (Column-wise):')
glossary_points = [
   "ISO3 - ISO 3166-1 alpha-3 code representing the country",
    "Country - Name of the country",
    "Continent - Continent where the country is located",
    "Hemisphere - Hemisphere (Northern or Southern) to which the country belongs",
    "Metric tons of CO2e per capita (1990) - CO2 emissions in metric tons per capita for 1990",
    "Metric tons of CO2e per capita (1995) - CO2 emissions in metric tons per capita for 1995",
    "Metric tons of CO2e per capita (2000) - CO2 emissions in metric tons per capita for 2000",
    "Metric tons of CO2e per capita (2005) - CO2 emissions in metric tons per capita for 2005",
    "Metric tons of CO2e per capita (2010) - CO2 emissions in metric tons per capita for 2010",
    "Metric tons of CO2e per capita (2013) - CO2 emissions in metric tons per capita for 2013",
    "Metric tons of CO2e per capita (2018) - CO2 emissions in metric tons per capita for 2018"
]
# Convert the list to a Markdown-formatted string
glossary_points_str = "\n".join([f"- {item}" for item in glossary_points])
# Display the list with bullet points using st.markdown
st.markdown(glossary_points_str)


# Show dataset
st.subheader('Dataset Details:')
df = pd.read_csv('./final_dataset.csv')
st.write(df)  # Display the first few rows of the dataset
st.write(f'Dataset shape: {df.shape}')

# Visualizations
st.subheader('Visualizations:')

# Bar chart of the top 10 countries with the highest CO2 emissions
top_10 = df.groupby('Country')['Total CO2 Emissions'].sum(
).sort_values(ascending=False).head(10)
top_10_fig = px.bar(df.groupby('Country')['Total CO2 Emissions'].sum().sort_values(ascending=False).head(10), y='Total CO2 Emissions', color='Total CO2 Emissions',
                    text="Total CO2 Emissions", labels={'Country': 'Total CO2 Emissions'}, template='ggplot2', title='Top 10 Countries with the Highest CO2 Emissions')
st.plotly_chart(top_10_fig)


# Group by 'Country' and calculate the sum of 'Total CO2 Emissions' for each country
top_countries = df.groupby('Country')['Total CO2 Emissions'].sum(
).sort_values(ascending=False).head(5)


# Choropleth map of CO2 emissions by country
fig = px.choropleth(df, locations='Country', locationmode='country names', color='Total CO2 Emissions', hover_name='Country',
                    title='Countries with the Highest CO2 Emissions(1990-2018)', color_continuous_scale='Magma', labels={'Total CO2 Emissions': 'CO2 Emissions'})
fig.update_layout(height=500, width=1000, margin=dict(l=20, r=20, t=40, b=20))
st.plotly_chart(fig)






st.write("Top 10 Countries with Highest Total CO2 Emissions")

df = df.sort_values(by='Total CO2 Emissions', ascending=False)
# Create subplots
main_plot_height = 14
main_plot_width = 16

# Create subplots
fig, axes = plt.subplots(5, 2, figsize=(main_plot_width * 2, main_plot_height * 5))
subplot_params = [
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20},
    {"height": 26, "width": 20}

   
]
axes = axes.ravel()





# Plot line charts for the top 10 countries
for i, country in enumerate(df['Country'].head(10)):
    plt.sca(axes[i])
    plt.plot(df.columns[5:-1], df.loc[df['Country'] == country, df.columns[5:-1]].values.ravel(), marker='o', label=country)
    plt.title(f"{country}")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions")
    plt.grid()
    plt.legend()
    plt.gcf().set_size_inches(subplot_params[i]["width"], subplot_params[i]["height"])
# Display the plot in Streamlit
st.pyplot(fig)


bullet_points = [
"The image shows the CO2 emissions of the ten largest emitting countries in the world, from 1990 to 2018. The data shows that Kuwait is the largest emitter of CO2, followed by other countries.",
"The data also shows that CO2 emissions have been declining in recent years ( from 2005/2010) for most of the countries."
]

# Convert the list to a Markdown-formatted string
bullet_points_str = "\n".join([f"- {item}" for item in bullet_points])

# Display the list with bullet points using st.markdown
st.markdown("#### Conclusion")
st.markdown(bullet_points_str)

# Pie charts for CO2 emissions by Hemisphere and Continent

# Group by Continent and calculate the sum of Total CO2 Emissions for each continent
hemisphere_totals = df.groupby('Hemisphere')['Total CO2 Emissions'].sum(
).reset_index().sort_values(by='Total CO2 Emissions', ascending=False)
continent_totals = df.groupby('Continent')['Total CO2 Emissions'].sum(
).reset_index().sort_values(by='Total CO2 Emissions', ascending=False)
matplotlib.use('Agg')


st.write('Total CO2 Emissions in Continent/ Hemisphere (1990-2018)')
# Set seaborn style
sns.set_theme()

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# Plot Continent data
plt.sca(axes[0])
plt.pie(continent_totals['Total CO2 Emissions'],
        labels=continent_totals['Continent'], autopct='%1.1f%%', startangle=90)
plt.title('Total CO2 Emissions by Continent')
# Plot Hemisphere data
plt.sca(axes[1])
plt.pie(hemisphere_totals['Total CO2 Emissions'],
        labels=hemisphere_totals['Hemisphere'], autopct='%1.1f%%', startangle=90)
plt.title('Total CO2 Emissions by Hemisphere')
# Display the plot in Streamlit
st.pyplot(fig)



# Create a list with bullet points
bullet_points = [
"Asia is the largest emitter of CO2, accounting for 35.1% of global emissions",
"North America is the second largest emitter, accounting for 26.4% of global emissions.",
"Europe is the third largest emitter, accounting for 19.4% of global emissions.",
"South America, Africa, and Australia account for the remaining 13.6%, 6.3%, and 12.8% of global emissions, respectively.",
"The Northern Hemisphere is responsible for a significantly larger share of global CO2 emissions (86.4%) than the Southern Hemisphere (13.6%)."
]

# Convert the list to a Markdown-formatted string
bullet_points_str = "\n".join([f"- {item}" for item in bullet_points])

# Display the list with bullet points using st.markdown
st.markdown("#### Conclusion")
st.markdown(bullet_points_str)






# Show the Streamlit app



hide_streamlit_style = """
            <style>
             footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write("""
         
         
         
         
         
         
         
         
         
         """)
st.write('Thank you for exploring the CO2 emissions statistics.')
st.write("Made with `♥`  by `Bro_CODE` Shivnandan Jha")
