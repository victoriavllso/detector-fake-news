import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import Stack from '@mui/material/Stack';

interface Props {
  onClick: () => void;
  disabled: boolean
}

export default function IconLabelButtons({ onClick, disabled }: Readonly<Props>) {
  return (
    <Stack direction="row" spacing={2}>
      <Button variant="contained" endIcon={<SendIcon />} size='large' onClick={onClick} disabled={disabled}>
        Analisar veracidade
      </Button>
    </Stack>
  );
}