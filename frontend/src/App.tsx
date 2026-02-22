import { useState } from 'react'
import './App.css'
import InputText from './components/InputText.tsx'
import TextFieldContainer  from './components/TextFieldContainer.tsx'
import IconLabelButtons from './components/Button.tsx'
import { Box } from '@mui/material'
import { css } from '@emotion/css'
import { usePrediction } from './hooks/usePredictions.ts'

function App() {
  const [text, setText] = useState('')
  const { result, loading, error, handleRequest } = usePrediction()


  return (
    <Box className={styles.CenteredColumn}>
      <TextFieldContainer title='Insira o texto da notícia'>  
        <InputText value={text} onChange={setText}/>
      </TextFieldContainer>
      <IconLabelButtons onClick={() => handleRequest(text)} disabled={loading}/>
        {loading && <p>Processando...</p>}
     
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {result && (
          <div className={styles.ResultArea}>
            <h3>Resultado: {result.classification}</h3>
            <h3>Percentual: {result.confidence}</h3>
          </div>
        )}
      <p className="read-the-docs">
        O modelo trata-se de um modelo probabilístico, ou seja, pode cometer falhas.
        Garanta 100% de confiança procurando em outras fontes.
     </p>
    </Box>
  )
}

export default App

const styles = {
  CenteredColumn: css`
  display: flex;
  flex-direction: column;
  width: 800px;
  margin: 0 auto;
  gap: 16px;
  margin-top:32px;
  align-items: center;
  `,
  ResultArea: css`
    margin-top: 20px;
    padding: 20px;
    background-color: #000000;
    border: 2px solid #007bff;
    border-radius: 8px;
    width: 100%;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  `,
  Label: css`
    color: #0056b3;
    font-size: 1.5rem;
    margin: 0;
    font-weight: bold;
  `
}
