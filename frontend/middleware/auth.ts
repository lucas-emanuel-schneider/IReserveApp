export default (context: any) => {
  const logged = context.store.state.user.isLoggedIn
  if (logged) return
  if (process.client) {
  const token = localStorage.getItem('token');
  if (!token && context.route.path !== '/login' && !logged) {
      return context.redirect('/');
    }
  }
}