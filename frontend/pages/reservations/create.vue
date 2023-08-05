<template>
  <div>
    <h2>Fazer Nova Reserva</h2>
    <div v-if="isLoading">
      Carregando...
    </div>
    <div v-else>
    <form @submit.prevent="createReservation">
      <label for="reservation-date">Data da Reserva:</label>
      <input type="date" id="reservation-date" v-model="reservationDate" required>

      <label for="work-station">Estação de Trabalho:</label>
      <select id="work-station" v-model="workStationId" required>
        <option v-for="workStation in stations" :key="workStation.id" :value="workStation.id">{{ workStation.station }}</option>
      </select>
      <button type="submit">Criar Reserva</button>
    </form>
    </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      stations: [],
      isLoading: true,
      reservationDate: '',
      workStationId: null,
    };
  },
  mounted() {
    this.getStations()
  },
  methods: {
    ...mapActions('stations', ['getStationsAction']),
    ...mapActions('reservations', ['createReservationAction']),

    async getStations() {
    const token = localStorage.getItem('token');
      if (!token) {
          this.$router.push('/');
          return;
        }

    const { status, data } = await this.getStationsAction(token);
      if (status === 200) {
        this.stations = data;
        this.isLoading = false;
      }
    },

    async createReservation() {
      const token = localStorage.getItem('token');
      if (!token) {
        this.$router.push('/');
        return;
      }

      const userStorage = localStorage.getItem('user');
      const user = JSON.parse(userStorage)

      const reservationData = {
        reservation_date: this.reservationDate,
        work_station_id: this.workStationId,
        user_id: Number(user.id)
      };

      const { status, data } = await this.createReservationAction({ token, reservationData })
      if (status === 200) {
        this.reservations = data;
        this.isLoading = false;
      }
    },
    },
};
</script>

<style>

</style>