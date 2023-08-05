<template>
  <div class="login-container">
    <div class="login-form">
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" v-model="email" id="email" required />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" v-model="password" id="password" required />
        </div>
        <div class="button-container">
        <button type="submit" class="login-button">Login</button>
        </div>
      </form>
    </div>
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
    ...mapMutations('user', ['setIsLoggedIn', 'setUsername', 'setEmail', 'setUserId']),

    async handleSubmit() {
      const { email, password } = this;
      const response = await this.loginUser({email, password})
      if (response.isAuthenticated === true) {
        localStorage.setItem('token', response.token);
        localStorage.setItem('user', JSON.stringify(response.user));

        this.setIsLoggedIn(true)
        this.setEmail(response.user.email)
        this.setUsername(response.user.username)
        this.setUserId(response.user.id)
        this.$router.push('/reservations')
      }
    }
  }

}
</script>

<style>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
  background-color: #282c34;
}

.login-form {
  width: 30rem;
  padding: 20px;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  font-weight: bold;
}

.login-form input {
  width: 90%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;

}

.login-button {
  width: 150px;
  height: 50px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-weight: bold;
  font-size: 16px;
}

.login-button:hover {
  background-color: #0056b3;
}

.login-button:focus,
.login-button:active {
  color: #fff;
  outline: none;
}

</style>