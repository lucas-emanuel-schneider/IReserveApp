import axios from 'axios';

export default {
  getReservationsAction: async (context: any, token: string) => {
    let status = false;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };
        // , {
        //   headers: headers,
        //   }
        const { status, data: logData } = await axios.get('http://127.0.0.1:8000/api/v1/reservations/2');

        if (status === 200) {
        return { status, data: logData }
      }
    } catch (error) {
      console.error('Erro na requisição de reservas:', error);
    }
    return { status, data: [] };
  }
}