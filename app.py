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
        job_ids = []
        job_register_time = []
        for receiver_email,message in zip(emailids,messages):
            print(receiver_email)
            print(message)
                    
            #put the job in redis queue, the worker thread running in bg will pick and execute it
            job = queue.enqueue(execute_task, args=(receiver_email,message))
            job_ids.append(job.id)
            job_register_time.append(job.enqueued_at)
        
        job_dict = {"job_id_list":job_ids, "job_register_list":job_register_time}
        return jsonify(job_dict)      #return job details as response
        
    else: #if the request is GET, simply display home page
        return render_template("home.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)