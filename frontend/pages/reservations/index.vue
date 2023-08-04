<template>
<div>
  <h1>Página de reservas, onde vai ta as tuas reservas já feitas!</h1>
  <div v-for="reserv in reservations" :key="reserv.id">
    {{ reserv.title }}
</div>
</div>
</template>

<script>
  import { mapActions, mapState } from 'vuex';
export default {
  data() {
    return {
      reservations: []
    };
  },
  methods: {
    ...mapActions('reservations', ['getReservationsAction']),
    ...mapState('user', ['user_id']),
    async getReservations() {
    const token = localStorage.getItem('token');
        if (!token) {
          this.$router.push('/');
          return;
        }
      const id = this.user_id;
    const { status, data } = await this.getReservationsAction(token, id)
    }
  },
  mounted() {
    this.getReservations()
  },
}
</script>

<style>

</style>