export default (context: any) => {
  if (context.store.state.user.isLoggedIn === false) {
    return context.redirect('/');
  }
  if (process.client) {
  const token = localStorage.getItem('token');
    if (!token && context.route.path !== '/login') {
      return context.redirect('/');
    }
  }
}