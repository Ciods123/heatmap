import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch

# Load the data from the Excel file
data = pd.read_excel(r"C:\Users\admin\Downloads\HEATMAP_UUDD+ (2).xlsx")
data_pivoted = data.pivot_table(index='proteins', columns='exp_condition', values='log2fc_log10fc', aggfunc='mean')

colors = ["#D81B60","#D81B60","#D81B60","#FFF","#1A237E","#1A237E","#1A237E"]
n_bins = 256
cmap_name = 'custom_cmap'
cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# Set up the plot
plt.figure(figsize=(8.1, 22.2))
plt.gca().set_facecolor('#EAFAF1')

heatmap_map=sns.heatmap(data_pivoted, cmap=cm, center=0, yticklabels=True, xticklabels=True, annot=False,cbar_kws={'location': 'right', 'pad': 0.08,'aspect': 60,'shrink':0.6},linewidths=0.1)
heatmap_map.set_yticklabels(heatmap_map.get_yticklabels(), fontsize=6)
heatmap_map.set_xticklabels(heatmap_map.get_xticklabels(), fontsize=6)

plt.xlabel('exp_condition',fontsize=10)
plt.ylabel('Proteins',fontsize=10)

legend_patches = [Patch(facecolor='#1A237E', label='log2fc_log10fc=<0.37'),
                  Patch(facecolor='#EAFAF1', label='-0.37=<log2fc_log10fc=>0.37'),
                  Patch(facecolor='#D81B60', label='log2fc_log10fc=>-0.37')]

plt.legend(handles=legend_patches, title='Expression', bbox_to_anchor=(0.59, 0.98), bbox_transform=plt.gcf().transFigure,
           loc='upper left', fontsize=8, title_fontsize=9)
plt.tight_layout()
# Save the plot as an SVG file
plt.savefig("tanuja.svg", format="svg")

# Show the plot
plt.show()