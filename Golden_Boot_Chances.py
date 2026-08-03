import csv
import turtle

print("Welcome to the Sports Heroes project")
print("We are going to do some analysis on FIFA World Cup Golden Boot winners.")
print("Please see the file analysis.dat for the results.")

def print_line(report_line):
    filename = 'analysis.dat'
    with open(filename, mode='a') as file:
        file.write(report_line)

def print_table(table):
    filename = 'analysis.dat'
    with open(filename, mode='a') as file:
        all_keys = list(table[0].keys())

        keys_line = ''
        for key in all_keys:
            keys_line = keys_line + key + (15 - len(key)) * ' '
          
        file.write(keys_line + '\n')

        for data in table:
            values_line = ''
            for values in data.values():
                values_line = values_line + str(values) + (15 - len(str(values))) * ' '
            file.write(values_line + '\n')

def initialize():
    filename = 'analysis.dat'
    with open(filename, mode='w') as file:
        file.write('Analysis Results \n\n')

def print_set(winner_set):
    filename = 'analysis.dat'
    with open(filename, mode='a') as file:
        if not winner_set:
            file.write("None\n\n")
            return
        for winner in winner_set:
            file.write(winner + ' , ')
        file.write('\n\n')

def readcsvdata(tournament_name):
    filename = tournament_name + '.csv'
    with open(filename, mode='r') as file:
        csvFile = csv.DictReader(file)
        tournament_data = list(csvFile)
    return tournament_data




def draw_bar_chart(labels, values, chart_title):
    turtle.clearscreen()
    screen = turtle.Screen()
    screen.title(chart_title)
    screen.setup(width=700, height=500)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    # Draw Title
    t.penup()
    t.goto(0, 200)
    t.write(chart_title, align="center", font=("Arial", 16, "bold"))
    
 
    start_x = -250
    start_y = -150
    
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.forward(500) 
    if not values:
        return
        
    max_val = max(values)
    bar_width = 40
    spacing = 20
    
 
    for i in range(min(len(labels), 7)): 
        height = (values[i] / max_val) * 250
        
        # Move to bar start
        t.penup()
        t.goto(start_x + 20 + i*(bar_width + spacing), start_y)
        t.pendown()
        
      
        t.fillcolor("steelblue")
        t.begin_fill()
        t.left(90)
        t.forward(height)
        t.right(90)
        t.forward(bar_width)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()
        
        
        t.penup()
        t.goto(start_x + 20 + i*(bar_width + spacing) + bar_width/2, start_y + height + 5)
        t.write(str(values[i]), align="center", font=("Arial", 10, "bold"))
        
        
        t.goto(start_x + 20 + i*(bar_width + spacing) + bar_width/2, start_y - 20)
        t.write(labels[i], align="center", font=("Arial", 8, "normal"))



def analyze(tname, tdata):
    winners_list = [winner['Name'] for winner in tdata]
    winners_set = set(winners_list)

    print_line('Reporting for ' + tname + '\n')
    print_line('Total Awards Given : ' + str(len(winners_list)) + '\n')
    print_line('Unique Winners : ' + str(len(winners_set)) + '\n\n')

    
    country_goals = {}
    for row in tdata:
        country = row['Country']
        goals = int(row['Goals'])
        country_goals[country] = country_goals.get(country, 0) + goals
    
    
    sorted_countries = sorted(country_goals.items(), key=lambda x: x[1], reverse=True)
    
    print_line("--- Top Countries by Total Golden Boot Goals ---\n")
    for country, goals in sorted_countries:
        print_line(f"{country}: {goals} goals\n")
    print_line("\n")

    
    top_country_names = [item[0] for item in sorted_countries]
    top_country_goals = [item[1] for item in sorted_countries]
    
    
    draw_bar_chart(top_country_names, top_country_goals, "Total Golden Boot Goals by Country")

    return winners_set

def comparative_analysis(winner_set1, winner_set2, label1, label2):
    winners_both = winner_set1 & winner_set2
    winners_only1 = winner_set1 - winner_set2
    winners_only2 = winner_set2 - winner_set1

    print_line(f'--- Comparative Analysis: {label1} vs {label2} ---\n\n')
    
    print_line(f'Winners in Both ({len(winners_both)}):\n')
    print_set(winners_both)
    
    print_line(f'Winners ONLY in {label1} ({len(winners_only1)}):\n')
    print_set(winners_only1)
    
    print_line(f'Winners ONLY in {label2} ({len(winners_only2)}):\n')
    print_set(winners_only2)



initialize()

worldcup_data = readcsvdata('WorldCupGoldenBoot')


all_winners = analyze('World Cup Golden Boot All-Time', worldcup_data)


data_20th_century = [row for row in worldcup_data if int(row['Year']) < 2000]
data_21st_century = [row for row in worldcup_data if int(row['Year']) >= 2000]

set_20th = set([row['Name'] for row in data_20th_century])
set_21st = set([row['Name'] for row in data_21st_century])


comparative_analysis(set_20th, set_21st, "20th Century", "21st Century")

print("\n[!] Check the 'analysis.dat' file for text results.")
print("[!] A Turtle graphics window is open. Close it to end the script.")
turtle.done()
