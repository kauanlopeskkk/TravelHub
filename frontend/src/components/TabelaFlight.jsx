import React from 'react';

// Função para aplicar a cor do status
function getStatusBadge(status) {
  const s = status?.toLowerCase() || '';
  if (s.includes('embarque')) return 'badge badge-embarque';
  if (s.includes('em sala')) return 'badge badge-em-sala';
  if (s.includes('atrasado')) return 'badge badge-atrasado';
  if (s.includes('cancelado')) return 'badge badge-cancelado';
  return 'badge';
}

export default function TabelaFlight({ voos }) {
  if (!voos || voos.length === 0) {
    return <div className="container">Nenhum voo encontrado.</div>;
  }

  return (
    <div className="table-container">
      <table className="flight-table">
        <thead>
          <tr>
            <th>Voo</th>
            <th>Companhia</th>
            <th>Origem → Destino</th>
            <th>Status</th>
            <th>Terminal / Portão</th>
          </tr>
        </thead>
        <tbody>
          {voos.map((voo) => (
            <tr key={voo.id || voo.flightNumber}>
              <td className="flight-number">{voo.flightNumber}</td>
              <td>{voo.airline || '-'}</td>
              <td className="flight-route">{voo.origin} → {voo.destination}</td>
              <td>
                <span className={getStatusBadge(voo.status)}>
                  {voo.status}
                </span>
              </td>
              <td>{voo.terminal ? `${voo.terminal} / ${voo.gate}` : '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
