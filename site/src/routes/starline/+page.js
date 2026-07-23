import { redirect } from '@sveltejs/kit';

// Old route kept as a permanent redirect so links to /starline survive the
// rename to /consent-transport. With adapter-static this prerenders a small
// redirect page.
export const prerender = true;

export function load() {
  redirect(301, '/consent-transport');
}
