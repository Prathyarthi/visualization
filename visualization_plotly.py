import plotly.graph_objects as go
import seaborn as sns

# Plotly is more interactive as compared to matplotlib and seaborn

# fig = go.Figure()
# fig.add_trace(go.Scatter(x = [1,2,3,4,5],y = [6,7,8,9,10],mode="markers"))
# fig.show()


# fig.add_trace(go.Scatter(x = [1,2,3,4,5],y = [6,7,8,9,10],mode="lines"))
# fig.show()

# tips = sns.load_dataset('tips')
# fig = go.Figure()
# fig.add_trace(go.Scatter(x = tips.total_bill,y = tips.tip,mode="markers"))
# fig.show()

# fig = go.Figure()
# fig.add_trace(go.Bar(x = [1,2,3,4,5],y = [6,7,8,9,10]))
# fig.show()


# fig = go.Figure()
# fig.add_trace(go.Histogram(x = [1,2,3,3,4,4,4,4,5]))
# fig.show()

# tips = sns.load_dataset('tips')
# fig = go.Figure()
# fig.add_trace(go.Scatter(x = tips.total_bill,y = tips.tip,mode="markers",marker_size = 5*tips['size']))      # marker_size is basically size of the dots, here, as the size(number of people going to restaurant) increases, the size of the marker also increases
# fig.show()

# 3D Scatterplot
tips = sns.load_dataset('tips')
fig = go.Figure()
fig.add_trace(go.Scatter3d(x = tips.total_bill,y = tips.tip,mode="markers",z = tips['size']))      
fig.show()