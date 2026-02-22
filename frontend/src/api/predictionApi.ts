import axios from 'axios';
import type { PredictionResult } from '../types/prediction';

const api = axios.create({
  baseURL: import.meta.env.VITE_URL_BACKEND,
  headers: {
	"Content-Type": "application/json"
  }
 
})

export async function requestPrediction(text: string): Promise<PredictionResult> {
	const response = await api.post<PredictionResult>("/predict", { text }); // axios já faz JSON.stringfy internamente
	console.log("debugando texto enviado para o back", response)
	return response.data
		
}

// implementar o get para quando tiver armazenamento em BD (vai bucar em predict/{id})