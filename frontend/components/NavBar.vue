<template>
  <div>
  <NuxtLink to="/reservations">Suas Reservas</NuxtLink>
  <NuxtLink to="/reservations/create">Criar Reserva</NuxtLink>
  <button @click="clickHandler">Logout</button>

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

</style>