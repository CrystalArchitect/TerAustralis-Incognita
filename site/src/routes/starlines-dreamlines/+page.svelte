<script>
  import Footer from '$lib/components/Footer.svelte';

  let { data } = $props();
</script>

<svelte:head>
  <title>Starlines & Dreamlines — TerAustralis Incognita</title>
</svelte:head>

<section class="section node" style="--node:var(--purple)">
  <h2>Starlines &amp; Dreamlines</h2>
  <p>
    The creative layer of the project — the stories and the music, kept honestly separate from the
    software. <strong>Starlines are the map; Dreamlines are the traveller of the map.</strong>
  </p>
</section>

<section class="section node" style="--node:var(--pink)">
  <h2>The works</h2>
  <div class="cards">
    {#each data.works as work (work.href)}
      <a
        class="card"
        href={work.href}
        style="--st:{work.st}"
        target={work.external ? '_blank' : undefined}
        rel={work.external ? 'noopener noreferrer' : undefined}
      >
        <h3>{work.title}</h3>
        <p>{work.body}</p>
        <span class="status">{work.cta}</span>
      </a>
    {/each}
  </div>
</section>

<Footer />
