import seaborn
import matplotlib.pyplot as plt

IN_IPYTHON = True
try:
    __IPYTHON__
except NameError:
    IN_IPYTHON = False

if IN_IPYTHON:
    if "DATA_FRAME" in locals():
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

    if "WEEKLY_DATA" in locals():
            print WEEKLY_DATA
            fig = plt.figure(figsize=(16, 12))

            plt.title(TITLE, { 'fontsize': 26 })
            for item in WEEKLY_DATA:
                val = WEEKLY_DATA[item]
                plt.plot(val)
                ax = fig.add_subplot(111)
                for x,y in zip(range(15), val):
                    ax.annotate('%s' %y, xy=(x,y), size=15)

            plt.ylabel('Percentage')
            plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
            plt.xticks(range(15), WEEKS)
            plt.legend(WEEKLY_DATA.keys(), loc='lower left', prop={'size': 16})


            plt.ylim(-10, 110)
            plt.show()
