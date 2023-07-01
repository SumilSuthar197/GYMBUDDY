# from tkinter import *
# from random import randint
#
# a = Tk()
# a.title('The dietician')
#
#
# def BMR():
#     protein = ['Yogurt(1 cup)', 'Cooked meat(3 Oz)', 'Cooked fish(4 Oz)', '1 whole egg + 4 egg whites', 'Tofu(5 Oz)']
#     fruit = ['Berries(80 Oz)', 'Apple', 'Orange', 'Banana', 'Dried Fruits(Handfull)', 'Fruit Juice(125ml)']
#     vegetable = ['Any vegetable(80g)']
#     grains = ['Cooked Grain(150g)', 'Whole Grain Bread(1 slice)', 'Half Large Potato(75g)', 'Oats(250g)',
#               '2 corn tortillas']
#     ps = ['Soy nuts(i Oz)', 'Low fat milk(250ml)', 'Hummus(4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt(125g)']
#     taste_en = ['2 TSP (10 ml) olive oil', '2 TBSP (30g) reduced-calorie salad dressin', '1/4 medium avocado',
#                 'Small handful of nuts', '1/2 ounce  grated Parmesan cheese',
#                 '1 TBSP (20g) jam, jelly, honey, syrup, sugar']
#
#     w = v3.get()
#     h = v4.get()
#     age = v5.get()
#     act = str(Lb.get(ACTIVE))
#     gender = Lb2.get(ACTIVE)
#
#     if gender == 'Male':
#         cal = int(88.362 + (13.397 * float(w)) + (4.799 * float(h)) - (5.677 * float(age)))
#         print(cal)
#     elif gender == 'Female':
#         cal = int(447.593 + (9.247 * float(w)) + (3.098 * float(h)) - (4.330 * float(age)))
#
#     if act == 'Sedentary (little or no exercise)':
#         cal = cal * 1.2
#
#     elif act == 'Lightly active (1-3 days/week)':
#         cal = cal * 1.375
#
#     elif act == 'Moderately active (3-5 days/week)':
#         cal = cal * 1.55
#
#     elif act == 'Very active (6-7 days/week)':
#         cal = cal * 1.725
#
#     elif act == 'Super active (twice/day)':
#         cal = cal * 1.9
#
#     print(cal)
#
#     if cal < 1500:
#         fin = StringVar()
#         l6 = Label(a, textvariable=fin, relief=RAISED)
#         fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l6.grid(row=0, column=3)
#
#         fin2 = StringVar()
#         l8 = Label(a, textvariable=fin2, relief=RAISED)
#         fin2.set("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)])
#         l8.grid(row=1, column=3)
#
#         fin3 = StringVar()
#         l9 = Label(a, textvariable=fin3, relief=RAISED)
#         fin3.set("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
#         l9.grid(row=2, column=3)
#
#         fin4 = StringVar()
#         l10 = Label(a, textvariable=fin4, relief=RAISED)
#         fin4.set("Dinner: " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)])
#         l10.grid(row=3, column=3)
#
#         fin5 = StringVar()
#         l11 = Label(a, textvariable=fin5, relief=RAISED)
#         fin5.set("Snack: " + fruit[randint(0, 5)])
#         l11.grid(row=4, column=3)
#
#
#     elif cal < 1800:
#         fin = IntVar()
#         l6 = Label(a, textvariable=fin, relief=RAISED)
#         fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l6.grid(row=0, column=3)
#
#         fin2 = StringVar()
#         l8 = Label(a, textvariable=fin2, relief=RAISED)
#         fin2.set("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l8.grid(row=1, column=3)
#
#         fin3 = StringVar()
#         l9 = Label(a, textvariable=fin3, relief=RAISED)
#         fin3.set("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
#         l9.grid(row=2, column=3)
#
#         fin4 = StringVar()
#         l10 = Label(a, textvariable=fin4, relief=RAISED)
#         fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)])
#         l10.grid(row=3, column=3)
#
#         fin5 = StringVar()
#         l11 = Label(a, textvariable=fin5, relief=RAISED)
#         fin5.set("Snack: " + fruit[randint(0, 5)])
#         l11.grid(row=4, column=3)
#
#     elif cal < 2200:
#         fin = StringVar()
#         l6 = Label(a, textvariable=fin, relief=RAISED)
#         fin.set("Breakfast: " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l6.grid(row=0, column=3)
#
#         fin2 = StringVar()
#         l8 = Label(a, textvariable=fin2, relief=RAISED)
#         fin2.set("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l8.grid(row=1, column=3)
#
#         fin3 = StringVar()
#         l9 = Label(a, textvariable=fin3, relief=RAISED)
#         fin3.set("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
#         l9.grid(row=2, column=3)
#
#         fin4 = StringVar()
#         l10 = Label(a, textvariable=fin4, relief=RAISED)
#         fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)])
#         l10.grid(row=3, column=3)
#
#         fin5 = StringVar()
#         l11 = Label(a, textvariable=fin5, relief=RAISED)
#         fin5.set("Snack: " + fruit[randint(0, 5)])
#         l11.grid(row=4, column=3)
#
#
#     elif cal >= 2200:
#         fin = StringVar()
#         l6 = Label(a, textvariable=fin, relief=RAISED)
#         fin.set("Breakfast: 2 " + protein[randint(0, 5)] + " + " + fruit[randint(0, 5)] + " + " + grains[randint(0, 4)])
#         l6.grid(row=0, column=3)
#
#         fin2 = StringVar()
#         l8 = Label(a, textvariable=fin2, relief=RAISED)
#         fin2.set("Lunch: " + protein[randint(0, 5)] + " + " + vegetable[0] + " + Leafy Greens" + grains[
#             randint(0, 4)] + " + " + taste_en[randint(0, 5)] + " + " + fruit[randint(0, 5)])
#         l8.grid(row=1, column=3)
#
#         fin3 = StringVar()
#         l9 = Label(a, textvariable=fin3, relief=RAISED)
#         fin3.set("Snack: " + ps[randint(0, 4)] + " + " + vegetable[0])
#         l9.grid(row=2, column=3)
#
#         fin4 = StringVar()
#         l10 = Label(a, textvariable=fin4, relief=RAISED)
#         fin4.set("Dinner: 2 " + protein[randint(0, 5)] + " + 2 " + vegetable[0] + " + Leafy Greens + 2 " + grains[
#             randint(0, 4)] + " + 2 " + taste_en[randint(0, 5)])
#         l10.grid(row=3, column=3)
#
#         fin5 = StringVar()
#         l11 = Label(a, textvariable=fin5, relief=RAISED)
#         fin5.set("Snack: " + fruit[randint(0, 5)])
#         l11.grid(row=4, column=3)
#
#
#
#
