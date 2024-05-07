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
alt.themes.enable("dark")

df = pd.read_csv("PMS (2).csv")
usecols=['Group Name','Duration','Received Project','str_category_name']

#sidebar
with st.sidebar:
  st.title('PMS analytics dashboard ')
  year_list= st.selectbox('Select the duartion',df['Duration'].unique())
  receival =  st.selectbox('Reveival of project',df['Received Project'].unique())
  group_name = st.selectbox('Select the department',df['Group Name'].unique())
  color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
  selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

"""PLOTS"""

# Heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    df_counts = input_df.groupby([input_y, input_x]).size().reset_index(name='count')
    heatmap = alt.Chart(df_counts).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="received project ", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="department", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        )
    # height=300
    return heatmap

def horizon_graph(input_df, input_x, input_y,input_color, input_color_theme):
  horizon = alt.Chart(input_df).mark_area(
      clip = True,
      interpolate = 'monotone',
      opacity = 0.6,
  ).encode(
      y=alt.Y(f'{input_y}:O',axis = alt.Axis(title ="departments ", titleFontSize=18, titlePadding = 15, titleFontWeight=900,labelAngle=0)),
      x=alt.X(f'{input_x}:O',axis = alt.Axis(title ="dora",titleFontSize=18, titlePadding=15, titleFontWeight=900,labelAngle=0)),
      color = alt.Color(input_color,
                        legend =None,
                        scale= alt.Scale(scheme= input_color_theme)),


      ).properties(
          width = 900,
          height = 90
      ).configure_axis(
          labelFontSize=12,
          titleFontSize=12
      )

  return horizon

# #Donut chart
# def donut_chart(input_response,input_text,input_color):
#   if input_color == 'blue':
#     chart_color = ['#29b5e8','#155F7A']
#   if input_color == 'green':
#     chart_color = ['#27AE60','#12783D']
#   if chart_color == 'orange':
#     chart_color = ['#F39C12','#875A12']
#   if input_color == 'red':
#     chart_color = ['#E743C','#781F16']

#   source = pd.DataFrame({
#       "Topic":['',input_text],
#       "% value":[100-input_response,input_response]
#   })

#   plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
#       theta="% value",
#       color= alt.Color("Topic:N",
#                       scale=alt.Scale(
#                           #domain=['A', 'B'],
#                           domain=[input_text, ''],
#                           # range=['#29b5e8', '#155F7A']),  # 31333F
#                           range=chart_color),
#                       legend=None),
#   ).properties(width=130, height=130)

#   text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
#   plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
#       theta="% value",
#       color= alt.Color("Topic:N",
#                       scale=alt.Scale(
#                           # domain=['A', 'B'],
#                           domain=[input_text, ''],
#                           range=chart_color),  # 31333F
#                       legend=None),
#   ).properties(width=130, height=130)
#   return plot_bg + plot + text

# def calculate_population_difference(input_df, input_year):
#   selected_year_data = input_df[input_df['year'] == input_year].reset_index()
#   previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
#   selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
#   return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)

col = st.columns((1.5, 4.5, 2), gap='medium')

# with col[0]:
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


#     st.markdown('#### States Migration')

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

#     migrations_col = st.columns((0.2, 1, 0.2))
#     with migrations_col[1]:
#         st.write('Inbound')
#         st.altair_chart(donut_chart_greater)
#         st.write('Outbound')
#         st.altair_chart(donut_chart_less)

with col[0]:
    st.markdown("#### Total")
    horizon = horizon_graph(df, 'Group Name', 'Duration', 'Group Name',selected_color_theme )
    st.altair_chart(horizon, use_container_width=True)
    heatmap = make_heatmap(df, 'Received Project', 'Group Name', 'Group Name',selected_color_theme)


    st.altair_chart(heatmap, use_container_width=True)



# with col[2]:
#     st.markdown('#### Top States')

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

#     with st.expander('About', expanded=True):
#         st.write('''
#             - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
#             - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
#             - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
#             ''')

