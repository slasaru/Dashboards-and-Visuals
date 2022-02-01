# based on this discussion https://stackoverflow.com/questions/64994341/gauge-needle-for-plotly-indicator-graph
# but updated: you can git it any required values and arrow will follow
# just make sure you keep the aspect ratio

from numpy import radians, cos, sin
from plotly import graph_objs as go

def runGauge():
    """
    Function to create a gauge chart (speedometer).
    """
  
    max_green = 100
    kpi = 120
    max_chart = 150
    current_value = 75
    max_yellow = max_chart
    
    #you can add also max_red level and put it into steps below
    fig, ax = plt.subplots(figsize=(10, 7))
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        delta = {'reference': kpi, 'decreasing': {'color': "green"}, 'increasing': {'color': "red"}, 'position': "top"},
        value = current_value,
        domain = {'x': [0,1], 'y': [0,1]},
        gauge = {
            'axis': {'range': [None, max_chart], 'tickwidth': 1, 'tickcolor': "darkblue", 'tickmode':'linear', 'dtick': 10},
            'bar': {'color': "#8DB600"}, 
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, max_green], 'color': '#7FFF00'},
                {'range': [max_green, max_yellow], 'color': 'yellow'},
            ],
            'threshold' : {'line': {'color': "maroon", 'width': 4}, 'thickness': 0.8, 'value': kpi}}
            , title="Stock Level, mln USD"
    ))

    fig.update_layout(
        font={'color': "black", 'family': "Arial", "size": 20},
        xaxis={'showgrid': False, 'showticklabels':False, 'range':[-1,1]},
        yaxis={'showgrid': False, 'showticklabels':False, 'range':[0,1]},
        plot_bgcolor="white",
        
        #Aspect ratio width/height is very important, otherwise the arrow will not be set correctly. Change carefully!
        width=700,
        height=410)

    theta = 180 - (180 * (current_value/max_chart)) 
    r= 0.9
    x_head = r * cos(radians(theta))*0.92
    y_head = r * sin(radians(theta))*1.1

    
    fig.add_annotation(
        ax=0,
        ay=0,
        axref='x',
        ayref='y',
        x=x_head,
        y=y_head,
        xref='x',
        yref='y',
        #you can play with arrow color / size, standoff below
        showarrow=True,
        arrowhead=1,
        arrowsize=1,
        arrowwidth=4,
        startstandoff=130
        )
    fig.show()


runGauge()