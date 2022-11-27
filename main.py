import pyrebase

config = {
  "apiKey": "AIzaSyA3ZIwKbwBIKACaWGck5XK2lk702uSVwmc",
  "authDomain": "pythonimage-e1b27.firebaseapp.com",
  "projectId": "pythonimage-e1b27",
  "databaseURL":"https://pythonimage-e1b27.firebaseapp.com",
  "storageBucket": "pythonimage-e1b27.appspot.com",
  "messagingSenderId": "71405559942",
  "appId": "1:71405559942:web:b9032b719aa260508af107",
  "measurementId": "G-6R053D1367"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_local = "my img.jpg"
path_on_cloud = "images/demo.jpg"

storage.child(path_on_cloud).put(path_local)
