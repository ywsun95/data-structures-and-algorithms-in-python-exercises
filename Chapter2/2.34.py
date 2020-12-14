
import matplotlib.pyplot as plt


def character_chart(document):
    """Draw the bar-chart plot of the frequencies of each alphabet character."""
    frq = dict()
    for s in document:    # type: str
        if s.isalpha():
            if s.lower() in frq:
                frq[s.lower()] += 1
            else:
                frq[s.lower()] = 1

    plt.xlabel("characters")
    plt.ylabel("frequencies")
    plt.title("the frequencies of each alphabet character")
    x_axis = sorted(frq, key=lambda x: x)
    y_axis = [frq[i] for i in x_axis]
    bar_list = plt.bar(x_axis, y_axis, tick_label=x_axis)
    for bar in bar_list:        # show nums
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, str(height), ha='center')
    plt.show()


if __name__ == '__main__':
    doc = """
        Write a Python program that inputs a document and then outputs a bar-
        chart plot of the frequencies of each alphabet character that appears in
        that document."""
    character_chart(doc)
