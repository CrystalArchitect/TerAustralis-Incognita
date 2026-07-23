export const prerender = true;

export function load() {
  // The technical layer — each entry carries its status and where to verify it.
  const protocols = [
    {
      title: 'Consent Transport',
      status: 'Built',
      body: 'Peer-to-peer sovereign memory exchange over a real Noise handshake — consent-gated, revocable on the very next request. Formerly Starline.',
      links: [
        { href: '/consent-transport', label: '→ Explore the page' },
        { href: '/docs/consent-transport', label: '→ Read the spec' }
      ],
      st: 'var(--green)'
    },
    {
      title: 'CrystalMatrix',
      status: 'Design',
      body: 'The networking layer that would let sovereign companions discover and reach each other — local-first, opt-in, no platform in the middle. Design/concept; no implementation yet.',
      links: [
        { href: '/docs/crystalmatrix', label: '→ Read the design' }
      ],
      st: 'var(--blue)'
    }
  ];

  return { protocols };
}
