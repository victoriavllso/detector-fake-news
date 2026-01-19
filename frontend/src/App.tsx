import { useState } from 'react'
import './App.css'
import InputText from './components/InputText.tsx'
import TextFieldContainer  from './components/TextFieldContainer.tsx'
import IconLabelButtons from './components/Button.tsx'
import { Box } from '@mui/material'
import { css } from '@emotion/css'


function App() {
  const [text, setText] = useState('')

  return (
    <Box className={styles.CenteredColumn}>
      <TextFieldContainer title='Insira o texto da notícia'>  
        <InputText
        value={text}
        onChange={setText}
        />
      </TextFieldContainer>
      <IconLabelButtons >
      </IconLabelButtons>
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
  `
}
