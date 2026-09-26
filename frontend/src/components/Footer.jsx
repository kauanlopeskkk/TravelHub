export default function Footer() {
  return (
    <footer style={styles.footer}>
      <p>&copy; {new Date().getFullYear()} TravelHub Aeroporto. Todos os direitos reservados.</p>
    </footer>
  );
}

const styles = {
  footer: {
    textAlign: 'center',
    padding: '1rem',
    background: '#0080ff',
    marginTop: 'auto'
  }
};




