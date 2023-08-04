<template>
  <div class="login-container">
    <form @submit.prevent="handleSubmit">
      <input type="email" v-model="email" placeholder="Email" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapMutations } from 'vuex';
export default {
    data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    ...mapActions('user', ['loginUser']),
    ...mapMutations('user', ['setIsLoggedIn']),

    async handleSubmit() {
      const { email, password } = this;
      const response = await this.loginUser({email, password})
      if (response.isAuthenticated === true) {
        localStorage.setItem('token', response.token);
        this.setIsLoggedIn()
        this.$router.push('/reservations')
      }
    }
  }

}
</script>

<style>

</style>