export const prerender = true;

export function load() {
  // The creative layer — stories and music, linked out to where they already live.
  const works = [
    {
      title: 'The Codex',
      body: 'The living archive — chapters I–V, from the southern dream to the reach for the stars.',
      href: '/codex',
      cta: '→ Read the Codex',
      st: 'var(--purple)'
    },
    {
      title: 'The Apocryphon',
      body: 'The companion text. In the beginning was not the Word, but the Vibration.',
      href: '/apocryphon',
      cta: '→ Read the Apocryphon',
      st: 'var(--blue)'
    },
    {
      title: 'The Book of the Sovereign Key',
      body: 'The founding myth — the Southern Anchor, and the first Starline to sing.',
      href: '/docs/the-sovereign-key',
      cta: '→ Read it',
      st: 'var(--gold)'
    },
    {
      title: 'The Starline Transmissions',
      body: 'The Vision-layer myth beside the running code — sovereign threads of consent, told as story.',
      href: '/docs/starline-transmissions',
      cta: '→ Read the Transmissions',
      st: 'var(--green)'
    },
    {
      title: 'The Soundtrack',
      body: 'Original music from the Crystal universe — the Starline Transmissions, on Suno.',
      href: 'https://suno.com/@m13crystalat',
      cta: '→ On Suno',
      st: 'var(--pink)',
      external: true
    }
  ];

  return { works };
}
