export default {
  setEmail(state: any, payload: string) {
    state.email = payload;
},
  setUsername(state: any, payload: string) {
    state.username = payload;
},
  setUserId(state:any, id: number) {
    state.userId = id;
  },
  setIsLoggedIn(state: any, payload: boolean) {
    state.isLoggedIn = payload;
}
}