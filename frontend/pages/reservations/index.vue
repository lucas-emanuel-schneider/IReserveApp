<template>
  <div>
    <h2>Reservas atuais</h2>
    <div v-if="isLoading">
      Carregando...
    </div>
    <div v-else>
      <template v-if="reservations.length > 0">
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Estação</th>
              <th>Desmarcar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="reserv in reservations" :key="reserv.id">
              <td>{{ reserv.reservation_date }}</td>
              <td>{{ reserv.work_station_name }}</td>
              <td>
                <button @click="confirmDeleteReservation(reserv.id)">X</button>
              </td>
            </tr>
          </tbody>
        </table>
      </template>
      <template v-else>
        Você ainda não possui reservas.
      </template>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';
export default {
  data() {
    return {
      reservations: [],
      isLoading: true,
    };
  },
  methods: {
    ...mapActions('reservations', ['getReservationsAction', 'deleteReservationAction']),
    getToken() {
      const token = localStorage.getItem('token');
      if (!token) {
          this.$router.push('/');
          return false;
        }
        return token;
    },
    async getReservations() {
    const token = this.getToken()
    const userStorage = localStorage.getItem('user');
    const user = JSON.parse(userStorage)
    const { status, data } = await this.getReservationsAction({token, id: user.id})
      if (status === 200) {
        this.reservations = data;
        this.isLoading = false;
      }
    },
    async confirmDeleteReservation(reservId) {
      const shouldDelete = window.confirm('Tem certeza que deseja deletar esta reserva?');
      if (!shouldDelete) return
      const token = this.getToken()
      const { status } = await this.deleteReservationAction({ token, id: reservId });

      if (status !== 204 ) return window.alert('Não foi possível deletar a reserva.');

      window.alert('Reserva deletada!');
        this.getReservations();
    }
  },
  mounted() {
    this.getReservations()
  },
}
</script>

<style>

</style>