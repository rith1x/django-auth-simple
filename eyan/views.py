from django.shortcuts import render, redirect
from django.contrib import auth
import pyrebase
import requests

config = {
  "apiKey": "AIzaSyB_9GX3alo9qic2BI7o0semK-SvyplsCTo",
  "authDomain": "eyantraxdb.firebaseapp.com",
  "databaseURL": "https://eyantraxdb-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "eyantraxdb",
  "storageBucket": "eyantraxdb.appspot.com",
  "messagingSenderId": "1089761583519",
  "appId": "1:1089761583519:web:1099ca8ff5f004ae379daa"

}

firebase = pyrebase.initialize_app(config)

database = firebase.database()
auth = firebase.auth()
global local_id


def signIn(request):
    return render(request, "login.html")


global name

def postSignIn(request):
    global local_id
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print(user)
            if user is not None and "idToken" in user:
                print("entered if")
                idtoken = user["idToken"]
                user_info = auth.get_account_info(idtoken)
                local_id = user_info["users"][0]["localId"]
                return render(request, "welcome.html")
            else:
                print("else enter")
                return render(request, "login.html")

        except Exception as e:
            return render(request, "login.html")

    return render(request, "login.html")




def signUp(request):
    return render(request, "signup.html")


def postSignUp(request):
    global local_id
    name = request.POST.get("name")
    email = request.POST.get("email")
    passw = request.POST.get("password")
    
    try:
        user = auth.create_user_with_email_and_password(email, passw)
        auth.send_email_verification(user["idToken"])
    except Exception as e:
        return render(request, "signup.html")

    uid = user["localId"]
    local_id = uid
    print(uid)
    data = {
        "name": name,
        "status": "1",
        "email": email,
    }
    print(data)
    database.child("users").child(uid).child("details").set(data)
    return render(request, "login.html")

