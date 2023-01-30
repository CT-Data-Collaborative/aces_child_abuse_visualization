import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd 
import chart_studio.tools as tls
import chart_studio.plotly as py


#Create Dataframe for the visuals
df = pd.DataFrame({"spacing":[1, 3, 5,  1, 3, 5,  1, 3, 5, 
                              1, 3, 5 ,1, 3, 5 , 1, 3, 5, 
                              1, 3, 5 , 1, 3, 5, 1, 3, 5, 
                              1, 3, 5],
                   
                   "data_values":[12.4, 1.5, 5.4,  7.5, 1.2, 5.5,  13.4, 1.5, 6.3, 
                                  13.3, 3.1, 6,  11.5, 0.7, 4.7,  16.3, 1.7, 8.3, 
                                  8.7, 1.3, 2.7,  21.2, 1.9, 12.2,  15.6, 2.9, 10.3, 
                                  9.5, 1, 3.4],
                   "bottom_error": [2, 0.7, 1.2,  3.9, 1, 4.5,  3.5, 1, 2.1, 
                                    2, 1.4, 1.4,  2.4, 0.4, 1.2,  3.1, 1, 2, 
                                    1.9, 0.4, 0.8,  5.4, 1.2, 3.5,  5.7, 2.1, 4.9, 
                                    1.7, 0.4, 1],
                   "top_error": [1.9, 0.6, 1.2, 7.6, 7.7, 18.7,  4.4, 2.8, 3.1,
                                 2.4, 2.6, 1.8,  3, 0.9, 1.7,  3.5, 2.3, 2.6, 
                                 2.4, 0.6, 1.2,  6.7, 3, 4.8,  8.2, 6.8, 8.3, 
                                 1.9, 0.7, 1.4],
                   
                   "breakdown":["Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused",
                                "Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused",
                                "Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused", "Insulted", "Hit/Kicked", "Sexually Abused",
                                "Insulted", "Hit/Kicked", "Sexually Abused"]
                   })

# print(df)

#Set paramaters for Bar charts
fig = go.Figure()
fig.add_trace(go.Bar(
        x=df.breakdown,
        y=df.data_values,

        error_y=dict(
            type='data',
            symmetric=False,
            array=df.top_error,
            arrayminus=df.bottom_error)
        ))

fig.update_traces(visible= True, selector=dict(type='bar'))


cols =["data_values"]

statewide = [list(df[item][0:3]) for item in cols]
asian = [list(df[item][3:6])  for item in cols]
black = [list(df[item][6:9])  for item in cols]
hispa = [list(df[item][9:12])  for item in cols]
white = [list(df[item][12:15])  for item in cols]
female = [list(df[item][15:18])  for item in cols]
male = [list(df[item][18:21])  for item in cols]
lgbt = [list(df[item][21:24])  for item in cols]
unsure = [list(df[item][24:27])  for item in cols]
hetero = [list(df[item][27:30])  for item in cols]
# print("statewide: ", statewide)
# print("asian: ", asian)
# print("black: ", black)
# print("hispa: ", hispa)
# print("white: ", white)
# print("female: ", female)
# print("male: ", male)
# print("lgbt: ", lgbt)
# print("unsure: ", unsure)
# print("hetero: ", hetero)

# Chart should display only the chart for the specified button, and can toggle between other charts, going back to the original 
dropdown1 =  dict(method = "restyle",
                  args = [{'y': statewide}],
                # args = [{'y': statewide, 'x': statewidex}],
                label = "Statewide")

dropdown2 =  dict(method = "restyle",
                args = [{'y': asian}],
                label = "Asian")

dropdown3 =  dict(method = "restyle",
                args = [{'y': black}],
                label = "Black")

dropdown4 =  dict(method = "restyle",
                args = [{'y': hispa}],
                label = "Hispanic")

dropdown5 =  dict(method = "restyle",
                args = [{'y': white}],
                label = "White")

dropdown6 =  dict(method = "restyle",
                args = [{'y': female}],
                label = "Female")

dropdown7 =  dict(method = "restyle",
                args = [{'y': male}],
                label = "Male")

dropdown8 =  dict(method = "restyle",
                args = [{'y': lgbt}],
                label = "Gay/Lesbian/Bisexual")

dropdown9 =  dict(method = "restyle",
                args = [{'y': unsure}],
                label = "Unsure")

dropdown10 =  dict(method = "restyle",
                args = [{'y': hetero}],
                label = "Heterosexual")

fig.update_layout(height=450,bargap=0.2, title="Child Abuse", title_x=0.5,
                  updatemenus=[dict(active=0,
                                    buttons=[dropdown1, dropdown2, dropdown3, dropdown4,
                                             dropdown5, dropdown6, dropdown7 ,dropdown8 ,
                                             dropdown9, dropdown10])
                               
                              ]) 

# fig.show()

# fig.write_html("child_abuse.html", auto_open=True)

pio.write_html(fig, file='child_abuse.html', auto_open=True)