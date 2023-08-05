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
      let status = 404;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };
        // , {
        const { status } = await axios.post('http://127.0.0.1:8000/api/v1/reservations/create',
        reservationData);

        if (status === 201) {
        return { status }
      }
    } catch (error) {
      console.error('Erro na requisição de criação de reservas:', error);
    }
    return { status };
  },
    deleteReservationAction: async (context: any, { token, id }: { token: string; id: number }) => {
      let status = false;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };
        // , {
        const { status } = await axios.delete(`http://127.0.0.1:8000/api/v1/reservations/delete/${id}`);

        if (status === 204) {
        return { status }
      }
    } catch (error) {
      console.error('Erro na requisição de criação de reservas:', error);
    }
    return { status };
  }
}