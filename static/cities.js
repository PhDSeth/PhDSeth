// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCoU_4EZb0mQLoemG7q5OJSWKhbJG4gd10",
  authDomain: "pluggportalen-f88da.firebaseapp.com",
  databaseURL: "https://pluggportalen-f88da-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "pluggportalen-f88da",
  storageBucket: "pluggportalen-f88da.appspot.com",
  messagingSenderId: "219161241102",
  appId: "1:219161241102:web:47e0e8f4ba95b43d3f7e5f",
  measurementId: "G-XZ6VPQKP2L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);