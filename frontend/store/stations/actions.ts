import axios from 'axios';

export default {
  getStationsAction: async (context: any, token: string) => {
    let status = false;
      try {
        // const headers = {
        //   'Authorization': token,
        //   'Content-Type': "application/json"
        // };

        const { status, data: logData } = await axios.get('http://127.0.0.1:8000/api/v1/stations');

        if (status === 200) {
        return { status, data: logData }
      }
    } catch (error) {
      console.error('Erro na requisição de stations:', error);
    }
    return { status, data: [] };
  }
}