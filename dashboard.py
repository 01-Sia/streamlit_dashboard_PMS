# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QD5G0LXDtl6HM-UAzdbe7u5DQVKOXp5H
"""

import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title = "PMS dashboard",
    layout = "wide",
    initial_sidebar_state="expanded"
)

# alt.themes.enable("dark")

df_data = pd.read_csv('PMS (2).csv')

# usecols=['Group Name','Duration','Received Project','str_category_name']

#sidebar
with st.sidebar:
  st.title('PMS analytics dashboard ')
  year_list= st.selectbox('Select the duartion',df_data['Duration'].unique())
  receival =  st.selectbox('Receival of project',df_data['Received Project'].unique())
  # group_name = st.selectbox('Select the department',df_data['Group Name'].unique())
  # selected_department = st.sidebar.selectbox('Select Department', ['Overall'] + df_data['Group Name'].unique())
  department_filter = st.selectbox('Select Department', ['All'] + list( df_data['Group Name'].unique()))


  color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
  selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
  # Filter the DataFrame
  # if selected_department == 'Overall':
  #    df_filtered = df_data
  # else:
  #    df_filtered = df_data[df_data['Group Name'] == selected_department]


"""PLOTS"""

# Heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    # input_df[input_x] = input_df[input_x].astype(str)
    # input_df[input_y] = input_df[input_y].astype(str)
    # input_df['Received Project'] = input_df['Received Project'].astype(str)
  
    # Filter for "yes" values in the "Received Project" column
    filtered_df = input_df[input_df['Received Project'] == 'Yes']
    
    # Group by input_y and input_x to count occurrences of "yes"
    df_counts = filtered_df.groupby([input_y, input_x]).size().reset_index(name='count')
    # df_counts = input_df.groupby([input_y, input_x],'Received Project').size().reset_index(name='count')
    heatmap = alt.Chart(df_counts).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="received project ", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title=" ", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):N',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
     
        ).properties(width= 1200,
                      # height=30
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        )
     
    return heatmap

# def scatterplot(input_df, input_x, input_y,input_color, input_color_theme):
    
#     # df_counts = input_df.groupby([input_y, input_x]).size().reset_index(name='count')
#     horizon = alt.Chart(input_df).mark_circle(
#       size = 80,
#   ).encode(
#       y=alt.Y(f'{input_y}:O',axis = alt.Axis(title =" funding organisation ", titleFontSize=18, titlePadding = 15, titleFontWeight=900,labelAngle=0)),
#       x=alt.X(f'{input_x}:O',axis = alt.Axis(title =" Cdac Outlay ",titleFontSize=18, titlePadding=15, titleFontWeight=900)),
#       color = alt.Color(f'{input_color}:N',
#                         legend =None,
#                         scale= alt.Scale(scheme= input_color_theme)),
#       tooltip=['Group Name','Received Project','Duration']


#       ).interactive(
#     ).properties(
#           width = 1100,
#           # height = 90
#       ).configure_axis(
#           labelFontSize=12,
#           titleFontSize=12
#       )

#     return horizon
def barchart(input_df, input_x, input_y,input_color, input_color_theme):
    # max_outlay_df = input_df.groupby([input_y, input_color])[input_x].max().reset_index()
    
    # Group by 'input_y' again and sum the max outlay values
    sum_outlay_df = input_df.groupby([input_y, input_color])[input_x].sum().reset_index()
    
    
    # df_counts = input_df.groupby([input_y, input_x]).size().reset_index(name='count')
    barchart = alt.Chart(sum_outlay_df).mark_bar(
      cornerRadiusTopLeft=3,
    cornerRadiusTopRight=3
  ).encode(
      y=alt.Y(f'{input_y}:O',axis = alt.Axis(title =" funding organisation ", titleFontSize=18, titlePadding = 15, titleFontWeight=900,labelAngle=0)),
      x=alt.X(f'{input_x}:O',axis = alt.Axis(title =" Cdac Outlay ",titleFontSize=18, titlePadding=15, titleFontWeight=900)),
      color = alt.Color(f'{input_color}:N',
                        legend =None,
                        scale= alt.Scale(scheme= input_color_theme)),
      order=alt.Order(
            f'sum({input_x}):O', 
            sort='descending'
        ),
      tooltip=[alt.Tooltip(f'{input_y}:N', title='CDAC Outlay'),
                 alt.Tooltip(f'{input_x}:N', title='Funding organisation'),
                 ]


      ).interactive(
    ).properties(
          width = 1200,
           # height = 30
      ).configure_axis(
          labelFontSize=12,
          titleFontSize=12
      )

    return barchart

#Donut chart
def donut_chart(input_data,input_text,input_color):
    
    # department_filter = st.sidebar.selectbox('Select Department', ['All'] + list(input_data['Group Name'].unique()))
    # filtered_data =  input_data['Group Name'] == filter

    # total_projects = len(filtered_data[filtered_data['Received Project'].notnull()])
    # yes_projects = len(filtered_data[filtered_data['Received Project'] == 'Yes'])
    # conversion_rate = (yes_projects / total_projects) * 100 if total_projects > 0 else 0
    
    if input_color == 'blue':
         chart_color = ['#29b5e8','#155F7A']
    if input_color == 'green':
         chart_color = ['#27AE60','#12783D']
    if chart_color == 'orange':
         chart_color = ['#F39C12','#875A12']
    if input_color == 'red':
            chart_color = ['#E743C','#781F16']

    source = pd.DataFrame({
      "Topic":['',input_text],
      "% value":[input_data,100-input_data]
  })

    plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                       scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text,''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
   ).properties(width=130, 
                height=130
   ).configure_mark(
        opacity=0.6
     ).configure_view(
        strokeWidth=0
     )
    # text = plot.mark_text(align='center', color=chart_color[0], font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(
    #     text=alt.value(f'{conversion_rate:.2f} %')
    # )

    return plot 


    

 

  


# def calculate_population_difference(input_df, input_year):
#   selected_year_data = input_df[input_df['year'] == input_year].reset_index()
#   previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
#   selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
#   return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

col = st.columns((1.5, 2.5, 2), gap='medium')

with col[0]:
#     st.markdown('#### Gains/Losses')




#     df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

#     if selected_year > 2010:
#         first_state_name = df_population_difference_sorted.states.iloc[0]
#         first_state_population = format_number(df_population_difference_sorted.population.iloc[0])
#         first_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[0])
#     else:
#         first_state_name = '-'
#         first_state_population = '-'
#         first_state_delta = ''
#     st.metric(label=first_state_name, value=first_state_population, delta=first_state_delta)

#     if selected_year > 2010:
#         last_state_name = df_population_difference_sorted.states.iloc[-1]
#         last_state_population = format_number(df_population_difference_sorted.population.iloc[-1])
#         last_state_delta = format_number(df_population_difference_sorted.population_difference.iloc[-1])
#     else:
#         last_state_name = '-'
#         last_state_population = '-'
#         last_state_delta = ''
#     st.metric(label=last_state_name, value=last_state_population, delta=last_state_delta)


    

#     if selected_year > 2010:
#         # Filter states with population difference > 50000
#         # df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference_absolute > 50000]
#         df_greater_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference > 50000]
#         df_less_50000 = df_population_difference_sorted[df_population_difference_sorted.population_difference < -50000]

#         # % of States with population difference > 50000
#         states_migration_greater = round((len(df_greater_50000)/df_population_difference_sorted.states.nunique())*100)
#         states_migration_less = round((len(df_less_50000)/df_population_difference_sorted.states.nunique())*100)
#         donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
#         donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
#     else:
#         states_migration_greater = 0
#         states_migration_less = 0
#         donut_chart_greater = make_donut(states_migration_greater, 'Inbound Migration', 'green')
#         donut_chart_less = make_donut(states_migration_less, 'Outbound Migration', 'red')
#   department_filter = st.sidebar.selectbox('Select Department', ['All'] + list(input_data['Group Name'].unique()))
    
    filtered_data =  df_data if department_filter =='ALL' else df_data[df_data['Group Name'] == department_filter]
    total_projects = len(filtered_data[filtered_data['Received Project'].notnull()])
    yes_projects = len(filtered_data[filtered_data['Received Project'] == 'Yes'])
    conversion_rate = (yes_projects / total_projects) * 100 if total_projects > 0 else 0
    donut_conversion = donut_chart(conversion_rate,'Conversion_Rate','green')
    migrations_col = st.columns((0.2, 1, 0.2))
    with migrations_col[1]:
        st.markdown('#### Conversion rate ')
        st.write('Proposal to Project conersion')
        st.altair_chart(donut_conversion)
    
    

    # migrations_col = st.columns((0.2, 1, 0.2))
    # with migrations_col[1]:
    # department_filter = st.sidebar.selectbox('Select Department', ['All'] + list(df_data['Group Name'].unique()))
    # st.markdown('#### Conversion rate ')
    # # donut = donut_chart(df_data,group_name,'blue')
    # donut = donut_chart(conversion_rate,'Conversion_rate,'blue')
    # st.altair_chart(donut, use_container_width = True )
         
         
         # st.altair_chart(sales_donut(df_data), use_container_width=True)
        # st.write('Inbound')
        # st.altair_chart(donut_chart_greater)
        # st.write('Outbound')
        # st.altair_chart(donut_chart_less)

with col[1]:
    st.markdown("#### Total")
    bar = barchart(df_data,'CDAC Outlay', 'Funding Organization','Group Name',selected_color_theme )
    st.altair_chart(bar, use_container_width=True)

    st.markdown('#### Projects in each category')
    heatmap = make_heatmap(df_data,'Group Name','str_category_name', 'Group Name',selected_color_theme)


    st.altair_chart(heatmap, use_container_width=True)



# with col[2]:
#     st.markdown('#### Projects vs CDAC outlay ')
#     bar = barchart(df_data,  'CDAC Outlay','Funding Organization', 'Group Name',selected_color_theme )
#     st.altair_chart(bar, use_container_width=True)
     

#     st.dataframe(df_selected_year_sorted,
#                  column_order=("states", "population"),
#                  hide_index=True,
#                  width=None,
#                  column_config={
#                     "states": st.column_config.TextColumn(
#                         "States",
#                     ),
#                     "population": st.column_config.ProgressColumn(
#                         "Population",
#                         format="%f",
#                         min_value=0,
#                         max_value=max(df_selected_year_sorted.population),
#                      )}
#                  )

# with st.expander('About', expanded=True):
#     st.write('''
#             - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
#             - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
#             - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
#             ''')


