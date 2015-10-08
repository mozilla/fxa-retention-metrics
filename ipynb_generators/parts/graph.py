import seaborn
import matplotlib.pyplot as plt

IN_IPYTHON = True
try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False

if IN_IPYTHON:
    seaborn.set(style='white')
    plt.figure(figsize=(16, 12))
    plt.title(TITLE, { 'fontsize': 26 })
    seaborn.heatmap(DATA_FRAME, annot=True, fmt='d', yticklabels=WEEKS, xticklabels=range(0, len(WEEKS)))
    # Rotate labels
    locs, labels = plt.yticks()
    plt.setp(labels, rotation=0)
    # Set axis font
    font = {
        'weight': 'bold',
        'size': 22
    }
    # Label axis
    plt.ylabel('Cohort Starting Week', **font)
    plt.xlabel('Retention Weeks', **font)

    print VOLUME_DATA_FRAME
