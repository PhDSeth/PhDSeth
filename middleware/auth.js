// Middleware will redirect the users to where we want them to be
// for example, for the first time u user login, we might not have info about them, auth wont be triggered. 

//This middleware should run before page load, to do that we need to register the middleware

export default function ({app, route, redirect}){
    if (route.path === '/LoggedInContent/PersonalPage' ) {
      //we are on a protected route
      if(!app.$fire.auth.currentUser) {
        //take them to sign in page
        return redirect('/auth/signin')
      }
    } else if (route.path === '/LoggedInContent/PersonalPage') {
      if(!app.$fire.auth.currentUser) {
        //leave them on the sign in page
      } else {
        return redirect('/')
      }
    }
  }