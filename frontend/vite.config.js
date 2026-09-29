import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Faz /api/* do frontend ir para o back-end (FastAPI)
      '/api': 'http://localhost:8000',
    },
  },
})
