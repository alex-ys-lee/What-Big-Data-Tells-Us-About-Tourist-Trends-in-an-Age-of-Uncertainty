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


mypath = '/Users/boredom/Downloads/Data_Science/DataSets/'

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
                 "gdp" : "GDP",
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
    
    st.subheader('Questions to be Answered (Ongoing)')
    
    st.markdown('To what extent does the length of tourist stay reflect GDP per capita, and why do certain low-income regions—particularly in Sub-Saharan Africa and South Asia—consistently defy this trend with longer average stays?')

    st.markdown('How do small island developing states (SIDS) achieve disproportionately high tourism arrival intensities despite limited land area and population—and what does this reveal about the scalability of tourism-led development?')
    
    st.markdown('Are high-income countries becoming "tourism-saturated", as suggested by declining growth rates in arrivals per 1000 people after 2010, while emerging economies in Southeast Asia and the Middle East accelerate rapidly?')

    st.markdown('What underlying geopolitical, infrastructural, and marketing factors explain why some landlocked, low-GDP nations (e.g., Nepal, Eswatini) outperform coastal peers in tourism density—and can these models be replicated?')
    
    st.markdown('Does the sharp decline in tourism metrics across nearly all countries in 2020 represent a structural reset in global travel behavior, or merely a temporary shock—and how do pre- and post-pandemic trajectories differ by region and income level?')

    st.markdown('Which countries dominate inbound versus outbound tourism flows, and what do imbalances in this ratio reveal about global economic inequality, cultural influence, and mobility privilege?')





















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
    
    st.markdown('explain what code does')
    
    country_codes = '''tourism = pd.DataFrame(columns=['country', 'code', 'year'])
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
    
    st.markdown('explain what code does')

    concat = '''tour_region_list = []
    tour_country_list = []
    
    for source, df in dataframes.items():
        df.loc[:, 'data_source'] = source
        tour_region_list.append(df[df['country'].isin(unique_region)].drop('code', axis=1))
        tour_country_list.append(df[~df['country'].isin(unique_region)].drop('country', axis=1))

    
    tourism_regions = pd.concat(tour_region_list, axis = 0, ignore_index=True)
    tourism_country = pd.concat(tour_country_list, axis = 0, ignore_index=True)'''
    
    st.code(concat, language='python')
    
    
    
    
    
    
    
    
    
    
    
    




















    
    
    
    
    
    
    
    
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
        
        # color_scales = [
        #     'Viridis', 'Cividis', 'Inferno', 'Magma', 'Plasma',
        #     'Hot', 'Blackbody', 'Earth', 'Electric', 'Portland',
        #     'Rainbow', 'Jet', 'Blues', 'Greens', 'Reds', 
        #     'YlOrRd', 'YlGnBu', 'BuPu', 'OrRd', 'PuRd'
        # ]
        
        # color_scale = col15.selectbox(
        #     'Select color scale',
        #     color_scales,
        #     key=37
        # )
    
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
                hover_data=keep_cols
                )
            
            fig8.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
            col16.plotly_chart(fig8, use_container_width=True)
            
    st.markdown('---')
    
    st.header('Exploring Immigration Factors by Time and Region')
    
    st.markdown('---')
    
    st.markdown('### <div style="text-align: center"> Histogram </div>', unsafe_allow_html=True)
        
    col1, col2 = st.columns([2, 5])
    
    with st.form('histogram two num one cat'):
        
        col1_x = col1.selectbox('select a numeric variable for the x-axis', np.setdiff1d(list(num_dict.values()), 'Year'), key=1)
        col1_x_df = [k for k, v in num_dict.items() if v == col1_x][0]
        
        col1_y = col1.selectbox('select a numeric variable for the y-axis', np.setdiff1d(list(num_dict.values()), [col1_x, 'Year']), key=2)
        col1_y_df = [k for k, v in num_dict.items() if v == col1_y][0]
        
        col1_color = col1.selectbox('select a category variable for the color', np.setdiff1d(list(cat_dict.values()), 'Country'), key=3)
        col1_color_df = [k for k, v in cat_dict.items() if v == col1_color][0]
        
        col1_checkbox = col1.checkbox('check to change the number of bins', key = 4)
        
        bins = 10
        if col1_checkbox:
            col1_bins = col1.number_input("Enter a number to specify the number of bins", min_value=5, placeholder="Type a number...")
            bins = col1_bins
            
        col1_log_y = col1.checkbox('Check to use logarithmic y-axis', key=5)

        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            user_cols=[col1_x_df, col1_y_df, col1_color_df]
            fig1=px.histogram(tourism[user_cols].dropna(), x=col1_x_df, y=col1_y_df, color=col1_color_df, nbins=bins, barmode='group', histfunc='avg', labels=all_dict, log_y=col1_log_y)
            #fig.update_xaxes(type='category', categoryorder='category ascending')
            col2.plotly_chart(fig1)
            
            
            
            
            
            
            
            
            
    
    st.subheader('histogram two cat one num')
    
    col3, col4 = st.columns([2, 5])
    
    with st.form('histogram_two_cat_one_num'):
        col3_x = col3.selectbox('Select a categorical variable for the x-axis',np.setdiff1d(list(cat_dict.values()), 'Country'), key=6)
        col3_x_df = [k for k, v in cat_dict.items() if v == col3_x][0]
        
        col3_color = col3.selectbox('Select a categorical variable for the color',np.setdiff1d(list(cat_dict.values()), ['Country', col3_x]),key=7)
        col3_color_df = [k for k, v in cat_dict.items() if v == col3_color][0]
        
        col3_y = col3.selectbox('Select a numeric variable for the y-axis',num_dict.values(),key=8)
        col3_y_df = [k for k, v in num_dict.items() if v == col3_y][0]
        
        col3_show_histfunc = col3.radio('Select aggregation function',['Avg','Sum'], key=9)
        
        col3_px_histfunc = "avg" if col3_show_histfunc == "Avg" else "sum"
        
        col3_log_y = col3.checkbox('Use logarithmic y-axis',key=10)
        
        submitted = st.form_submit_button('Submit to produce the histogram')
        
        user_cols=[col3_x_df, col3_y_df, col3_color_df]
        
        if submitted:
            fig2=px.histogram(tourism[user_cols].dropna(),x=col3_x_df,y=col3_y_df,color=col3_color_df,barmode='group',histfunc=col3_px_histfunc,labels=all_dict,log_y=col3_log_y)
            col4.plotly_chart(fig2)
            
            
            
            
            
            
            
            
            
    st.subheader('histogram one num one cat')
    
    col5, col6 = st.columns([2, 5])
    
    with st.form('histogram_one_num_one_cat'):
        col5_x = col5.selectbox('Select a numeric variable for the x-axis',num_dict.values(),key=11)
        col5_x_df = [k for k, v in num_dict.items() if v == col5_x][0]
        
        col5_color = col5.selectbox('Select a categorical variable for the color',np.setdiff1d(list(cat_dict.values()), 'Country'),key=12)
        col5_color_df = [k for k, v in cat_dict.items() if v == col5_color][0]
        
        col5_y_type = col5.radio('Select y-axis type',['Counts','Percent'],key=13)
        histnorm = 'percent' if col5_y_type == 'Percent' else None
        
        col5_bins_toggle = col5.checkbox('Check to change the number of bins',key=14)
        bins = 10
        if col5_bins_toggle:
            bins = col5.number_input("Enter number of bins",min_value=5,value=10,step=1)
        
        col5_log_y = col5.checkbox('Check to use logarithmic y-axis',key=15)
        
        submitted = st.form_submit_button("Submit to produce the histogram")
        
        if submitted:
            fig3=px.histogram(tourism,x=col5_x_df,color=col5_color_df,nbins=bins,barmode='group',histnorm=histnorm,labels=all_dict,log_y=col5_log_y)
            col6.plotly_chart(fig3)
            
            
            
            
            
            
            
            
        
    st.subheader('histogram two cat')

    col7, col8 = st.columns([2, 5])

    with st.form('histogram_two_cat'):
        col7_x = col7.selectbox('Select a categorical variable for the x-axis', np.setdiff1d(list(cat_dict.values()), 'Country'), key=16)
        col7_x_df = [k for k, v in cat_dict.items() if v == col7_x][0]
        
        col7_color = col7.selectbox('Select a categorical variable for the color', np.setdiff1d(list(cat_dict.values()), [col7_x, 'Country']), key=17)
        col7_color_df = [k for k, v in cat_dict.items() if v == col7_color][0]
        
        col7_y_type = col7.selectbox('Select y-axis type', ['Counts', 'Percent'], key=18)
        histnorm = 'percent' if col7_y_type == 'Percent' else None
        
        submitted = st.form_submit_button("Submit to produce the histogram")
        
        if submitted:
            fig4 = px.histogram(tourism, x=col7_x_df, color=col7_color_df, histnorm=histnorm, labels=all_dict)
            col8.plotly_chart(fig4)









    st.subheader('histogram_two_cat_enhanced')
    
    col9, col10 = st.columns([2, 5])
    
    with st.form('histogram_two_cat_enhanced'):
        col9_x = col9.selectbox('Select a categorical variable for the x-axis',np.setdiff1d(list(cat_dict.values()), 'Country'),key=19)
        col9_x_df = [k for k, v in cat_dict.items() if v == col9_x][0]
        
        col9_color = col9.selectbox('Select a categorical variable for the color',np.setdiff1d(list(cat_dict.values()),[col9_x, 'Country']),key=20)
        col9_color_df = [k for k, v in cat_dict.items() if v == col9_color][0]
        
        col9_y_type = col9.selectbox('Select y-axis type',['Counts','Percent'],key=21)
        histnorm = 'percent' if col9_y_type == 'Percent' else None
        
        col9_barmode = col9.selectbox('Select bar mode',['group','stack'],key=22)
        
        col9_title = col9.text_input('Enter plot title','Category Distribution',key=23)
        
        submitted = st.form_submit_button('Submit to produce the histogram')
        
        if submitted:
            fig5=px.histogram(tourism,x=col9_x_df,color=col9_color_df,histnorm=histnorm,barmode=col9_barmode,labels=all_dict,title=col9_title)
            fig5.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
            col10.plotly_chart(fig5)










    st.subheader('boxplot_cat_country_num')
    
    col11, col12 = st.columns([2, 5])
    
    with st.form('boxplot_cat_country_num'):
        col11_x = col11.selectbox('Select a categorical variable for the x-axis', np.setdiff1d(list(cat_dict.values()),'Country'),key=24)
        col11_x_df = [k for k, v in cat_dict.items() if v == col11_x][0]
        
        col11_y = col11.selectbox('Select a numeric variable for the y-axis',num_dict.values(),key=25)
        col11_y_df = [k for k, v in num_dict.items() if v == col11_y][0]
        
        col11_points = col11.selectbox('Show points',['None','all','outliers'],key=26)
        points = False if col11_points == 'None' else col11_points
        
        col11_log_y = col11.checkbox('Use logarithmic y-axis',key=27)
        
        submitted = st.form_submit_button('Submit to produce the boxplot')
        
        if submitted:
            fig6=px.box(tourism,x=col11_x_df,y=col11_y_df,color=col11_x_df,points=points,labels=all_dict,log_y=col11_log_y)
            fig6.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
            col12.plotly_chart(fig6)
    
        
    st.subheader('Scatter Plot')
    
    col17, col18 = st.columns([2, 5])
    
    with st.form('scatter_form'):
        x_var = col17.selectbox('Select x-axis variable', num_dict.values(), key=38)
        x_var_df = [k for k, v in num_dict.items() if v == x_var][0]
        y_var = col17.selectbox('Select y-axis variable', np.setdiff1d(list(num_dict.values()), x_var), key=39)
        y_var_df = [k for k, v in num_dict.items() if v == y_var][0]
        
        # User selects color variable (categorical)
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
        col18.plotly_chart(fig9, use_container_width=True)
        
    st.subheader('histogram one num one cat by cat(year)')
    
    col19, col20 = st.columns([2, 5])
    
    with st.form('histogram one num one cat by cat(year)'):
        
        
        col19_y = col19.selectbox('select a numeric variable for the y-axis', np.setdiff1d(list(num_dict.values()), 'Year'), key=41)
        col19_y_df = [k for k, v in num_dict.items() if v == col19_y][0]
        
        col19_color = col19.selectbox('select a category variable for the color', np.setdiff1d(list(cat_dict.values()), 'Country'), key=42)
        col19_color_df = [k for k, v in cat_dict.items() if v == col19_color][0]
        
        col19_checkbox = col19.checkbox('check to change the number of bins', key = 43)
        
        bins = 10
        if col19_checkbox:
            col19_bins = col19.number_input("Enter a number to specify the number of bins", min_value=5, placeholder="Type a number...", key = 44)
            bins = col19_bins
            
        col19_log_y = col19.checkbox('Check to use logarithmic y-axis', key=45)
    
        submitted=st.form_submit_button("Submit to produce the histogram")
        if submitted:
            user_cols=['year', col19_y_df, col19_color_df]
            fig10=px.histogram(tourism[user_cols].dropna(), x='year', y=col19_y_df, color=col19_color_df, nbins=bins, barmode='group', histfunc='avg', labels=all_dict, log_y=col19_log_y)
            fig10.update_xaxes(type='category', categoryorder='category ascending')
            col20.plotly_chart(fig10)
















if selected == 'Decennial Impact of Tourism':
    
    st.title('Decennial Impact of Tourism')
    
    st.header('Tourism’s Contribution to GDP Growth')
    
    col1, col2 = st.columns([0.1, 5])
    
    col3, col4 = st.columns([0.1, 5])
    
    col4.subheader('Tourists in each Country by Decade')
    
    cat_orders = {'decade' : ['1990s', '2000s', '2010s']}
    
    st.markdown('overall trend example based on all subplots: as expected tourism increases, gdp increases), (high and low country examples, include possible explanation for position), (find exception countries that are opposite the trend')
    
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
    
    col2.markdown('Europe and Central Asia: The trend is positive, with GDP rising as tourist numbers increase. High GDP countries like France and Germany fit this, driven by cultural tourism (e.g. France). Low GDP countries like Moldova and Kyrgyzstan align, with modest growth from emerging tourism. High GDP nations like Switzerland deviate, possibly due to economic diversification, while low GDP countries like Tajikistan lag due to instability. The bar chart shows a steady tourist rise, reflecting strong travel infrastructure. Sub-Saharan Africa: The trend is positive, with GDP growing with tourist numbers. High GDP countries like South Africa fit, boosted by wildlife tourism, while low GDP nations like Kenya align with gains from safari tourism. High GDP countries like Mauritius deviate, possibly due to small size limiting scalability, and low GDP countries like Burundi underperform due to conflict. The bar chart indicates a gradual tourist increase, driven by eco-tourism growth. Latin America and Caribbean: The trend is positive, with GDP increasing with tourists. High GDP countries like Mexico fit, thanks to beach tourism, and low GDP nations like Haiti align with cultural tourism growth. High GDP countries like Barbados deviate, possibly due to saturation, while low GDP countries like Haiti lag further due to instability. The bar chart shows a notable tourist rise, fueled by cruise tourism. East Asia and Pacific: The trend is positive, with GDP rising with tourist numbers. High GDP countries like Japan fit, driven by cultural appeal, and low GDP nations like Laos align with eco-tourism. High GDP countries like Singapore deviate, possibly due to diversification, while low GDP countries like Vanuatu underperform due to remoteness. The bar chart reflects a significant tourist increase, boosted by regional travel hubs. Middle East and North Africa: The trend is positive, with GDP growing with tourists. High GDP countries like the UAE fit, due to luxury tourism, and low GDP nations like Jordan align with historical sites. High GDP countries like Qatar deviate, possibly due to oil reliance, while low GDP countries like Yemen lag due to conflict. The bar chart shows a sharp tourist rise, driven by diversification efforts. South Asia: The trend is positive, with GDP increasing with tourist numbers. High GDP countries like India fit, thanks to cultural tourism, and low GDP nations like Nepal align with mountaineering. High GDP countries like Sri Lanka deviate, possibly due to recovery challenges, while low GDP countries like Afghanistan underperform due to security issues. The bar chart indicates a moderate tourist increase, supported by heritage tourism. North America: The trend is positive, with GDP rising with tourists. High GDP countries like the USA fit, driven by diverse attractions, and low GDP nations like Belize align with eco-tourism. High GDP countries like Canada deviate, possibly due to broad economic base, while low GDP countries like Haiti (regionally considered) lag due to instability. The bar chart shows a strong tourist rise, fueled by global appeal. The overall increase in tourists over time is true due to globalization, improved transportation, and marketing, making travel more accessible.')
    
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

    col2.markdown('Europe and Central Asia: The trend is positive, with GDP rising with arrivals. High GDP countries like France fit, due to cultural tourism, and low GDP nations like Moldova align with growing visits. High GDP countries like Switzerland deviate, possibly due to diversification, while low GDP countries like Tajikistan lag due to infrastructure gaps. The bar chart shows a steady arrival increase, driven by travel networks. Sub-Saharan Africa: The trend is positive, with GDP growing with arrivals. High GDP countries like South Africa fit, boosted by safaris, and low GDP nations like Kenya align with wildlife tourism. High GDP countries like Mauritius deviate, possibly due to capacity limits, while low GDP countries like Burundi underperform due to conflict. The bar chart indicates a gradual arrival rise, supported by eco-tourism. Latin America and Caribbean: The trend is positive, with GDP increasing with arrivals. High GDP countries like Mexico fit, thanks to beaches, and low GDP nations like Haiti align with cultural growth. High GDP countries like Barbados deviate, possibly due to saturation, while low GDP countries like Haiti lag further due to instability. The bar chart shows a notable arrival increase, driven by cruises. East Asia and Pacific: The trend is positive, with GDP rising with arrivals. High GDP countries like Japan fit, due to cultural appeal, and low GDP nations like Laos align with eco-tourism. High GDP countries like Singapore deviate, possibly due to economic diversity, while low GDP countries like Vanuatu underperform due to isolation. The bar chart reflects a significant arrival rise, boosted by regional hubs. Middle East and North Africa: The trend is positive, with GDP growing with arrivals. High GDP countries like the UAE fit, due to luxury tourism, and low GDP nations like Jordan align with historical sites. High GDP countries like Qatar deviate, possibly due to oil focus, while low GDP countries like Yemen lag due to conflict. The bar chart shows a sharp arrival rise, driven by diversification. South Asia: The trend is positive, with GDP increasing with arrivals. High GDP countries like India fit, thanks to culture, and low GDP nations like Nepal align with mountaineering. High GDP countries like Sri Lanka deviate, possibly due to recovery issues, while low GDP countries like Afghanistan underperform due to security. The bar chart indicates a moderate arrival increase, supported by heritage. North America: The trend is positive, with GDP rising with arrivals. High GDP countries like the USA fit, driven by attractions, and low GDP nations like Belize align with eco-tourism. High GDP countries like Canada deviate, possibly due to broad economy, while low GDP countries like Haiti lag due to instability. The bar chart shows a strong arrival rise, fueled by global appeal. The overall increase in arrivals over time is true due to economic growth, travel technology, and tourism policies.')
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","arv_1000", "country"]], x="arv_1000",y="gdp",color='region',labels=all_dict, title="Relationship Between Incoming Arrivals and GDP Per Capita", facet_col='region', facet_col_wrap=2, height=1000, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","arv_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="arv_1000",y="gdp",color='region',labels=all_dict, title="", facet_col='region', facet_col_wrap=2, height=1000, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)

    fig=px.histogram(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","arv_1000", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="arv_1000",y="gdp",color='region',labels=all_dict, title="", barmode='group', histfunc='avg', log_y=True, height=400, nbins=30)
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(matches=None, showticklabels=False)
    fig.update_xaxes(matches=None, showticklabels=True)
    col2.plotly_chart(fig)
    
    col2.subheader('Tourists Duration of Stay in each Country by Region')

    col2.markdown('Europe and Central Asia: The trend is negative, with longer stays linked to lower GDP. High GDP countries like Switzerland fit, due to high costs, and low GDP nations like Moldova align with budget tourism. High GDP countries like France deviate, thanks to cultural depth, while low GDP countries like Kyrgyzstan buck the trend with growing tourism. The bar chart shows moderate stay lengths, focusing on short visits. Sub-Saharan Africa: The trend is negative, with longer stays tied to lower GDP. High GDP countries like South Africa fit, due to cost concerns, and low GDP nations like Kenya align with budget travel. High GDP countries like Mauritius deviate, thanks to luxury stays, while low GDP countries like Tanzania grow with safari tourism. The bar chart indicates a slight stay increase, with varied impact. Latin America and Caribbean: The trend is negative, with longer stays linked to lower GDP. High GDP countries like Mexico fit, due to costs, and low GDP nations like Haiti align with budget tourism. High GDP countries like Barbados deviate, thanks to luxury, while low GDP countries like Jamaica grow with culture. The bar chart shows a notable stay rise, driven by experiential travel. East Asia and Pacific: The trend is negative, with longer stays tied to lower GDP. High GDP countries like Japan fit, due to high costs, and low GDP nations like Laos align with budget stays. High GDP countries like Australia deviate, thanks to diverse attractions, while low GDP countries like Vietnam grow with tourism. The bar chart reflects a significant stay increase, boosted by culture. Middle East and North Africa: The trend is negative, with longer stays linked to lower GDP. High GDP countries like the UAE fit, due to costs, and low GDP nations like Jordan align with budget travel. High GDP countries like Qatar deviate, thanks to luxury, while low GDP countries like Morocco grow with culture. The bar chart shows a sharp stay rise, driven by diversification. South Asia: The trend is negative, with longer stays tied to lower GDP. High GDP countries like India fit, due to costs, and low GDP nations like Nepal align with budget tourism. High GDP countries like Sri Lanka deviate, thanks to recovery, while low GDP countries like Bhutan grow with niche tourism. The bar chart indicates a moderate stay increase, supported by heritage. North America: The trend is negative, with longer stays linked to lower GDP. High GDP countries like the USA fit, due to costs, and low GDP nations like Belize align with budget travel. High GDP countries like Canada deviate, thanks to nature tourism, while low GDP countries like Haiti lag due to instability. The bar chart shows a strong stay rise, fueled by experience. The overall trend of increasing length of stay over time is true due to experiential travel and affordable options, though economic returns vary.')
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","length", "country"]], x="length",y="gdp",color='region',labels=all_dict, title="Relationship Between Length of Stay and GDP Per Capita", facet_col='region', facet_col_wrap=2, height=1000, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)
    
    fig=px.scatter(tourism.loc[tourism["region"].isin(regions_list),["region", "gdp","length", "country"]].groupby(["region", "country"]).mean(numeric_only=True).reset_index(), x="length",y="gdp",color='region',labels=all_dict, title="", facet_col='region', facet_col_wrap=2, height=1000, width=400, log_x=True, facet_col_spacing=0.1, log_y=True, hover_name="country")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
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
    
    col2.markdown('Medium (e.g. Canada and United Kingdom): The trend is positive but less pronounced, with GDP gains moderated by diverse economies. In North America and Europe, economic diversification (e.g. Canada) tempers tourism’s impact, with steady growth from the 2000s onward due to global travel networks.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(tour_dict['medium']), ["decade","tourists_per_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="tourists_per_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col2.plotly_chart(fig)
    
    st.markdown('Low (e.g. Tajikistan and Bangladesh): The trend is positive but weak, with low GDP countries in South Asia and Sub-Saharan Africa showing modest tourism growth (e.g. Pakistan’s cultural travel). Lags in the 1990s and 2000s stem from infrastructure and stability issues, with slight gains in the 2010s from emerging tourism.')

    
    fig=px.line(tourism.loc[tourism['code'].isin(tour_dict['low']), ["decade","tourists_per_1000","country", 'code', 'year']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="tourists_per_1000",color="country",hover_name='country',labels=all_dict, height = 300, width=400,title="", log_x=True, log_y = True)
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
    
    arv_dict = {'high' : ["SMR", "CYM", "TCA", "MAC", "KNA", "BHS", "ATG", "ABW", "BMU", "DMA"],
                'medium' : ["CAN", "GEO", "SGP", "VUT", "ITA", "JAM", "FIN", "NOR", "BGR", "SWZ"],
                'low' : ["TZA", "SEN", "COG", "COD", "TJK", "PHL", "MDA", "CMR", "TGO", "IND"]}
    
    col6.markdown('High (e.g. San Marino and Macao): The trend is strongly positive, with GDP rising sharply with arrivals. In East Asia and Pacific (e.g. and Macao’s gaming tourism) and small Caribbean nations, the 2010s peak reflects cruise and luxury tourism growth, boosted by travel technology.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['high']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="Relationship Between Incoming Arrivals and GDP Per Capita", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col6.plotly_chart(fig)
    
    col6.markdown('Medium (e.g. Canada and Singapore): The trend is positive but moderated, with GDP gains influenced by diverse economies. In North America and East Asia, the 2000s and 2010s show steady arrival increases, though diversification (e.g. Singapore) reduces tourism’s dominance.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['medium']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col6.plotly_chart(fig)
    
    col6.markdown('Low (e.g. Tanzania and India): The trend is positive but weak, with low GDP countries in Sub-Saharan Africa and South Asia showing modest arrival growth (e.g. Tanzania’s safaris). Infrastructure gaps and instability limit progress, with slight 2010s gains from eco-tourism.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(arv_dict['low']), ["decade","arv_1000","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="arv_1000",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col6.plotly_chart(fig)
    
    col7, col8 = st.columns([0.1, 5])
    
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
    col8.plotly_chart(fig7)

    
    length_dict = {'high' : ["SLB", "PNG", "KIR", "NPL", "GHA", "CRI", "KEN", "GMB", "LKA", "SYC"],
                   'medium' : ["RUS", "URY", "GTM", "GEO", "BWA", "BEN", "ZMB", "BHS", "GIN", "HRV"],
                   'low' : ["SMR", "NOR", "BDI", "CMR", "MYS", "MAC", "PER", "JPN", "PAK", "OMN"]}
    
    col8.markdown('High (e.g. Solomon Islands and Nepal): The trend is negative but less defined, with longer stays linked to lower GDP. In East Asia and Pacific and South Asia, the 2010s show a stay peak driven by experiential travel (e.g. Nepal’s mountaineering), though economic returns are limited. Regional effects, like Sub-Saharan Africa’s longer stays (e.g. Kenya) despite low GDP, suggest cultural or budget tourism influences.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['high']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="Relationship Between Length of Stay and GDP Per Capita", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12), title_x=0.3)
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col8.plotly_chart(fig)
    
    col8.markdown('Medium (e.g. Russia and Bahamas): The trend is negative with variability, with moderate stays tied to mixed GDP impacts. In Europe and Latin America, the 2000s and 2010s show slight increases, influenced by diverse attractions (e.g. Bahamas’ luxury and Russia’s vast tourism), balancing cost and experience.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['medium']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col8.plotly_chart(fig)
    
    col8.markdown('Low (e.g. SMR, Japan): The trend is negative, with shorter stays linked to high GDP. In Europe and East Asia, the 1990s and 2000s show brief visits due to costs (e.g. Japan’s high expenses), though the 2010s see some growth from niche tourism. The inverse pattern and less defined trend may reflect regional effects, such as Middle East luxury stays (e.g. Oman) countering the negative GDP link.')
    
    fig=px.line(tourism.loc[tourism['code'].isin(length_dict['low']), ["decade","length","code", 'year', 'country']].dropna().sort_values(by=['year', 'code']).reset_index(drop=True), x="year",y="length",color="country",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    fig.add_vline(x=2000, line_width=3, line_dash="dash", line_color="green")
    fig.add_vline(x=2010, line_width=3, line_dash="dash", line_color="green")
    fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    fig.update_yaxes(showticklabels=True)
    fig.update_xaxes(showticklabels=True)
    col8.plotly_chart(fig)










    
    
    
    
    
        
    # fig=px.scatter(tourism[["decade","gdp","tourists_per_1000","country"]].dropna(),x="tourists_per_1000",y="gdp",color="decade",hover_name='country',labels={'gdp': 'GDP', 'tourists_per_1000': 'Tourists (Per 1000)', 'decade' : 'Decade'}, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col4.plotly_chart(fig)
    
    # col4.markdown('outliers in kuwait, tajikstan, turkmenistan, bangladesh, libya, sudan, angola')
    

    
    # col5, col6 = st.columns([0.1, 5])
    
    # col6.markdown('arv_1000 for country by decade')
    
    # fig=px.scatter(tourism[["decade","gdp","arv_1000","country"]].dropna(),x="arv_1000",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col6.plotly_chart(fig)
    
    # fig=px.scatter(tourism[["decade","gdp","arv_1000","country"]].dropna().groupby(['country', 'decade']).mean().reset_index(),x="arv_1000",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, facet_col = "decade", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col6.plotly_chart(fig)
    

    
    
    # col7, col8 = st.columns([0.1, 5])
    
    # col8.markdown('length for country by decade')
    
    # fig=px.scatter(tourism[["decade","gdp","length","country"]].dropna(),x="length",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col8.plotly_chart(fig)
    
    # fig=px.scatter(tourism[["decade","gdp","length","country"]].dropna().groupby(['country', 'decade']).mean().reset_index(),x="length",y="gdp",color="decade",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, facet_col = "decade", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col8.plotly_chart(fig)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # fig32=px.scatter(tourism[["region","gdp","tourists_per_1000","country"]].dropna().groupby(['country', 'region']).mean().reset_index(),x="tourists_per_1000",y="gdp",color="region",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, facet_col = "region", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig32.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig32.update_yaxes(showticklabels=True)
    # fig32.update_xaxes(showticklabels=True)
    # col2.plotly_chart(fig32)
    
    # fig=px.scatter(tourism[["region","gdp","tourists_per_1000","country"]].dropna(),x="tourists_per_1000",y="gdp",color="region",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col2.plotly_chart(fig)
    
    # col5, col6 = ([0.1, 5])
    
    # fig=px.scatter(tourism[["region","gdp","arv_1000","country"]].dropna(),x="arv_1000",y="gdp",color="region",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col6.plotly_chart(fig)
    
    # fig=px.scatter(tourism[["region","gdp","arv_1000","country"]].dropna().groupby(['country', 'region']).mean().reset_index(),x="arv_1000",y="gdp",color="region",hover_name='country',labels=all_dict, height = 2000, width=400,title="", log_x=True, facet_col = "region", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col6.plotly_chart(fig)
    
    # col7, col8 = ([0.1, 5])
    
    # fig30=px.scatter(tourism[["region","gdp","length","country"]].dropna(),x="length",y="gdp",color="region",hover_name='country',labels=all_dict, height = 2000, width=400,title="", log_x=True, facet_col = "region", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig30.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig30.update_yaxes(showticklabels=True)
    # fig30.update_xaxes(showticklabels=True)
    # col8.plotly_chart(fig30)
    
    # fig=px.scatter(tourism[["region","gdp","length","country"]].dropna(),x="length",y="gdp",color="region",hover_name='country',labels=all_dict, height = 1000, width=400,title="", log_x=True, log_y = True)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col8.plotly_chart(fig)
    
    # col8.markdown('slight linear moderate negative correlation for Europe and Central Asia, Middle East and North Africa, and East Asia and Pacific')
    
    # fig=px.scatter(tourism[["region","gdp","length","country"]].dropna().groupby(['country', 'region']).mean().reset_index(),x="length",y="gdp",color="region",hover_name='country',labels=all_dict, height = 2000, width=400,title="", log_x=True, facet_col = "region", facet_col_wrap = 2, facet_col_spacing=0.1, log_y = True, facet_row_spacing=0.1)
    # fig.update_layout(showlegend=True,margin=dict(l=20,r=20,t=50,b=20),font=dict(size=12))
    # fig.update_yaxes(showticklabels=True)
    # fig.update_xaxes(showticklabels=True)
    # col8.plotly_chart(fig)
    
    


if selected == 'Conclusion':
    
    st.title('Conclusion')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if selected == 'Bibliography':
        st.title('Bibliography')
#         col1.markdown('Bibliography on Tourisms Economic Impact

# Below is a curated bibliography of sources that discuss the correlation between tourism and economic indicators such as GDP, tourist arrivals, country, and region. Each source provides expert insights into how tourism affects economies, with a focus on recent studies and data-driven analyses.





# World Travel & Tourism Council (WTTC). (2021). Travel & Tourism Economic Impact Research (EIR).





# Description: This report, in collaboration with Oxford Economics, provides a comprehensive analysis of the economic impact of travel and tourism across 184 countries and 28 regions. It highlights correlations between tourism’s contribution to global GDP (US$10.9 trillion in 2024, 10% of global GDP) and tourist arrivals, emphasizing regional variations and employment impacts (357 million jobs globally). The report includes data from 2015–2025 and forecasts to 2035, showing trends in GDP contribution and international visitor spending by country and region.



# Relevance: Discusses correlations between GDP, tourist arrivals, and regional economic contributions, with detailed metrics for specific countries.



# Source: WTTC Research Hub, wttc.org



# Behsudi, A. (2021). Impact of the Pandemic on Tourism. IMF Finance & Development.





# Description: This IMF study examines the economic impact of the COVID-19 pandemic on tourism-dependent economies, correlating tourist arrivals with GDP declines in 2020. It notes that tourism-dependent countries (e.g., African and Caribbean nations) experienced GDP contractions of up to 12–21%, compared to global averages, due to a drop in arrivals (65% globally in early 2021). The study highlights specific countries like Barbados and Seychelles, linking tourist arrivals to GDP and employment.



# Relevance: Provides evidence of the correlation between tourist arrivals and GDP declines, with country-specific data.



# Source: www.imf.org



# Statista. (2025). Travel and Tourism: Contribution to Global GDP 2023.





# Description: This report details the global contribution of travel and tourism to GDP (9.9 trillion USD in 2023, 9.1% of global GDP) and correlates it with international tourist arrivals by country and region. It highlights leading markets like the United States, China, and France (100 million arrivals in 2023), noting how arrivals drive GDP contributions. Forecasts for 2024 and 2034 are included, showing expected GDP growth tied to tourism recovery.



# Relevance: Correlates GDP with tourist arrivals across countries and regions, with a focus on recent data and projections.



# Source: www.statista.com



# Nhamo, G., Dube, K., & Chikodzi, D. (2021). Tourism Recovery and the Economic Impact: A Panel Assessment. ScienceDirect.





# Description: This study uses system-GMM estimation to analyze the economic impact of tourism on 46 countries, correlating tourist arrivals per capita and tourism receipts with GDP growth. It finds that a 1% increase in tourism receipts per capita boosts GDP per capita by 0.31% in the long run, with stronger effects in countries with higher tourism specialization. The study also explores non-linear relationships, showing diminishing returns at high tourism levels.



# Relevance: Establishes a direct correlation between tourist arrivals, tourism receipts, and GDP growth across multiple countries.



# Source: www.sciencedirect.com



# Fahimi, A., Akadiri, S. S., & others. (2022). Tourism and Economic Growth: A Global Study on Granger Causality and Wavelet Coherence. PMC.





# Description: This global study of 105 countries uses Granger causality and wavelet coherence to explore bidirectional causality between tourism (measured by arrivals and receipts) and GDP. It finds that tourism growth drives economic growth in most countries, with stronger correlations in regions like Europe and the Americas (2010–2017). The study highlights how economic growth also boosts tourism, creating a feedback loop.



# Relevance: Demonstrates bidirectional correlations between tourist arrivals, tourism revenue, and GDP across regions and countries.



# Source: www.ncbi.nlm.nih.gov



# Brida, J. G., & others. (2020). On the Empirical Relationship Between Tourism and Economic Growth. ScienceDirect.





# Description: This study analyzes the dynamics of tourism and economic growth in 80 countries from 1995–2016, using per capita GDP growth and international tourist arrivals per inhabitant. It identifies clusters of countries with high and low tourism performance, showing how tourism specialization correlates with GDP growth. The study notes that countries with higher tourist arrivals per capita (e.g., Uruguay vs. Brazil) have stronger economic impacts relative to their population size.



# Relevance: Correlates tourist arrivals per capita with GDP growth, highlighting country-specific and regional differences.



# Source: www.sciencedirect.com



# World Bank. (2025). Tourism and Competitiveness.





# Description: This report emphasizes tourism’s role in economic development, contributing US$10.9 trillion to global GDP in 2024 (10% of global GDP) and supporting 357 million jobs. It correlates international visitor spending (US$1.9 trillion) with GDP and job creation in countries like Sierra Leone, where tourism doubled arrivals and created 17,000 jobs. The report also discusses regional impacts, particularly in small island nations.



# Relevance: Links tourist arrivals and spending to GDP and employment, with a focus on developing countries and regions.



# Source: www.worldbank.org



# UN Tourism. (2024). International Tourism to Reach Pre-Pandemic Levels in 2024. UNWTO.





# Description: This report provides data on tourism’s economic recovery, estimating tourism direct GDP at US$3.3 trillion in 2023 (3% of global GDP). It correlates international tourist arrivals (1.3 billion in 2023, 88% of 2019 levels) with GDP contributions across regions, noting that the Middle East exceeded 2019 arrival levels by 22%. The report highlights how arrivals drive economic recovery in specific countries and regions.



# Relevance: Correlates tourist arrivals with tourism’s direct GDP contribution, with regional and country-specific insights.



# Source: www.unwto.org



# Kim, Y. R., & Song, H. (2022). Toward an Accurate Assessment of Tourism Economic Impact: A Systematic Literature Review. ScienceDirect.





# Description: This systematic review (1975–2020) evaluates methods for assessing tourism’s economic impact, emphasizing the need for dynamic causal models to link tourism (arrivals and receipts) with GDP. It critiques traditional approaches and highlights studies showing positive correlations between tourism receipts and GDP in countries like Mexico and Romania, with regional variations.



# Relevance: Discusses correlations between tourist arrivals, tourism receipts, and GDP, with a focus on methodological advancements.



# Source: www.sciencedirect.com



# Mize. (2025). The Economic Impact of Tourism: What You Need to Know.





# Description: This blog post outlines tourism’s economic contributions, noting its 10.4% share of global GDP in 2019 (US$10 trillion) and 7.6% in 2022. It correlates tourist arrivals with job creation (22 million jobs in 2022) and GDP in countries like South Africa (3.7% of GDP). The report emphasizes how tourist spending drives economic activity across regions.



# Relevance: Links tourist arrivals and spending to GDP and employment, with country-specific examples.



# Source: mize.tech')
    