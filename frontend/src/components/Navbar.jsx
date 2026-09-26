import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <div style={styles.logo}>✈️ TravelHub</div>
      <div style={styles.links}>
        <NavLink to="/" style={styles.link}>Início</NavLink>
        <NavLink to="/voos" style={styles.link}>Voos</NavLink>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: 'flex',
    justifyContent: 'space-between',
    padding: '1rem 2rem',
    background: '#1e293b',
    color: '#fff',
  },
  logo: { fontSize: '1.2rem', fontWeight: 'bold' },
  links: { display: 'flex', gap: '1rem' },
  link: { color: '#cbd5e1', textDecoration: 'none' }
};
