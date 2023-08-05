<template>
  <div class="reservation-form">
    <h2>Fazer Nova Reserva</h2>
    <div v-if="isLoading">
      <Loading />
    </div>
    <div v-else>
      <form @submit.prevent="createReservation" class="form-container">
        <label for="reservation-date" class="form-label">Data da Reserva:</label>
        <input type="date" id="reservation-date" v-model="reservationDate" required class="form-input">

        <label for="work-station" class="form-label">Estação de Trabalho:</label>
        <select id="work-station" v-model="workStationId" required class="form-select">
          <option v-for="workStation in stations" :key="workStation.id" :value="workStation.id">{{ workStation.station }}</option>
        </select>
        <button type="submit" class="form-button">Criar Reserva</button>
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
    this.getStations();
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

      const { status } = await this.createReservationAction({ token, reservationData });
      if (status !== 201) return window.alert('Não foi possivel criar a reserva!')
        this.isLoading = false;
        window.alert('Reserva criada!');
        this.reservationDate = '';
        this.workStationId = null;
    },
    },
};
</script>

<style>
.reservation-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-size: 16px;
  margin-bottom: 8px;
}

.form-input,
.form-select {
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 12px;
}

.form-button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.form-button:hover {
  background-color: #0056b3;
}

.select-wrapper {
  position: relative;
}

.select-wrapper::after {
  content: "\25BE";
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}
</style>