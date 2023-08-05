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
                <button @click="navigateToReservation(reserv.id)">X</button>
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
    ...mapActions('reservations', ['getReservationsAction']),
    async getReservations() {
    const token = localStorage.getItem('token');
      if (!token) {
          this.$router.push('/');
          return;
        }
    const userStorage = localStorage.getItem('user');
    const user = JSON.parse(userStorage)
    const { status, data } = await this.getReservationsAction({token, id: user.id})
      if (status === 200) {
        this.reservations = data;
        this.isLoading = false;
      }
    },
    navigateToReservation(reservId) {
      this.$router.push(`reservations/delete/${reservId}`);
    }
  },
  mounted() {
    this.getReservations()
  },
}
</script>

<style>

</style>