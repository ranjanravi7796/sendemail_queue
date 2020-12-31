from flask import Flask, request, jsonify,render_template,json
from logic import execute_task
from redis import Redis
from rq import Queue

app = Flask(__name__)

queue = Queue(connection=Redis()) #connection to redis queue


@app.route("/",methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        data = request.get_json()
        messages = data['messages']
        emailids = data['emailids']
        for receiver_email,message in zip(emailids,messages):
            print(receiver_email)
            print(message)
                    
            #put the job in redis queue, the worker thread running in bg will pick and execute it
            job = queue.enqueue(execute_task, args=(receiver_email,message))

            print(job.id) #printing job id and time to check
            print(job.enqueued_at)
        
        return render_template("success.html") #once all tasks were done, success page will be loaded
        
        
    else: #if the request is GET, simply display home page
        return render_template("home.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)