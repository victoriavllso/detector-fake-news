import { useState } from 'react'
import { requestPrediction } from '../api/predictionApi';
import type { PredictionResult } from '../types/prediction';


export function usePrediction() {
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRequest = async (text: string) => {
    if (!text.trim()) return;

    setLoading(true);
    setError(null);
    try {
      const response = await requestPrediction(text);
      setResult(response);
    }catch (err: any) {
  console.log("erro completo:", err);

  if (err.response) {
    console.log("status:", err.response.status);
    console.log("data:", err.response.data);
  } else if (err.request) {
    console.log("sem resposta do servidor:", err.request);
  } else {
    console.log("erro ao configurar requisição:", err.message);
  }

  setError("Erro ao processar predição. Tente novamente.");
  setResult(null);
  }finally {
      setLoading(false);
    }
  };
  return { result, loading, error, handleRequest };
}