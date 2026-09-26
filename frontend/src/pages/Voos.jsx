import { useVoos } from '../hooks/useVoos'
import TabelaFlight from '../components/TabelaFlight'

export default function Voos() {
	const { data, isLoading, error } = useVoos()

	const voos = Array.isArray(data) ? data : []

	if (isLoading) {
		return <div style={{ padding: '20px' }}>Carregando voos...</div>
	}

	if (error) {
		return <div style={{ padding: '20px', color: 'red' }}>Erro: {error.message}</div>
	}

	return (
		<div style={{ padding: '20px' }}>
			<h2>Painel de Voos</h2>
			<TabelaFlight voos={voos} />
		</div>
	)
}
