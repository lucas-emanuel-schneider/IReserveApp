import axios from 'axios';

export default {
  getReservationsAction: async (context: any, {token, id}: any) => {
    let status = false;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };
        // , {
        const { status, data: logData } = await axios.get(`http://127.0.0.1:8000/api/v1/reservations/${id}`);

        if (status === 200) {
        return { status, data: logData }
      }
    } catch (error) {
      console.error('Erro na requisição de reservas:', error);
    }
    return { status, data: [] };
  },
    createReservationAction: async (context: any, { token, reservationData }: any) => {
      let status = false;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };
        // , {
        const { status, data: logData } = await axios.post('http://127.0.0.1:8000/api/v1/reservations/create',
        reservationData);

        if (status === 200) {
        return { status, data: logData }
      }
    } catch (error) {
      console.error('Erro na requisição de criação de reservas:', error);
    }
    return { status, data: [] };
  }
}