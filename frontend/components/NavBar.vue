<template>
  <div class="navbar-container">
    <div class="navbar-link-container">
      <NuxtLink to="/reservations" class="navbar-link">Suas Reservas</NuxtLink>
      <NuxtLink to="/reservations/create" class="navbar-link">Criar Reserva</NuxtLink>
    </div>
  <button @click="clickHandler" class="navbar-button">Logout</button>

  </div>
</template>

<script>
  import { mapMutations } from 'vuex';
export default {

  methods: {
    ...mapMutations('user', ['setIsLoggedIn']),

    clickHandler() {
        localStorage.removeItem('token');
        this.setIsLoggedIn(false)
        this.$router.push('/')
    },
  }
}
</script>

<style>
.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.navbar-link-container {
  display: flex;
  align-items: center;
}

.navbar-link {
  text-decoration: none;
  color: #007bff;
  font-weight: bold;
  margin-right: 20px;
  transition: color 0.3s ease;
}

.navbar-link:hover {
  color: #0056b3;
}

.navbar-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.footer-button:hover {
  background-color: #0056b3;
}

</style>