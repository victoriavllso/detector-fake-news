import { TextField } from '@mui/material'

type inputTextProps = {
	value: string
	onChange: (value: string) => void
}

export default function inputText({value, onChange}: inputTextProps) {

  return (
      <TextField
        label="Cole o corpo da notícia aqui..."
		    sx={{width:800}}
		    rows={15}
        multiline
		    value={value}
		    onChange={(e) => onChange(e.target.value)}
      />

  )
}
