import { Box, Typography } from '@mui/material'

interface TextFieldContainerProps {
  title: string
  children: React.ReactNode
}

export default function TextFieldContainer({
  title,
  children
}: Readonly<TextFieldContainerProps>) {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, alignItems: 'center' }}>
      <Typography variant="h4" fontWeight={500} sx={{color: 'black'}}>
        {title}
      </Typography>

      {children}
    </Box>
  )
}
