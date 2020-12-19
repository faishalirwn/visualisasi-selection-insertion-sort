import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):
    # Helper function to swap elements i and j of list A

    if i != j:
        A[i], A[j] = A[j], A[i]


def insertionsort(A):
    # In-place insertion sort

    for i in range(1, len(A)):
        x = A[i]
        j = i - 1
        # j = i <- other version
        while j >= 0 and A[j] > x:
        # while j > 0 and A[j-1] > A[j]: <- other version
            A[j+1] = A[j]
            # swap(A, j, j - 1) <- other version
            j -= 1
            yield A
        A[j+1] = x
        i += 1
        yield A


def selectionsort(A):
    # In-place selection sort
    if len(A) == 1:
        return

    for i in range(len(A)):
        # Find minimum unsorted value.
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A


if __name__ == "__main__":
    # Get user input to determine range of integers (1 to N)
    N = int(input("Enter number of integers: "))

    # Build and randomly shuffle list of integers.
    A1 = [x + 1 for x in range(N)]
    A2 = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A1)
    random.shuffle(A2)


    # Get appropriate generator to supply to matplotlib FuncAnimation method.
    title1 = "Insertion sort"
    generator1 = insertionsort(A1)
    title2 = "Selection sort"
    generator2 = selectionsort(A2)

    # Initialize figure and axis.
    fig = plt.figure(1)
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_title(title1)
    ax2.set_title(title2)

    ax1.set(xticklabels=[])
    ax1.set(yticklabels=[])
    ax1.tick_params(bottom=False)
    ax1.tick_params(left=False)
    ax2.set(xticklabels=[])
    ax2.set(yticklabels=[])
    ax2.tick_params(bottom=False)
    ax2.tick_params(left=False)


    # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
    # list of rectangles (with each bar in the bar plot corresponding
    # to one rectangle), which we store in bar_rects.
    bar_rects1 = ax1.bar(range(len(A1)), A1, align="edge")
    bar_rects2 = ax2.bar(range(len(A2)), A2, align="edge")


    # Set axis limits. Set y axis upper limit high enough that the tops of
    # the bars won't overlap with the text label.
    ax1.set_xlim(0, N+1)
    ax1.set_ylim(0, int(1.2 * N))

    ax2.set_xlim(0, N+1)
    ax2.set_ylim(0, int(1.2 * N))

    # Place a text label in the upper-left corner of the plot to display
    # number of operations performed by the sorting algorithm (each "yield"
    # is treated as 1 operation).
    text1 = ax1.text(0.02, 0.95, "", transform=ax1.transAxes)
    text2 = ax2.text(0.02, 0.95, "", transform=ax2.transAxes)


    # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
    # To track the number of operations, i.e., iterations through which the
    # animation has gone, define a variable "iteration". This variable will
    # be passed to update_fig() to update the text label, and will also be
    # incremented in update_fig(). For this increment to be reflected outside
    # the function, we make "iteration" a list of 1 element, since lists (and
    # other mutable objects) are passed by reference (but an integer would be
    # passed by value).
    # NOTE: Alternatively, iteration could be re-declared within update_fig()
    # with the "global" keyword (or "nonlocal" keyword).
    iteration = [0]

    def update_fig(A, rects,text, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim1 = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(
                                       bar_rects1,text1, iteration), frames=generator1, interval=1,
                                   repeat=False)

    anim2 = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(
                                       bar_rects2,text2, iteration), frames=generator2, interval=1,
                                   repeat=False)
    plt.show()
