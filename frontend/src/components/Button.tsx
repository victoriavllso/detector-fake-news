import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import Stack from '@mui/material/Stack';

interface Props {
  onClick: () => void;
}

export default function IconLabelButtons({ onClick }: Props) {
  return (
    <Stack direction="row" spacing={2}>
      <Button variant="contained" endIcon={<SendIcon />} size='large' onClick={onClick}>
        Analisar veracidade
      </Button>
    </Stack>
  );
}