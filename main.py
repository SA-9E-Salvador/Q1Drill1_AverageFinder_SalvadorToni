from pyscript import document

def compute_average(event):
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    average = (score1 + score2) / 2

    if average >= 95:
        result = "With flying colors!"
    elif average >= 75:
        result = "Yep"
    else:
        result = "Sadly no :("

    document.getElementById("average").innerText = round(average, 2)
    document.getElementById("result").innerText = result

