// frontend/src/pages/Home.jsx
import { useState } from 'react';

const style = {
  button: {
    backgroundColor: 'red',
  },
};

export default function Home() {
  const [message, setMessage] = useState('Bem-vindo ao site Aeroporto!');

  return (
    <div style={{ textAlign: 'center', padding: '50px' }}>
      <h1>{message}</h1>
      <button style={style.button} onClick={() => setMessage('Aeroporto pronto!')}>
        Clique aqui
      </button>
    </div>
  );
}
