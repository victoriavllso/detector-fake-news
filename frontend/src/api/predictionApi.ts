import axios from 'axios';


const api = axios.create({
  baseURL: import.meta.env.VITE_URL_BASE,
  headers: {
	"Content-Type": "application/json"
  }
 
})

export async function requestPrediction(text: string) {
	const response = await api.post("/predict", { text }); // axios já faz JSON.stringfy internamente
	console.log("debugando texto enviado para o back", response)
	return response.data
		
}

// implementar o get para quando tiver armazenamento em BD (vai bucar em predict/{id})