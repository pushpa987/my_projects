from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')
grade_points = {
    'A+': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 0
}
@app.route('/s11', methods=['GET', 'POST'])
def s11():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,1.5,1.5,1.5,1.5] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)
    return render_template('s11.html')
@app.route('/s12', methods=['GET', 'POST'])
def s12():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
     
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        percentage = (total_points / total_credits) * 10  
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)
    return render_template('s12.html')
@app.route('/s21', methods=['GET', 'POST'])
def s21():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)   
    return render_template('s21.html')
@app.route('/s22', methods=['GET', 'POST'])
def s22():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)    
    return render_template('s22.html')
@app.route('/s31', methods=['GET', 'POST'])
def s31():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10     
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage) 
    return render_template('s31.html')
@app.route('/s32', methods=['GET','POST'])
def s32():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
    
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,1.5,1.5,1.5,2.0] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10        
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)   
    return render_template('s32.html')
@app.route('/s41', methods=['GET', 'POST'])
def s41():
    if request.method == 'POST':
        sub1 = request.form['Subject1']
        sub2 = request.form['Subject2']
        sub3 = request.form['Subject3']
        sub4 = request.form['Subject4']
        sub5 = request.form['Subject5']
        lab1 = request.form['Lab1']
        lab2 = request.form['Lab2']
        lab3 = request.form['Lab3']
        lab4 = request.form['Lab4']
     
        grades = [sub1, sub2, sub3, sub4, lab1, lab2, lab3]
        credits=[3,3,3,3,3,3,2,3] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)    
    return render_template('s41.html')
@app.route('/s42', methods=['GET', 'POST'])
def s42():
    if request.method == 'POST':
        Project = request.form['Project']   
    
        grades = [Project]
        credits=[12] # Assuming 4 subjects and 4 labs
        # Calculate percentage based on credits and grades
        total_credits = sum(credits)
        total_points = sum([grade_points[grade] * credit for grade, credit in zip(grades, credits)])
        percentage = (total_points / total_credits) * 10
        percentage = (total_points / total_credits) * 10   
        if percentage>75:
            return render_template('result.html', percentage=percentage) 
        elif percentage>65:
            return render_template('result1.html',percentage=percentage)  
        else:
            return render_template('result2.html',percentage=percentage)  
    return render_template('s42.html')
if __name__ == '__main__':
    app.run(debug=True)