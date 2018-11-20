from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')
@app.route("/marks",methods=['POST','GET'])
def marks():
    if(request.method=='POST'):
        getname=request.form['name']
        getregno=request.form['regno']
        getsem=request.form['sem']
        getcollege=request.form['college']

        getsub1name=request.form['sub1name']
        getsub1mark=request.form['sub1mark']
        getsub1tmark=request.form['sub1tmark']
        getsub2name=request.form['sub2name']
        getsub2mark=request.form['sub2mark']
        getsub2tmark=request.form['sub2tmark']
        getsub3name=request.form['sub3name']
        getsub3mark=request.form['sub3mark']
        getsub3tmark=request.form['sub3tmark']
        getsub4name=request.form['sub4name']
        getsub4mark=request.form['sub4mark']
        getsub4tmark=request.form['sub4tmark']


        sub1mark=int(getsub1mark)
        sub1tmark=int(getsub1tmark)

        sub2mark=int(getsub2mark)
        sub2tmark=int(getsub2tmark)
        
        sub3mark=int(getsub3mark)
        sub3tmark=int(getsub3tmark)
        
        sub4mark=int(getsub4mark)
        sub4tmark=int(getsub4tmark)

        

        percent_sub1=sub1mark/sub1tmark*100
        percent_sub2=sub2mark/sub2tmark*100
        percent_sub3=sub3mark/sub3tmark*100
        percent_sub4=sub4mark/sub4tmark*100

        sublist=[percent_sub1,percent_sub2,percent_sub3,percent_sub4]

        result_list=[]
        
        for i in sublist:
                
                if i>=50 and i<58:
                        
                        grade='D+'
                        result='Pass'
                
                elif i>=58 and i<65:
                        
                        grade='C'
                        result='Pass'
                
                elif i>=65 and i<72:
                        
                        grade='C+'
                        result='Pass'

                elif i>=72 and i<79:
                        
                        grade='B'
                        result='Pass'

                elif i>=79 and i<86:
                        
                        grade='B+'
                        result='Pass'

                elif i>=86 and i<93:
                        
                        grade='A'
                        result='Pass'

                elif i>=93 and i<=100:
                        
                        grade='A+'
                        result='Pass'
                
                else:
                        grade='D'
                        result='Fail'

                result_list.append(grade)
                result_list.append(result)

        for j in result_list:

                if j=='Fail':
                        semester_result='Fail'
                        break
                else:
                        semester_result='Pass'
        
        
        return render_template('/results.html',final_result=semester_result,list=result_list,a=getname,b=getregno,c=getsem,d=getcollege,e=getsub1name,e1=getsub1mark,e2=getsub1tmark,f=getsub2name,f1=getsub2mark,f2=getsub2tmark,g=getsub3name,g1=getsub3mark,g2=getsub4tmark,h=getsub4name,h1=getsub4mark,h2=getsub4tmark)

if(__name__=='__main__'):
        app.run(debug=True)






            
        



