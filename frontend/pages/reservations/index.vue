<template>
  <div class="reservation-container">
    <h2>Reservas atuais</h2>
    <div v-if="isLoading">
      <Loading />
    </div>
    <div v-else>
      <template v-if="reservations.length > 0">
        <table class="reservation-table">
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
              <td class="center-button">
                <button @click="confirmDeleteReservation(reserv.id)" class="delete-button">X</button>
              </td>
            </tr>
          </tbody>
        </table>
      </template>
      <template v-else>
        <p class="no-reservation-message">Você ainda não possui reservas.</p>
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
.reservation-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.reservation-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.reservation-table th {
  background-color: #007bff;
  color: #fff;
  padding: 10px;
  text-align: center;
}

.reservation-table td {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.center-button {
  text-align: center;
}

.delete-button {
  padding: 6px 12px;
  background-color: #c33b49;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.delete-button:hover {
  background-color: #c82333;
}

.no-reservation-message {
  color: #999;
  font-size: 18px;
  text-align: center;
}


</style>