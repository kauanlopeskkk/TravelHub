export async function listVoos() {
  const res = await fetch("/api/voos");

  if (!res.ok) {
    let details = null;
    try {
      details = await res.json();
    } catch {}

    const msg = details?.message || `Erro na API (${res.status})`;
    throw new Error(msg);
  }

  return res.json();
}
