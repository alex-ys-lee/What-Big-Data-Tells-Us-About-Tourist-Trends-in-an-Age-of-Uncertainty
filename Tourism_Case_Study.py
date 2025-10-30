#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 21:21:25 2025

@author: boredom
"""

import pandas as pd
import numpy as np
import plotly.express as px
import json
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")


mypath = ''

tourism = pd.read_csv(mypath + 'tour_econ_df.csv')

tourism['year'] = tourism['year'].astype('category')

tourism.sort_values(['country', 'year'], inplace=True)

regions_list = ["Europe and Central Asia", "Sub-Saharan Africa", "Latin America and Caribbean", "East Asia and Pacific:", "Middle East", "North Africa", "South Asia", "North America"]

full_num_dict = {'international_em' : 'Intl Emissions', 
            'domestic_em' : 'Domestic Emissions', 
            'total_em' : 'Total Emissions', 
            'year' : 'Year',
            "empl_tour_1000" : "Tourism Employment (Per 1000 People)",
            "tour_prop_total" : "Tourism GDP : Total GDP",
            "length" : "Length of Stay",
            "empl_serv_1000" : "Serving Employment (Per 1000 People)",
            "guests" : "Guests",
            "arv_1000" : "Arrivals (Per 1000 People)",
            "dep_tourists" : "Departing_Tourists",
            "tourists_per_1000" : "Tourists per 1000 People",
            "domestic_trips_1000" : "Domestic Trips (Per 1000 People)",
            "purpose_biz_profesh" : "Purpose of Travel",
            "int_dep" : "International Departures"
            }

temp_num_dict = {'year' : 'Year',
                 "gdp" : "GDP Per Capita",
                 "length" : "Length of Stay",
                 "arv_1000" : "Arrivals (Per 1000 People)",
                 "purpose_biz_profesh" : "Number of Business Travelers",
                 "tourists_per_1000" : "Tourists per 1000 People"
                 }

num_dict = temp_num_dict

full_cat_dict = {'country' : 'Country',
            'region' : 'Region', 
            'month' : 'Month', 
            'weekday' : 'Weekday',
            'decade' : 'Decade'
            }
temp_cat_dict = {'country' : 'Country',
            'region' : 'Region',
            'decade' : 'Decade',
            'length_cat' : 'Length of Stay Levels',
            'arv_cat' : 'Incoming Arrival Levels',
            'gdp_cat' : 'GDP Per Capita Levels'
            }
cat_dict = temp_cat_dict

all_dict = num_dict.copy()
all_dict.update(cat_dict)

range_mean_dict = {'tourists_per_1000' : [1, 300],
                    'gdp' : [800, 40000],
                    'length' : [1, 9],
                    'arv_1000' : [1, 300],
                    'purpose_biz_profesh' : [100, 4500000] 
                    }
range_sum_dict = {'tourists_per_1000' : [1, 10000],
                    'gdp' : [1, 1000000],
                    'length' : [1, 150],
                    'arv_1000' : [1, 1500],
                    'purpose_biz_profesh' : [1, 100000000] 
                    }





with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation Pane',
		options = ['Abstract', 'Background Information', 'Data Cleaning','Exploratory Analysis', 'Decennial Impact of Tourism', 'Regional Impact of Tourism', 'Progressive Impact of Tourism', 'Conclusion', 'Bibliography'],
		menu_icon = 'list',
		icons = ['bookmark-check', 'book', 'box', 'map', 'map', 'file', 'map', 'bar-chart', 'check2-circle'],
		default_index = 0,
		)


if selected=='Abstract':
    st.title("Tourism Intensity, Duration, and Return: Global Patterns 1995–2020")
    
    st.markdown('Tourism is a vital component of global economies, significantly influencing gross domestic product (GDP), employment, and regional development through visitor spending and infrastructure growth. Many countries and regions thrive on tourism, but what are the key factors that drive its economic impact? Why do some destinations generate greater economic benefits than others? This case study leverages a comprehensive dataset to explore the scientific and economic factors behind tourism’s influence, examining correlations between GDP, tourist arrivals, length of stay, and regional variations. By analyzing data from 1995 to 2020, this study aims to uncover patterns that explain tourism’s economic contributions, identify the factors that enhance economic outcomes, and understand regional differences in tourism-driven growth. Let’s dive into the data to reveal the dynamics of tourism’s economic impact!')
    
    st.subheader('Questions to be Answered')
    
    st.markdown('To what extent does the length of tourist stay reflect GDP per capita, and why do certain low-income regions—particularly in Sub-Saharan Africa and South Asia—consistently defy this trend with longer average stays?')

    st.markdown('How do small island developing states (SIDS) achieve disproportionately high tourism arrival intensities despite limited land area and population—and what does this reveal about the scalability of tourism-led development?')
    
    st.markdown('Are high-income countries becoming "tourism-saturated", as suggested by declining growth rates in arrivals per 1000 people after 2010, while emerging economies in Southeast Asia and the Middle East accelerate rapidly?')

    st.markdown('What underlying geopolitical, infrastructural, and marketing factors explain why some landlocked, low-GDP nations (e.g., Nepal, Eswatini) outperform coastal peers in tourism density—and can these models be replicated?')
    
    st.markdown('Does the sharp decline in tourism metrics across nearly all countries in 2020 represent a structural reset in global travel behavior, or merely a temporary shock—and how do pre- and post-pandemic trajectories differ by region and income level?')

    st.markdown('Which countries dominate inbound versus outbound tourism flows, and what do imbalances in this ratio reveal about global economic inequality, cultural influence, and mobility privilege?')
    
    st.markdown('<h1><b>WORK IN PROGRESS</b></h1>', unsafe_allow_html=True)
    
    st.markdown('<h4>Please comeback in 2-3 months to view the final version.</h4>', unsafe_allow_html=True)





















if selected=="Background Information":
    st.title("Background Information")
    
    st.markdown('Tourism is a significant driver of global economic activity, contributing substantially to gross domestic product (GDP), employment, and regional development. In 2024, the global travel and tourism sector accounted for approximately 10% of global GDP (US$10.9 trillion) and supported 357 million jobs worldwide, according to the World Travel & Tourism Council (WTTC). The economic impact of tourism is often measured through its direct contributions, such as tourist spending, and indirect effects, including job creation and infrastructure development, with strong correlations to tourist arrivals, length of stay, and regional economic performance.')
    
    st.markdown('The dataset for this study includes economic indicators from various countries and regions, covering metrics such as GDP contribution from tourism, international tourist arrivals, average length of stay, and yearly trends from 1995 to 2020. Each data point reflects a specific country or region, detailing tourist arrivals (e.g., 1.3 billion globally in 2023), tourism’s share of GDP (e.g., 9.1% globally in 2023), and regional variations, such as the Middle East’s 22% increase in arrivals compared to pre-pandemic levels. These metrics allow for an analysis of how tourism influences economic growth and how factors like tourist arrivals and length of stay correlate with GDP.')
    
    st.markdown('Previous studies provide insights into these correlations. According to the WTTC (2021), countries with high tourist arrivals, such as the United States, China, and France (100 million arrivals in 2023), show significant GDP contributions from tourism, with international visitor spending reaching US$1.9 trillion globally in 2024. A study by Nhamo et al. (2021) found that a 1% increase in tourism receipts per capita boosts GDP per capita by 0.31% in the long run, with stronger effects in tourism-specialized countries like Barbados and Seychelles. This suggests that tourist arrivals and spending are key drivers of economic growth, particularly in tourism-dependent regions.')
    
    st.markdown('Furthermore, a 2022 study by Fahimi et al. identified bidirectional causality between tourism and GDP in 105 countries, with regions like Europe and the Americas showing stronger correlations due to high tourist arrivals (2010–2017 data). The study noted that economic growth also boosts tourism, creating a feedback loop. For instance, countries with higher GDP growth often invest in tourism infrastructure, attracting more visitors. Brida et al. (2020) highlighted that countries with high tourist arrivals per capita, such as Uruguay, exhibit stronger GDP growth compared to less tourism-intensive countries like Brazil.')
    
    st.markdown('The length of stay also plays a role in economic impact. According to the World Bank (2020), longer tourist stays correlate with higher spending, which directly boosts GDP and job creation, particularly in small island nations like Sierra Leone, where tourism doubled arrivals and created 17,000 jobs. UN Tourism (2024) reported that regions with extended visitor stays, such as the Middle East, saw faster economic recovery post-pandemic, with tourism direct GDP reaching US$3.3 trillion in 2023. These findings suggest that length of stay and tourist arrivals are critical factors in maximizing economic benefits.')
    
    st.markdown('This case study aims to analyze the 1995–2020 trends in tourism’s economic impact, testing correlations between tourist arrivals, length of stay, GDP, and regional differences. It will explore whether countries with higher arrivals and longer stays continue to see stronger GDP contributions, and how regional variations influence these outcomes, building on the insights from prior studies.')









































if selected=='Data Cleaning':
    st.title('Data Cleaning')
    
    st.markdown('This block initializes two empty DataFrames to later store tourism data by country and region, then creates a dictionary mapping variable names to their respective pre-loaded DataFrames. It concatenates all DataFrames to extract unique country-code pairs, separates entries with missing codes (treated as regions), and creates a clean country-to-code lookup table by dropping nulls and setting the code as the index for efficient mapping.')
    
    country_codes = '''
    tourism = pd.DataFrame(columns=['country', 'code', 'year'])
    tourism_regions = pd.DataFrame(columns=['country', 'code', 'year'])
    dataframes = {
        "empl_tour_1000" : empl_tour_1000,
        "tour_gdp" : tour_gdp,
        "avg_stay" : avg_stay,
        "empl_serv_1000" :empl_serv_1000,
        "guests" :guests,
        "vist_1000" :vist_1000,
        "int_dep" : int_dep,
        "dep_gdp" : dep_gdp,
        "expd_int" : expd_int,
        "expd_out" : expd_out,
        "int_1000" : int_1000,
        "int_bus" : int_bus,
        "em_c" : em_c_year,
        "dep_1000" : dep_1000,
        "dom_1000" : dom_1000
    }
    
    unique_countries=pd.concat(dataframes)[['code', 'country']].drop_duplicates()
    unique_region=unique_countries.loc[unique_countries['code'].isnull(), 'country']
    country_code = unique_countries.dropna()
    country_code.set_index('code', inplace=True)'''
    
    st.code(country_codes, language='python')
    
    st.markdown('This block iterates through each DataFrame in the "dataframes" dictionary, adds a "data_source" column to track its origin, and splits entries into regions (no code) or countries (with code). It drops the "code" column for regions and the "country" column for countries to standardize, then concatenates all regional and country-specific rows into separate DataFrames: "tourism_regions" and "tourism_country".')

    concat = '''
    tour_region_list = []
    tour_country_list = []
    
    for source, df in dataframes.items():
        df.loc[:, 'data_source'] = source
        tour_region_list.append(df[df['country'].isin(unique_region)].drop('code', axis=1))
        tour_country_list.append(df[~df['country'].isin(unique_region)].drop('country', axis=1))

    
    tourism_regions = pd.concat(tour_region_list, axis = 0, ignore_index=True)
    tourism_country = pd.concat(tour_country_list, axis = 0, ignore_index=True)'''
    
    st.code(concat, language='python')
    
    st.markdown('This block reshapes the country-level tourism data: first, it melts the wide-format "tourism_country" DataFrame into long format using key identifiers, dropping rows with missing values. It then pivots back to wide format (excluding "data_source") to create a clean multi-metric structure per country-year. Column names are flattened and cleaned. A second pivot retains "data_source" to track metric availability and identify missing data patterns in "tourism_country_missing".')
    
    dataset = '''
    tourism_country_melt = pd.melt(tourism_country, id_vars=["country", "region", "code", "year", "data_source"], var_name="tourism_metrics").dropna(subset='value')
    
    tourism_country = pd.pivot(tourism_country_melt.drop('data_source', axis=1), index=['country', 'code', 'year', 'region'], columns='tourism_metrics').reset_index()
    tourism_country.columns = pd.Series(tourism_country.columns.get_level_values(level=0)+tourism_country.columns.get_level_values(level=1)).str.replace('value', '')

    tourism_country_missing = pd.pivot(tourism_country_melt, index=['country', 'code', 'year', 'region', 'data_source'], columns='tourism_metrics').reset_index()
    tourism_country_missing.columns = pd.Series(tourism_country_missing.columns.get_level_values(level=0)+tourism_country_missing.columns.get_level_values(level=1)).str.replace('value', '')'''
    
    st.code(dataset, language='python')
    
    st.markdown('This block categorizes the "year" column into decades (1990s–2020s) using predefined bins and right-inclusive intervals, adds a "decade" column, removes rows with missing "gdp" values, and displays the updated DataFrame structure with .info() to verify the changes.')
    
    decade = '''
    decade_bins=[1990, 2000, 2010, 2020, 2030]
    decade_labels=["1990s", "2000s", "2010s", "2020s"]decade = pd.cut(tourism_country["year"], bins=decade_bins, right=True, labels=decade_labels)
    
    tourism_country["decade"] = decade
    tourism_country.dropna(subset="gdp", inplace=True)
    tourism_country.info()'''
    
    st.code(decade, language="python")
    
    st.markdown('This block defines length-of-stay bins in days and categorizes the "length" column into tiers from "very_short" (1–3 days) to "very_long" (23+ days) using left-inclusive intervals, then assigns the resulting categories to a new "length_cat" column and returns the series.')
    
    length = '''
    length_bins = [1, 3, 5, 10, 23, float("inf")]
    length_labels = ["very_short", "short", "medium", "long", "very_long"]
    length_cat = pd.cut(tourism_country["length"], bins=length_bins, right=False, labels=length_labels)
    
    tourism_country["length_cat"] = length_cat
    tourism_country["length_cat"]'''
    
    st.code(length, language="python")
    
    st.markdown('This block classifies annual tourist arrivals (in thousands) into volume tiers from "very Low" (0–20k) to "very high" (>1M) using right-inclusive bins on the "arv_1000" column, creating a categorical "arv_cat" column to reflect tourism inflow intensity.')
    
    arrivals = '''
    arv_bins = [0, 20, 100, 450, 1000, float("inf")]
    arv_labels = ["very Low", "low", "moderate", "high", "very high"]
    arv_cat = pd.cut(tourism_country["arv_1000"], bins=arv_bins, right=True, labels=arv_labels)
    tourism_country["arv_cat"] = arv_cat'''
    
    st.code(arrivals, language="python")
    
    st.markdown('This block groups countries by GDP per capita into income levels from "very low" (<4k) to "very high" (>70k) using right-inclusive bins on the "gdp" column, assigning each to a "gdp_cat" category for socioeconomic analysis.')
    
    gdp = '''
    gdp_bins = [0, 4000, 10000, 30000, 70000, float("inf")]
    gdp_labels = ["very low", "low", "middle", "high", "very high"]
    gdp_cat = pd.cut(tourism_country["gdp"], bins=gdp_bins, right=True, labels=gdp_labels)
    tourism_country["gdp_cat"] = gdp_cat'''
    
    st.code(gdp, language="python")


    
    
    
    
    
    
    
    
    
    
    




















    
    
    
    
    
    
    
    
if selected=="Exploratory Analysis":
    st.title('Exploratory Analysis')
    
    st.header('Exploring Immigration Factors by Country')
    
    st.markdown('---')
    
    st.markdown('### <div style="text-align: center"> Choropleth Map </div>', unsafe_allow_html=True)
        
    col15, col16 = st.columns([2, 5])

    with st.form('choropleth'):
        color_var = col15.selectbox(
            'Select an emissions variable for color',
            np.setdiff1d(list(num_dict.values()), 'Year'),
            key=33
        )
        color_var_df = [k for k, v in num_dict.items() if v == color_var]
        
        col15_agg = col15.radio('Select How You want to Aggregate Yearly Data', ['Average', 'Sum'], key = 100)
        
        hover_cols = np.setdiff1d(list(num_dict.values()), ['Year', color_var])
        hover_cols_df = [k for k, v in num_dict.items() if v in hover_cols]
    
        submitted = st.form_submit_button("Generate Choropleth Map")
        
        if submitted:
            if col15_agg == 'Average':
                color_range_dict = range_mean_dict
                multi_col_df = tourism[['code']+color_var_df+hover_cols_df].groupby('code').agg(['mean', 'count']).reset_index()
                multi_col_df.columns = ['_'.join(col) for col in multi_col_df.columns]
                keep_cols = ['code_', f'{color_var_df[0]}_mean', f'{color_var_df[0]}_count']+[f'{var}_mean'for var in hover_cols_df]
                data = multi_col_df[keep_cols]
                multi_col = f'{color_var_df[0]}_mean'
            elif col15_agg == 'Sum':
                color_range_dict = range_sum_dict
                multi_col_df = tourism[['code']+color_var_df+hover_cols_df].groupby('code').agg(['sum', 'count']).reset_index()
                multi_col_df.columns = ['_'.join(col) for col in multi_col_df.columns]
                keep_cols = ['code_', f'{color_var_df[0]}_sum', f'{color_var_df[0]}_count']+[f'{var}_sum'for var in hover_cols_df]
                data = multi_col_df[keep_cols]
                multi_col = f'{color_var_df[0]}_sum'
            fig8 = px.choropleth(
                data,
                locations='code_',
                locationmode='ISO-3',
                range_color=color_range_dict[color_var_df[0]],
                color=multi_col, 
                color_continuous_scale='sunset',
                labels={multi_col: color_var,
                        'code_' : 'country'},
                title=f'{color_var}',
                hover_name='code_',
                hover_data=keep_cols,
                )
            
            fig8.update_layout(margin={"r":0, "t":0, "l":0, "b":0}, title_x=0.32, title_y=0.94)
            col16.plotly_chart(fig8, use_container_width=True)
            
    st.markdown('---')
    
    st.header('Exploring Immigration Factors by Time and Region')
    
    st.markdown('---')
    
    st.markdown('### <div style="text-align: center"> Histogram </div>', unsafe_allow_html=True)
    
    st.markdown('<p style="font-size: 23px;">Numerical</p>', unsafe_allow_html=True)        
    col1, col2 = st.columns([2, 5])
    
    with st.form('Numerical'):
        
        col1_x = col1.selectbox('Select a numeric variable for the x-axis', np.setdiff1d(list(num_dict.values()), 'Year'), key=1)
        col1_x_df = [k for k, v in num_dict.items() if v == col1_x][0]
        
        col1_y = col1.selectbox('Select a numeric variable for the y-axis', np.setdiff1d(list(num_dict.values()), [col1_x, 'Year']), key=2)
        col1_y_df = [k for k, v in num_dict.items() if v == col1_y][0]
        
        col1_color = col1.selectbox('Select a category variable for the color', np.setdiff1d(list(cat_dict.values()), 'Country'), key=3)
        col1_color_df = [k for k, v in cat_dict.items() if v == col1_color][0]
        
        col1_show_histfunc = col1.radio('Select aggregation function',['Avg','Sum'], key=90)
        
        col1_px_histfunc = "avg" if col1_show_histfunc == "Avg" else "sum"
        
        col1_checkbox = col1.checkbox('Check to change the number of bins', key = 4)
        
        bins = 10
        if col1_checkbox:
            col1_bins = col1.number_input("Enter a number to specify the number of bins", min_value=5, placeholder="Type a number...")
            bins = col1_bins
            
        col1_log_y = col1.checkbox('Check to use logarithmic y-axis', key=5)

        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            user_cols=[col1_x_df, col1_y_df, col1_color_df]
            fig1=px.histogram(tourism[user_cols].dropna(), x=col1_x_df, y=col1_y_df, color=col1_color_df, nbins=bins, barmode='group', histfunc=col1_px_histfunc, labels=all_dict, log_y=col1_log_y, title=f'{col1_y} by {col1_x}')
            fig1.update_layout(title_x=0.28)
            col2.plotly_chart(fig1)
            
            
            
            
            
            
            
            
            
    
    st.markdown('<p style="font-size: 23px;">Categorical</p>', unsafe_allow_html=True)        
    
    col3, col4 = st.columns([2, 5])
    
    with st.form('histogram_two_cat_one_num'):
        col3_x = col3.selectbox('Select a categorical variable for the x-axis',np.setdiff1d(list(cat_dict.values()), 'Country'), key=6)
        col3_x_df = [k for k, v in cat_dict.items() if v == col3_x][0]
        
        col3_color = col3.selectbox('Select a categorical variable for the color',np.setdiff1d(list(cat_dict.values()), ['Country', col3_x]),key=7)
        col3_color_df = [k for k, v in cat_dict.items() if v == col3_color][0]
        
        col3_y = col3.selectbox('Select a numeric variable for the y-axis',np.setdiff1d(list(num_dict.values()), 'Year'),key=8)
        col3_y_df = [k for k, v in num_dict.items() if v == col3_y][0]
        
        col3_barmode = col3.selectbox('Select bar mode',['group','stack'],key=22)
        
        col3_show_histfunc = col3.radio('Select aggregation function',['Avg','Sum'], key=9)
        
        col3_px_histfunc = "avg" if col3_show_histfunc == "Avg" else "sum"
        
        col3_checkbox = col3.checkbox('Check to change the number of bins', key = 40)
        bins = 10
        if col3_checkbox:
            col3_bins = col3.number_input("Enter a number to specify the number of bins", min_value=5, placeholder="Type a number...")
            bins = col3_bins
        
        col3_log_y = col3.checkbox('Use logarithmic y-axis',key=10)
        
        submitted = st.form_submit_button('Submit to produce the histogram')
        
        user_cols=[col3_x_df, col3_y_df, col3_color_df]
        
        if submitted:
            fig2=px.histogram(tourism[user_cols].dropna(),x=col3_x_df,y=col3_y_df,color=col3_color_df,barmode=col3_barmode,histfunc=col3_px_histfunc,labels=all_dict,log_y=col3_log_y, nbins=bins, title=f'{col3_y} by {col3_x}')
            fig2.update_layout(title_x=0.28)
            col4.plotly_chart(fig2)

    
    st.markdown('<p style="font-size: 23px;">Yearly</p>', unsafe_allow_html=True)        
    
    col19, col20 = st.columns([2, 5])
    
    with st.form('histogram one num one cat by cat(year)'):
        
        
        col19_y = col19.selectbox('select a numeric variable for the y-axis', np.setdiff1d(list(num_dict.values()), 'Year'), key=41)
        col19_y_df = [k for k, v in num_dict.items() if v == col19_y][0]
        
        col19_color = col19.selectbox('select a category variable for the color', np.setdiff1d(list(cat_dict.values()), 'Country'), key=42)
        col19_color_df = [k for k, v in cat_dict.items() if v == col19_color][0]
        
        col19_show_histfunc = col19.radio('Select aggregation function',['Avg','Sum'], key=200)
        
        col19_px_histfunc = "avg" if col19_show_histfunc == "Avg" else "sum"
        
        col19_checkbox = col19.checkbox('Check to change the number of bins', key = 43)
        
        bins = 10
        if col19_checkbox:
            col19_bins = col19.number_input("Enter a number to specify the number of bins", min_value=5, placeholder="Type a number...", key = 44)
            bins = col19_bins
            
        col19_log_y = col19.checkbox('Check to use logarithmic y-axis', key=45)
    
        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            user_cols=['year', col19_y_df, col19_color_df]
            fig10=px.histogram(tourism[user_cols].dropna(), x='year', y=col19_y_df, color=col19_color_df, nbins=bins, barmode='group', labels=all_dict, log_y=col19_log_y, title=f'{col19_y} by Year', histfunc=col19_px_histfunc)
            fig10.update_xaxes(type='category', categoryorder='category ascending')
            fig10.update_layout(title_x=0.32)
            col20.plotly_chart(fig10)
    
    st.markdown('---')
    
    st.markdown('### <div style="text-align: center"> Boxplot </div>', unsafe_allow_html=True)
    
    col11, col12 = st.columns([2, 5])
    
    with st.form('boxplot_cat_country_num'):
        col11_x = col11.selectbox('Select a categorical variable for the x-axis', np.setdiff1d(list(cat_dict.values()),'Country'),key=24)
        col11_x_df = [k for k, v in cat_dict.items() if v == col11_x][0]
        
        col11_y = col11.selectbox('Select a numeric variable for the y-axis',np.setdiff1d(list(num_dict.values()),'Year'),key=25)
        col11_y_df = [k for k, v in num_dict.items() if v == col11_y][0]
        
        col11_points = col11.selectbox('Show points',['None','all','outliers'],key=26)
        points = False if col11_points == 'None' else col11_points
        
        col11_log_y = col11.checkbox('Use logarithmic y-axis',key=27)
        
        submitted = st.form_submit_button('Submit to produce the boxplot')
        
        if submitted:
            fig6=px.box(tourism,x=col11_x_df,y=col11_y_df,color=col11_x_df,points=points,labels=all_dict,log_y=col11_log_y, title=f'{col11_y} by {col11_x}')
            fig6.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.31)
            col12.plotly_chart(fig6)
    
        
    st.markdown('---')
    
    st.markdown('### <div style="text-align: center"> Scatterplot </div>', unsafe_allow_html=True)
    
    col17, col18 = st.columns([2, 5])
    
    with st.form('scatter_form'):
        x_var = col17.selectbox('Select x-axis variable', num_dict.values(), key=38)
        x_var_df = [k for k, v in num_dict.items() if v == x_var][0]
        y_var = col17.selectbox('Select y-axis variable', np.setdiff1d(list(num_dict.values()), x_var), key=39)
        y_var_df = [k for k, v in num_dict.items() if v == y_var][0]
        
        color_var = col17.selectbox('Select color variable', np.setdiff1d(list(cat_dict.values()), 'Country'), key=40)
        color_var_df = [k for k, v in cat_dict.items() if v == color_var][0]
        
        scale_y_match = col17.checkbox('Check to allow different y-scale', key=141)
        match_y = None if scale_y_match else "y"
            
        
        scale_x_match = col17.checkbox('Check to allow different x-scale', key=142)
        match_x = None if scale_x_match else "x"
        
        user_cols = [x_var_df, y_var_df, color_var_df, 'country']
        
        data = tourism[user_cols].dropna()
        
        submitted = st.form_submit_button("Generate Scatter Plot")
    
    if submitted:
        fig9 = px.scatter(
            data,
            x=x_var_df,
            y=y_var_df,
            color=color_var_df,
            hover_name='country',
            title=f'{x_var} vs {y_var} by {color_var}',
            log_x=False, 
            facet_col = color_var_df, 
            facet_col_spacing=0.1, 
            log_y=False
        )
        fig9.update_yaxes(matches=match_y, showticklabels=True)
        fig9.update_xaxes(matches=match_x, showticklabels=True)
        fig9.update_layout(title_x=0.4)
        col18.plotly_chart(fig9, use_container_width=True)
        
    st.markdown('---')


















if selected == 'Decennial Impact of Tourism':
    
    st.title('Decennial Impact of Tourism')
    
    st.header('Tourism’s Contribution to GDP Growth')
    
    col1, col2 = st.columns([0.1, 5])
    
    col3, col4 = st.columns([0.1, 5])
    
    col4.subheader('Tourists in each Country by Decade')
    
    cat_orders = {'decade' : ['1990s', '2000s', '2010s']}
    
    col4.markdown('1990s: The trend is positive, with GDP rising as tourist numbers grow. High GDP countries like Macao and Bermuda fit this, thanks to their gambling and luxury tourism boosting economies. Low GDP countries like Moldova and Sierra Leone also follow, with modest growth from emerging tourism. However, high GDP nations like Switzerland and Canada show less GDP gain, likely due to diverse economies, while low GDP countries like Burundi lag due to poor infrastructure. The bar chart shows a rising tourist number, driven by early globalization.')
    
    col4.markdown('2000s: The positive trend continues, with Macao and Bermuda leading due to tourism growth, and low GDP countries like Pakistan seeing small gains from cultural travel. High GDP countries like Singapore and low GDP nations like Togo deviate, possibly due to economic diversification or instability. The bar chart highlights a significant increase in tourists, fueled by budget airlines.')
    
    col4.markdown('2010s: The positive trend peaks, with Macao and Bermuda thriving, and low GDP countries like Malawi growing slowly. High GDP countries like Luxembourg and low GDP nations like Tajikistan show weaker GDP links, possibly from saturation or development gaps. The bar chart notes the highest tourist rise, boosted by digital marketing and travel booms. The overall increase in tourists over time, as seen across these decades, is true due to globalization, advancements in transportation (e.g., low-cost airlines), and effective marketing strategies that have made travel more accessible and appealing worldwide.')
    
    fig31=px.scatter(tourism[["decade","gdp","tourists_per_1000","country"]].dropna().groupby(['country', 'decade']).mean().reset_index(),x="tourists_per_1000",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 400, width=400,title="Relationship Between Tourists and GDP Per Capita", log_x=True, facet_col = "decade", category_orders=cat_orders, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    fig31.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig31.update_yaxes(showticklabels=True)
    fig31.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig31)
    
    fig4=px.histogram(tourism[["decade", "gdp","tourists_per_1000","country"]].dropna(), x="tourists_per_1000",y="gdp",color='decade',hover_name='country',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, category_orders=cat_orders, facet_col_spacing=0.1, nbins=10)
    fig4.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig4.update_yaxes(showticklabels=True)
    fig4.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig4)

    col4.subheader('Incoming Arrivals in each Country by Decade')

    col4.markdown('1990s: The trend is positive, with GDP increasing with arrivals. High GDP countries like Macao and Finland benefit from gaming and nature tourism, while low GDP nations like Laos see modest gains. High GDP countries like the UK and low GDP nations like Vietnam lag, possibly due to diversification or infrastructure issues. The bar chart shows a growing arrival trend with early travel expansion.')
    
    col4.markdown('2000s: The positive trend strengthens, with Macao and Finland leading, and low GDP countries like Haiti improving slightly. High GDP nations like Canada and low GDP countries like Kenya deviate, likely due to mature economies or challenges. The bar chart reflects a notable arrival increase with economic growth.')
    
    col4.markdown('2010s: The positive trend peaks, with Macao and Finland excelling, and low GDP nations like El Salvador growing. High GDP countries like Bermuda and low GDP nations like Jordan underperform, possibly from saturation or gaps. The bar chart shows the largest arrival rise, driven by digital platforms. The overall increase in arrivals over time, observed across these decades, is true due to global economic development, technological improvements in travel (e.g., online booking systems), and targeted tourism policies that have encouraged more visitors.')
    
    fig31=px.scatter(tourism[["decade","gdp","arv_1000","country"]].dropna().groupby(['country', 'decade']).mean().reset_index(),x="arv_1000",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 400, width=400,title="Relationship Between Incoming Arrivals and GDP Per Capita", log_x=True, facet_col = "decade", category_orders=cat_orders, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    fig31.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig31.update_yaxes(showticklabels=True)
    fig31.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig31)
    
    fig=px.histogram(tourism[["decade", "gdp","arv_1000","country"]].dropna(), x="arv_1000",y="gdp",color='decade',hover_name='country',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, category_orders=cat_orders, facet_col_spacing=0.1, nbins=10)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig)

    col4.subheader('Tourists Duration of Stay in each Country by Decade')

    col4.markdown('1990s: The trend is negative, with longer stays linked to lower GDP. High GDP countries like Switzerland and Bermuda fit this, possibly due to high costs, while low GDP nations like Morocco follow with budget tourism. High GDP countries like Macao and low GDP nations like El Salvador buck the trend, thanks to luxury or emerging tourism. The bar chart shows moderate stay lengths, focusing on short visits.')
    
    col4.markdown('2000s: The negative trend persists, with Switzerland and Thailand aligning due to cost or budget stays, while Macao and low GDP nations like China grow from diverse tourism. The bar chart indicates a slight stay increase with varied economic impact.')
    
    col4.markdown('2010s: The negative trend continues, with Norway and Morocco fitting due to costs or budget travel, while Macao and low GDP nations like Vietnam grow from unique attractions. The bar chart shows a stay peak, but economic returns diminish. The overall trend of increasing length of stay over time, as noted across these decades, is true due to a shift toward experiential and longer-duration travel, driven by cultural interest and affordable travel options, though this does not always translate to proportional economic gains.')
    
    fig=px.scatter(tourism[["decade","gdp","length","country"]].dropna().groupby(['country', 'decade']).mean().reset_index(),x="length",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 400, width=400,title="Relationship Between Length of Stay and GDP Per Capita", log_x=True, facet_col = "decade", category_orders=cat_orders, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig)
    
    fig=px.histogram(tourism[["decade", "gdp","length","country"]].dropna(), x="length",y="gdp",color='decade',hover_name='country',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, category_orders=cat_orders, facet_col_spacing=0.1, nbins=10)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col4.plotly_chart(fig)
    
    
if selected == 'Regional Impact of Tourism':
    
    st.title('Regional Impact of Tourism')

    col1, col2 = st.columns ([0.1, 5])
    
    col2.subheader('Tourists in each Country by Region')
    col2.markdown('all graphs exhibit positive linear correlation, slight outliers from libya and tajikstan, constant top spot from Macau')
    
    col2.markdown('Europe and Central Asia: The trend is positive, with GDP rising as tourist numbers increase. High GDP countries like France and Germany fit this, driven by cultural tourism (e.g. France). Low GDP countries like Moldova and Kyrgyzstan align, with modest growth from emerging tourism. High GDP nations like Switzerland deviate, possibly due to economic diversification, while low GDP countries like Tajikistan lag due to instability. The bar chart shows a steady tourist rise, reflecting strong travel infrastructure. ')
    
    col2.markdown('Sub-Saharan Africa: The trend is positive, with GDP growing with tourist numbers. High GDP countries like South Africa fit, boosted by wildlife tourism, while low GDP nations like Kenya align with gains from safari tourism. High GDP countries like Mauritius deviate, possibly due to small size limiting scalability, and low GDP countries like Burundi underperform due to conflict. The bar chart indicates a gradual tourist increase, driven by eco-tourism growth. ')
    
    col2.markdown('Latin America and Caribbean: The trend is positive, with GDP increasing with tourists. High GDP countries like Mexico fit, thanks to beach tourism, and low GDP nations like Haiti align with cultural tourism growth. High GDP countries like Barbados deviate, possibly due to saturation, while low GDP countries like Haiti lag further due to instability. The bar chart shows a notable tourist rise, fueled by cruise tourism. ')
    
    col2.markdown('South Asia: The trend is positive, with GDP increasing with tourist numbers. High GDP countries like India fit, thanks to cultural tourism, and low GDP nations like Nepal align with mountaineering. High GDP countries like Sri Lanka deviate, possibly due to recovery challenges, while low GDP countries like Afghanistan underperform due to security issues. The bar chart indicates a moderate tourist increase, supported by heritage tourism. ')
    
    col2.markdown('North America: The trend is positive, with GDP rising with tourists. High GDP countries like the USA fit, driven by diverse attractions, and low GDP nations like Belize align with eco-tourism. High GDP countries like Canada deviate, possibly due to broad economic base, while low GDP countries like Haiti (regionally considered) lag due to instability. The bar chart shows a strong tourist rise, fueled by global appeal. The overall increase in tourists over time is true due to globalization, improved transportation, and marketing, making travel more accessible. ')
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","tourists_per_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="tourists_per_1000",y="gdp",color='region',labels=all_dict, title="Relationship Between Tourists and GDP Per Capita", facet_col='region', facet_col_wrap=3, height=600, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country", facet_row_spacing=0.25)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=80,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)

    fig=px.histogram(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","tourists_per_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="tourists_per_1000",y="gdp",color='region',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, nbins=30)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(matches=None, showticklabels=False)
    fig.update_xaxes(matches=None, showticklabels=True)
    col2.plotly_chart(fig)
    
    col2.subheader('Incoming Arrivals in each Country by Region')

    col2.markdown('Europe and Central Asia: The trend is positive, with GDP rising with arrivals. High GDP countries like France fit, due to cultural tourism, and low GDP nations like Moldova align with growing visits. High GDP countries like Switzerland deviate, possibly due to diversification, while low GDP countries like Tajikistan lag due to infrastructure gaps. The bar chart shows a steady arrival increase, driven by travel networks. ')
    
    col2.markdown('Sub-Saharan Africa: The trend is positive, with GDP growing with arrivals. High GDP countries like South Africa fit, boosted by safaris, and low GDP nations like Kenya align with wildlife tourism. High GDP countries like Mauritius deviate, possibly due to capacity limits, while low GDP countries like Burundi underperform due to conflict. The bar chart indicates a gradual arrival rise, supported by eco-tourism. ')
    
    col2.markdown('Latin America and Caribbean: The trend is positive, with GDP increasing with arrivals. High GDP countries like Mexico fit, thanks to beaches, and low GDP nations like Haiti align with cultural growth. High GDP countries like Barbados deviate, possibly due to saturation, while low GDP countries like Haiti lag further due to instability. The bar chart shows a notable arrival increase, driven by cruises. ')
    
    col2.markdown('South Asia: The trend is positive, with GDP increasing with arrivals. High GDP countries like India fit, thanks to culture, and low GDP nations like Nepal align with mountaineering. High GDP countries like Sri Lanka deviate, possibly due to recovery issues, while low GDP countries like Afghanistan underperform due to security. The bar chart indicates a moderate arrival increase, supported by heritage. ')
    
    col2.markdown('North America: The trend is positive, with GDP rising with arrivals. High GDP countries like the USA fit, driven by attractions, and low GDP nations like Belize align with eco-tourism. High GDP countries like Canada deviate, possibly due to broad economy, while low GDP countries like Haiti lag due to instability. The bar chart shows a strong arrival rise, fueled by global appeal. The overall increase in arrivals over time is true due to economic growth, travel technology, and tourism policies.')

    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","arv_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="arv_1000",y="gdp",color='region',labels=all_dict, title="Relationship Between Incoming Arrivals and GDP Per Capita", facet_col='region', facet_col_wrap=3, height=600, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country", facet_row_spacing=0.25)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=80,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)

    fig=px.histogram(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","arv_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="arv_1000",y="gdp",color='region',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, nbins=30)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(matches=None, showticklabels=False)
    fig.update_xaxes(matches=None, showticklabels=True)
    col2.plotly_chart(fig)
    
    col2.subheader('Tourists Duration of Stay in each Country by Region')

    col2.markdown('Europe and Central Asia: The trend is negative, with longer stays linked to lower GDP. High GDP countries like Switzerland fit, due to high costs, and low GDP nations like Moldova align with budget tourism. High GDP countries like France deviate, thanks to cultural depth, while low GDP countries like Kyrgyzstan buck the trend with growing tourism. The bar chart shows moderate stay lengths, focusing on short visits. ')
    
    col2.markdown('Sub-Saharan Africa: The trend is negative, with longer stays tied to lower GDP. High GDP countries like South Africa fit, due to cost concerns, and low GDP nations like Kenya align with budget travel. High GDP countries like Mauritius deviate, thanks to luxury stays, while low GDP countries like Tanzania grow with safari tourism. The bar chart indicates a slight stay increase, with varied impact. ')

    col2.markdown('Latin America and Caribbean: The trend is negative, with longer stays linked to lower GDP. High GDP countries like Mexico fit, due to costs, and low GDP nations like Haiti align with budget tourism. High GDP countries like Barbados deviate, thanks to luxury, while low GDP countries like Jamaica grow with culture. The bar chart shows a notable stay rise, driven by experiential travel. ')

    col2.markdown('South Asia: The trend is negative, with longer stays tied to lower GDP. High GDP countries like India fit, due to costs, and low GDP nations like Nepal align with budget tourism. High GDP countries like Sri Lanka deviate, thanks to recovery, while low GDP countries like Bhutan grow with niche tourism. The bar chart indicates a moderate stay increase, supported by heritage. ')

    col2.markdown('North America: The trend is negative, with longer stays linked to lower GDP. High GDP countries like the USA fit, due to costs, and low GDP nations like Belize align with budget travel. High GDP countries like Canada deviate, thanks to nature tourism, while low GDP countries like Haiti lag due to instability. The bar chart shows a strong stay rise, fueled by experience. The overall trend of increasing length of stay over time is true due to experiential travel and affordable options, though economic returns vary.')
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","length", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="length",y="gdp",color='region',labels=all_dict, title="Relationship Between Length of Stay and GDP Per Capita", facet_col='region', facet_col_wrap=3, height=600, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country", facet_row_spacing=0.25)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)

    fig=px.histogram(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","length", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="length",y="gdp",color='region',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, nbins=30)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(matches=None, showticklabels=False)
    fig.update_xaxes(matches=None, showticklabels=True)
    col2.plotly_chart(fig)

if selected == 'Progressive Impact of Tourism':

    st.title('Progressive Impact of Tourism')

    fig = px.choropleth(
        tourism.groupby(['code', 'country']).mean(numeric_only=True).reset_index(),
        locations='code',
        locationmode='ISO-3',
        range_color=range_mean_dict['gdp'],
        color="gdp", 
        color_continuous_scale='sunset',
        labels=all_dict,
        title='',
        hover_name='country',
        projection='robinson'
        )
    fig.update_layout(showlegend=True,margin=dict(l=0,r=210,t=65,b=65),font=dict(size=12), title_x=0.3)
    st.plotly_chart(fig)
    
    fig = px.choropleth(
        tourism.groupby(['code', 'country']).mean(numeric_only=True).reset_index(),
        locations='code',
        locationmode='ISO-3',
        range_color=range_mean_dict['tourists_per_1000'],
        color="tourists_per_1000", 
        color_continuous_scale='sunset',
        labels=all_dict,
        title='',
        hover_name='country',
        projection='robinson'
        )
    st.plotly_chart(fig)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    
    col1, col2 = st.columns([1, 1])
    
    col1.markdown('High (e.g. Spain and France): The trend is strongly positive across decades, with GDP rising as tourist numbers grow. In Europe and Central Asia, cultural tourism (e.g. France) drives this, while the UAE in Middle East and North Africa benefits from luxury tourism. The 2010s peak reflects digital marketing and travel booms.')
    
    tour_dict = {'high': ["ESP", "FRA", "GRC", "CHE", "ARE", "HRV"],
                 'medium': ["CAN", "GBR", "NAM", "SVK", "MYS", "BRN"],
                 'low': ['TCD', 'BGD', 'COD', 'PAK', 'ETH', 'GIN']}
    
    fig=px.line(tourism.loc[tourism['code'].isin(tour_dict['high']), ["decade","tourists_per_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="tourists_per_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col1.plotly_chart(fig)
    
    col2.markdown('Low (e.g. Tajikistan and Bangladesh): The trend is positive but weak, with low GDP countries in South Asia and Sub-Saharan Africa showing modest tourism growth (e.g. Pakistan’s cultural travel). Lags in the 1990s and 2000s stem from infrastructure and stability issues, with slight gains in the 2010s from emerging tourism.')

    
    fig=px.line(tourism.loc[tourism['code'].isin(tour_dict['low']), ["decade","tourists_per_1000","country", 'code', 'year']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="tourists_per_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)
    
    st.markdown('Medium (e.g. Canada and United Kingdom): The trend is positive but less pronounced, with GDP gains moderated by diverse economies. In North America and Europe, economic diversification (e.g. Canada) tempers tourism’s impact, with steady growth from the 2000s onward due to global travel networks.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(tour_dict['medium']), ["decade","tourists_per_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="tourists_per_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    st.plotly_chart(fig)
    
    col5, col6 = st.columns([0.1, 5])
    
    fig8 = px.choropleth(
        tourism.groupby(['code', 'country']).sum(numeric_only=True).reset_index(),
        locations='code',
        locationmode='ISO-3',
        range_color=range_sum_dict['arv_1000'],
        color="arv_1000", 
        color_continuous_scale='sunset',
        labels=all_dict,
        title='',
        hover_name='country',
        projection='robinson'
        )
    col6.plotly_chart(fig8)

    col7, col8 = st.columns([1, 1])

    arv_dict = {'high' : ["SMR", "CYM", "TCA", "MAC", "KNA", "BHS", "ATG", "ABW", "BMU", "DMA"],
                'medium' : ["CAN", "GEO", "SGP", "VUT", "ITA", "JAM", "FIN", "NOR", "BGR", "SWZ"],
                'low' : ["TZA", "SEN", "COG", "COD", "TJK", "PHL", "MDA", "CMR", "TGO", "IND"]}
    
    col7.markdown('High (e.g. San Marino and Macao): The trend is strongly positive, with GDP rising sharply with arrivals. In East Asia and Pacific (e.g. and Macao’s gaming tourism) and small Caribbean nations, the 2010s peak reflects cruise and luxury tourism growth, boosted by travel technology.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['high']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="Relationship Between Incoming Arrivals and GDP Per Capita", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col7.plotly_chart(fig)
    
    col8.markdown('Low (e.g. Tanzania and India): The trend is positive but weak, with low GDP countries in Sub-Saharan Africa and South Asia showing modest arrival growth (e.g. Tanzania’s safaris). Infrastructure gaps and instability limit progress, with slight 2010s gains from eco-tourism.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['low']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col8.plotly_chart(fig)
    
    st.markdown('Medium (e.g. Canada and Singapore): The trend is positive but moderated, with GDP gains influenced by diverse economies. In North America and East Asia, the 2000s and 2010s show steady arrival increases, though diversification (e.g. Singapore) reduces tourism’s dominance.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['medium']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    st.plotly_chart(fig)
    

    
    col9, col10 = st.columns([0.1, 5])
    
    fig7 = px.choropleth(
        tourism.groupby(['code', 'country']).sum(numeric_only=True).reset_index(),
        locations='code',
        locationmode='ISO-3',
        range_color=range_sum_dict['length'],
        color="length", 
        color_continuous_scale='sunset',
        labels=all_dict,
        title='',
        hover_name='country',
        projection='robinson'
        )
    col10.plotly_chart(fig7)
    
    col11, col12 = st.columns([1, 1])

    
    length_dict = {'high' : ["SLB", "PNG", "KIR", "NPL", "GHA", "CRI", "KEN", "GMB", "LKA", "SYC"],
                   'medium' : ["RUS", "URY", "GTM", "GEO", "BWA", "BEN", "ZMB", "BHS", "GIN", "HRV"],
                   'low' : ["SMR", "NOR", "BDI", "CMR", "MYS", "MAC", "PER", "JPN", "PAK", "OMN"]}
    
    col11.markdown('High (e.g. Solomon Islands and Nepal): The trend is negative but less defined, with longer stays linked to lower GDP. In East Asia and Pacific and South Asia, the 2010s show a stay peak driven by experiential travel (e.g. Nepal’s mountaineering), though economic returns are limited. Regional effects, like Sub-Saharan Africa’s longer stays (e.g. Kenya) despite low GDP, suggest cultural or budget tourism influences.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['high']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="Relationship Between Length of Stay and GDP Per Capita", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col11.plotly_chart(fig)
    
    col12.markdown('Low (e.g. SMR, Japan): The trend is negative, with shorter stays linked to high GDP. In Europe and East Asia, the 1990s and 2000s show brief visits due to costs (e.g. Japan’s high expenses), though the 2010s see some growth from niche tourism. The inverse pattern and less defined trend may reflect regional effects, such as Middle East luxury stays (e.g. Oman) countering the negative GDP link.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['low']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col12.plotly_chart(fig)
    
    st.markdown('Medium (e.g. Russia and Bahamas): The trend is negative with variability, with moderate stays tied to mixed GDP impacts. In Europe and Latin America, the 2000s and 2010s show slight increases, influenced by diverse attractions (e.g. Bahamas’ luxury and Russia’s vast tourism), balancing cost and experience.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['medium']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    st.plotly_chart(fig)




if selected == 'Conclusion':
    
    st.title('Conclusion')
    

    
    
    
    if selected == 'Bibliography':
        st.title('Bibliography')
        
        st.markdown('The dataset is downloaded from https://www.kaggle.com/datasets/amirjdai/tourism')
