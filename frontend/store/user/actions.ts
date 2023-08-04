import axios from 'axios';

export default {
loginUser: async (context: any, { email, password }: any) => {
  let isAuthenticated = false;
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/get-csrf-token');
      const token = response.data['X-CSRFToken'];
      const headers = {
        'X-CSRFToken': token,
        'Content-Type': "application/json"
      };
      const data = {
        email: email,
        password: password
      };
      const { status, data: logData } = await axios.post('http://127.0.0.1:8000/api/v1/login', data, {
        headers });

      if (status === 200) {
      return {
        isAuthenticated: true,
        token: `Bearer ${logData.access_token}`,
        user: logData.user }
      }
    } catch (error) {
      console.error('Erro na requisição de login:', error);
    }
  return { isAuthenticated, token: '' };
  }
}