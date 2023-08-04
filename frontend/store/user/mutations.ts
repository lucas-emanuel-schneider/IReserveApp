export default {
  setEmail(state: any, payload: any) {
    state.email = payload.email;
},
  setUsername(state: any, payload: any) {
    state.username = payload.username;
},
  setUserId(state:any, id: number) {
    state.userId = id;
  },
  setIsLoggedIn(state: any, payload: boolean) {
    state.isLoggedIn = payload;
}
}