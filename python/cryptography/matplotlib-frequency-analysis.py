import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"

code = """
Qu'est-ce que le Lorem Ipsum?
Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.
"""

letter_counts = [code.count(l) for l in alphabet]
letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

plt.bar(range(26), letter_counts, color=letter_colors)
plt.xticks(range(26), alphabet) # letter labels on x-axis
plt.tick_params(axis="x", bottom=False) # no ticks, only labels on x-axis
plt.title("Frequency of each letter")
plt.savefig("output.png")
