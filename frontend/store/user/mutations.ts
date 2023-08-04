export default {
  setEmail(state: any, payload: any) {
    state.email = payload.email;
},
  setUsername(state: any, payload: any) {
    state.username = payload.username;
},
  setIsLoggedIn(state: any, payload: any) {
    state.isLoggedIn = true;
}
}