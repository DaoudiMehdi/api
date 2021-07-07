
from flask import Flask  ,request , flash , jsonify
import requests
import json
app= Flask(__name__)

app.config["SECRET_KEY"] = 'Mehdi'

header ={"Content-Type": "application/json; charset=utf-8",
                
                "Authorization" : "Basic NGVjMjRkMDItZjQwMi00MDNkLTg4YjUtMWJlOGQ3ODgzODhi"
}


list=[]

@app.route("/" , methods = ['GET', 'POST'])
def send():
    if request.method == 'POST':
            sub_id = request.form.get("sub_id")
            message = request.form.get("message")

            payload = {"app_id" : "f17bc311-f05b-434a-b916-b2c798195aba",
                "include_player_ids": ["{}".format(sub_id)],
                "contents": {"en": "{}".format(message)}}

            req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))

            if req.status_code == 200 :
                data= {
                "sub_id":sub_id,
                "message":message,
                 }
                list.append(data)
                flash("Message envoyér")

            else:
                flash("Message non envoyér")
                
            return jsonify(list)
    else:
        flash("Message non envoyér")


if __name__ == "__main__":
    app.run(debug=True)