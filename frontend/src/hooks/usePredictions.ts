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
    } catch (err) {
      setError("Erro ao processar predição. Tente novamente.");
      setResult(null);
	  console.log("erro capturado", err)
    } finally {
      setLoading(false);
    }
  };
  return { result, loading, error, handleRequest };
}