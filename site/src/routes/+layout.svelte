<script>
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import { Analytics } from '@vercel/analytics/sveltekit';

  /** @type {{ children: import('svelte').Snippet }} */
  let { children } = $props();
</script>

<Analytics />

<div class="stars" aria-hidden="true"></div>

<div class="wrap">
  <div class="starline" aria-hidden="true"></div>

  <Header />

  {@render children()}
</div>
