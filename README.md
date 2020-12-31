"# sendemail_queue" 

This is my first micro project using REST API's and AWS Elastic Cache.
EXECUTION STEPS:

1. create a redis cluster in AWS elastic-cache and launch it.
2. create an EC2 instance, download the pem file and launch it.
3. using puttygen, create a private key file .ppk file.
4. using putty, create a session and connect to ec2 machine.
5. using filezilla, move the code files from local machine to ec2 machine.
6. Install all the necessary packages in the ec2 machine.
7. add inbound rules to accept custom tcp, port 6379 for security groups of both ec2 instance and redis server.
8. redis-cli -h demo-redis.cgnl6j.ng.0001.use2.cache.amazonaws.com -p 6379 -> use this cmd to run the redis server.
9. use rq worker cmd to run the worker thread in one session.
10. create another session to run the python file app.py.
11. In the postman, make post request with list of email-ids and messages as input json.
12. Each task i.e. (message will be send to its corresponding email-id) will be registered in the redis queue and the worker thread which was running in the background will pick the job from the queue and execute it(send email).
13. The waiting time for the job to get executed has been set it as 5sec for demo purpose.
