import { useState } from 'react'
import './App.css'
import InputText from './components/InputText.tsx'
import TextFieldContainer  from './components/TextFieldContainer.tsx'
import IconLabelButtons from './components/Button.tsx'
import { Box } from '@mui/material'
import { css } from '@emotion/css'
import { usePrediction } from './hooks/usePredictions.ts'
import { Gauge, gaugeClasses } from '@mui/x-charts/Gauge';


function App() {
  const [text, setText] = useState('')
  const { result, loading, error, handleRequest } = usePrediction()
  
  const getColor = (classification: string) => {
    return classification.toLowerCase().includes('fake') ? colors.fake : colors.true;
  }

  const numericValue = result ? result.confidence * 100 : null 
  const formattedValue = numericValue ? numericValue.toFixed(1) : null
  
  return (
      <Box className={styles.MainCard}>
        
        <div className={styles.Header}>
          <h1 className={styles.Title}>Detector de Fake News</h1>
        </div>
       
        <TextFieldContainer title=''>  
          <InputText value={text} onChange={setText}/>
        </TextFieldContainer>

        <IconLabelButtons onClick={() => handleRequest(text)} disabled={loading || !text}/>
        
        {loading && <p className={styles.LoadingText}>Analisando padrões no texto...</p>}
        {error && <p className={styles.ErrorText}>{error}</p>}
        
        {result && (
          <div className={styles.ResultBox}>
            <div className={styles.ResultTextContainer}>
              <span className={styles.ResultPreTitle}>Resultado do modelo:</span>
              <h3 
                className={styles.Label} 
                style={{ color: getColor(result.classification) }}
                >
                {result.classification.toUpperCase()}
              </h3>
            </div>

            <div className={styles.GaugeContainer}>
              <Gauge 
                width={200} 
                height={200} 
                value={numericValue ?? 0} 
                text={`${formattedValue}%`}
                sx={{
                  [`& .${gaugeClasses.valueArc}`]: {
                    fill: getColor(result.classification),
                  },
                  [`& .${gaugeClasses.referenceArc}`]: {
                    fill: colors.gaugeTrack,
                  },
                  [`& .${gaugeClasses.valueText}`]: {
                    fontSize: 32,
                    fontWeight: 800,
                    fill: colors.gaugeTrack,
                  },
                }}
              />
            </div>
          </div>
        )}

        <p className={styles.Disclaimer}>
          O modelo é de natureza probabilística e pode cometer falhas. 
          Recomenda-se validar as informações consultando fontes adicionais oficiais.
        </p>
      </Box>
  )
}

export default App

const colors = {
  fake: '#e53935',
  true: '#43a047',
  label: '#2c3e50',
  background: '#f4f7f6',
  gaugeText: '#1e293b',
  gaugeTrack: '#e2e8f0'
};
const styles = {

  MainCard: css`
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08); /* Sombra elegante */
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 800px; /* Limita a largura em telas grandes */
    padding: 40px;
    gap: 24px;
    align-items: center;
  `,
  Header: css`
    text-align: center;
    margin-bottom: 10px;
  `,
  Title: css`
    margin: 0;
    font-size: 2rem;
    color: ${colors.label};
    font-weight: 800;
  `,
  Subtitle: css`
    margin: 8px 0 0 0;
    color: #64748b;
    font-size: 1rem;
  `,
  ResultBox: css`
    margin-top: 16px;
    padding: 30px 40px;
    width: 100%;
    background-color: #f8fafc; /* Um fundo bem suave para a área de resultado */
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    display: flex;
    justify-content: space-evenly; /* Mantém os itens próximos, mas com respiro */
    align-items: center;
    box-sizing: border-box;
  `,
  ResultTextContainer: css`
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  `,
  ResultPreTitle: css`
    font-size: 0.9rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
    margin-bottom: 4px;
  `,
  Label: css`
    font-size: 3.5rem; /* Título gigante e impactante */
    margin: 0;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -1px;
  `,
  GaugeContainer: css`
    display: flex;
    justify-content: center;
    align-items: center;
  `,
  LoadingText: css`
    color: #3b82f6;
    font-weight: 500;
  `,
  ErrorText: css`
    color: ${colors.fake};
    background-color: #fee2e2;
    padding: 12px;
    border-radius: 8px;
    width: 100%;
    text-align: center;
  `,
  Disclaimer: css`
    font-size: 0.85rem;
    color: #94a3b8;
    text-align: center;
    max-width: 90%;
    margin-top: 20px;
    line-height: 1.5;
  `
}